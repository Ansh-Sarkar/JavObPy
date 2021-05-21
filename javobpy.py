import sys
conversion_map = dict()

def string_gen(data):
	global conversion_map
	if data in conversion_map:
		return conversion_map[data]
	else:
		res = []
		for val in data:
			res.append(conversion_map.get(val, "'"+val+"'"))
		return "+".join(res)

def gen_ascii_arr(data):
	return [str(ord(i)) for i in data]

def minifier(source_file):
    newFile = source_file.split(".js")[0] + ".min.js"
    try:
        src = open(source_file, "r+")
    except:
        print("An error occured while opening the requested file")
        return
    in_stream = src.readlines()
    if(ord(in_stream[len(in_stream) - 1][len(in_stream[len(in_stream) - 1]) - 1]) != 10 or ord(in_stream[len(in_stream) - 1][len(in_stream[len(in_stream) - 1]) - 1]) != 32):  # 10 -> LF, 32 -> Space
        src.close()
        src = open(source_file, "a+")
        src.write(" ")
        src.close()
    src = open(source_file, "r+")
    out = open(newFile, "w+")
    in_stream = src.readlines()
    for i in range(0, len(in_stream)):
        token = ""
        for j in range(0, len(in_stream[i])):
            if(ord(in_stream[i][j]) == 10 or ord(in_stream[i][j]) == 32 or ord(in_stream[i][j]) == 9):
                if(token == "function" or token == "const" or token == "var" or token == "let" or token == "class" or token == "new" or token == "return"):
                    out.write(token + " ")
                    token = ""
                else:
                    out.write(token)
                    token = ""
            elif(ord(in_stream[i][j-1]) != 58 and ord(in_stream[i][j]) == 47 and ord(in_stream[i][j+1]) == 47):
                break
            else:
                token = token + in_stream[i][j]
    src.close()
    out.close()
    return newFile

def table_gen():
	global conversion_map
	conversion_map[0] = '+[]'
	conversion_map[1] = '+!![]'
	conversion_map[2] = '!![]+!![]'
	conversion_map[3] = '!![]+!![]+!![]'
	conversion_map[4] = '!![]+!![]+!![]+!![]'
	conversion_map[5] = '!![]+!![]+!![]+!![]+!![]'
	conversion_map[6] = '!![]+!![]+!![]+!![]+!![]+!![]'
	conversion_map[7] = '!![]+!![]+!![]+!![]+!![]+!![]+!![]'
	conversion_map[8] = '!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]'
	conversion_map[9] = '!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]'
	conversion_map['0'] = '('+conversion_map[0]+'+[])'
	conversion_map['1'] = '('+conversion_map[1]+'+[])'
	conversion_map['2'] = '('+conversion_map[2]+'+[])'
	conversion_map['3'] = '('+conversion_map[3]+'+[])'
	conversion_map['4'] = '('+conversion_map[4]+'+[])'
	conversion_map['5'] = '('+conversion_map[5]+'+[])'
	conversion_map['6'] = '('+conversion_map[6]+'+[])'
	conversion_map['7'] = '('+conversion_map[7]+'+[])'
	conversion_map['8'] = '('+conversion_map[8]+'+[])'
	conversion_map['9'] = '('+conversion_map[9]+'+[])'
	conversion_map[''] = '([]+[])'
	conversion_map['true'] = '(!![]+[])'
	conversion_map['false'] = '(![]+[])'
	conversion_map['NaN'] = '(+[![]]+[])'
	conversion_map['NaN'] = '(+{}+[])'
	conversion_map['undefined'] = '([][[]]+[])'
	conversion_map['[object Object]'] = '({}+[])'
	conversion_map['a'] = conversion_map['false']+'['+conversion_map[1]+']'
	conversion_map['b'] = conversion_map['[object Object]'] + \
		'['+conversion_map[2]+']'
	conversion_map['c'] = conversion_map['[object Object]'] + \
		'['+conversion_map[5]+']'
	conversion_map['d'] = conversion_map['undefined']+'['+conversion_map[2]+']'
	conversion_map['e'] = conversion_map['true']+'['+conversion_map[3]+']'
	conversion_map['Infinity'] = '(+('+conversion_map[1]+'+'+conversion_map['e']+'+('+conversion_map[1] + \
            ')+('+conversion_map[0]+')+('+conversion_map[0] + \
            ')+('+conversion_map[0]+'))+[])'
	conversion_map['f'] = conversion_map['false']+'['+conversion_map[0]+']'
	conversion_map['i'] = conversion_map['undefined']+'['+conversion_map[5]+']'
	conversion_map['j'] = conversion_map['[object Object]'] + \
		'['+conversion_map[3]+']'
	conversion_map['l'] = conversion_map['false']+'['+conversion_map[2]+']'
	conversion_map['n'] = conversion_map['undefined']+'['+conversion_map[1]+']'
	conversion_map['o'] = conversion_map['[object Object]'] + \
		'['+conversion_map[1]+']'
	conversion_map['r'] = conversion_map['true']+'['+conversion_map[1]+']'
	conversion_map['s'] = conversion_map['false']+'['+conversion_map[3]+']'
	conversion_map['t'] = conversion_map['true']+'['+conversion_map[0]+']'
	conversion_map['u'] = conversion_map['true']+'['+conversion_map[2]+']'
	conversion_map['y'] = conversion_map['Infinity']+'['+conversion_map[7]+']'
	conversion_map['I'] = conversion_map['Infinity']+'['+conversion_map[0]+']'
	conversion_map['N'] = conversion_map['NaN']+'['+conversion_map[0]+']'
	conversion_map['O'] = conversion_map['[object Object]'] + \
		'['+conversion_map[8]+']'
	conversion_map[','] = '[[],[]]+[]'
	conversion_map['['] = conversion_map['[object Object]'] + \
		'['+conversion_map[0]+']'
	conversion_map[']'] = conversion_map['[object Object]'] + \
		'['+conversion_map['1']+'+('+conversion_map[4]+')]'
	conversion_map[' '] = conversion_map['[object Object]'] + \
		'['+conversion_map[7]+']'
	conversion_map['"'] = conversion_map[''] + \
            '['+string_gen('fontcolor')+']()['+conversion_map['1'] + \
            '+('+conversion_map[2]+')]'
	conversion_map['<'] = conversion_map[''] + \
		'['+string_gen('sub')+']()['+conversion_map[0]+']'
	conversion_map['='] = conversion_map[''] + \
            '['+string_gen('fontcolor')+']()['+conversion_map['1'] + \
            '+('+conversion_map[1]+')]'
	conversion_map['>'] = conversion_map[''] + \
		'['+string_gen('sub')+']()['+conversion_map[4]+']'
	conversion_map['/'] = conversion_map[''] + \
		'['+string_gen('sub')+']()['+conversion_map[6]+']'
	conversion_map['+'] = '(+('+conversion_map[1]+'+'+conversion_map['e']+'+['+conversion_map[1] + \
            ']+('+conversion_map[0]+')+('+conversion_map[0] + \
            '))+[])['+conversion_map[2]+']'
	conversion_map['.'] = '(+('+conversion_map[1]+'+['+conversion_map[1]+']+'+conversion_map['e'] + \
            '+('+conversion_map[2]+')+('+conversion_map[0] + \
            '))+[])['+conversion_map[1]+']'
	conversion_map[','] = '([]['+string_gen('slice')+']['+string_gen('call') + \
            ']'+conversion_map['[object Object]']+'+[])['+conversion_map[1]+']'
	conversion_map['[object Window]'] = '([]['+string_gen('filter')+']['+string_gen(
		'constructor')+']('+string_gen('return self')+')()+[])'
	conversion_map['W'] = conversion_map['[object Window]'] + \
		'['+conversion_map[8]+']'
	conversion_map['h'] = '([]['+string_gen('filter')+']['+string_gen('constructor') + \
            ']('+string_gen('return location')+')()+[])['+conversion_map[0]+']'
	conversion_map['p'] = '([]['+string_gen('filter')+']['+string_gen('constructor') + \
            ']('+string_gen('return location')+')()+[])['+conversion_map[3]+']'
	conversion_map['m'] = '[]['+string_gen('filter')+']['+string_gen(
		'constructor')+']('+string_gen('return typeof 0')+')()['+conversion_map[2]+']'
	conversion_map['C'] = '[]['+string_gen('filter')+']['+string_gen('constructor')+']('+string_gen(
		'return escape')+')()('+conversion_map['1']+'['+string_gen("sub")+']())['+conversion_map[2]+']'
	conversion_map['('] = '([]['+string_gen('filter')+']+[])[' + \
            string_gen('trim')+']()['+conversion_map['1'] + \
            '+('+conversion_map[5]+')]'
	conversion_map[')'] = '([]['+string_gen('filter')+']+[])[' + \
            string_gen('trim')+']()['+conversion_map['1'] + \
            '+('+conversion_map[6]+')]'
	conversion_map['{'] = '([]['+string_gen('filter')+']+[])[' + \
            string_gen('trim')+']()['+conversion_map['1'] + \
            '+('+conversion_map[8]+')]'
	conversion_map['g'] = '[]['+string_gen('filter')+']['+string_gen(
		'constructor')+']('+string_gen('return typeof""')+')()['+conversion_map[5]+']'
	conversion_map['%'] = '[]['+string_gen('filter')+']['+string_gen(
		'constructor')+']('+string_gen('return escape')+')()({})['+conversion_map[0]+']'
	conversion_map['B'] = '[]['+string_gen('filter')+']['+string_gen(
		'constructor')+']('+string_gen('return escape')+')()({})['+conversion_map[2]+']'
	conversion_map['S'] = '[]['+string_gen('filter')+']['+string_gen('constructor')+'](' + \
            string_gen('return unescape')+')()(' + \
            conversion_map['%']+'+'+conversion_map['5'] + \
            '+('+conversion_map[3]+'))'
	conversion_map['x'] = '[]['+string_gen('filter')+']['+string_gen('constructor')+'](' + \
            string_gen('return unescape')+')()(' + \
            conversion_map['%']+'+'+conversion_map['7'] + \
            '+('+conversion_map[8]+'))'
	conversion_map['v'] = '[]['+string_gen('filter')+']['+string_gen('constructor')+'](' + \
            string_gen('return unescape')+')()(' + \
            conversion_map['%']+'+'+conversion_map['7'] + \
            '+('+conversion_map[6]+'))'
	return

def obfuscator(code):
	global conversion_map
	if len(conversion_map) == 0:
		table_gen()
	converted_string = ','.join(string_gen(str(x))
                             for x in gen_ascii_arr(code))
	converted_string = '[]['+string_gen('filter')+']['+string_gen('constructor')+'](' + \
            string_gen('return String') + \
            ')()['+string_gen('fromCharCode')+']('+converted_string+')'
	converted_string = '[]['+string_gen('filter')+'][' + \
            string_gen('constructor')+']('+converted_string+')()'
	return converted_string

def main():
	if len(sys.argv) != 2:
		print('Syntax : python main.py <filepath>.js')
		return

	minified_file = minifier(sys.argv[1])
	with open(minified_file, 'r') as f:
		before = f.read()
	final = minified_file.split('.')
	after = obfuscator(before)
	with open(final[0]+'-secure.js', 'w+') as f:
		f.write(after)
	print(after)

if __name__ == '__main__':
	main()

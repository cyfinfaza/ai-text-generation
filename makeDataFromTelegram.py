import json

with open('result.json', encoding='utf-8') as file:
	data = json.load(file)

outputLines = []

lastAuthor = ''
for line in data['messages']:
	if 'text' in line and isinstance(line['text'], str) and line['text'] != '' and 'from' in line:
		if line['from'] != lastAuthor:
			outputLines.append('⥹')
		lastAuthor = line['from']
		outputLines.append(line['text'])

def strGen(lines):
	coll = []
	colls = []
	for line in lines:
		if line == '⥹':
			if len(coll) > 0:
				colls.append(coll)
			coll = []
		else:
			coll.append(line)
	return '⥹'.join('\n'.join(coll) for coll in colls)


with open('telegramMessages2.txt', 'wb') as file:
	file.write(bytes(strGen(outputLines), 'utf-8'))
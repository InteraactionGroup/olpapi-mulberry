import json
import wordnets
wn = wordnets.WordNet('eng')

mulberry = open('names.txt').read().split('\n')[:-1]

output = {}
counts = []

for i in range(len(mulberry)):
	words = mulberry[i].replace('_-_', '_').replace('_,_to', '').split('_')
	if words[-1][0].isnumeric(): words.pop()
	synsets_per_word = [wn.get_synsets(word) for word in words]
	if [] in synsets_per_word: print(words[synsets_per_word.index([])])
	count = 0
	for synsets in synsets_per_word:
		for synset in synsets:
			if synset in output: output[synset].append(i)
			else: output[synset] = [i]
		count += len(synsets)
	counts.append(count)

json.dump(output, open('svg.mulberry.color.json', 'w'))
json.dump(counts, open('svg.mulberry.color.counts.json', 'w'))

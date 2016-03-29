with open('hamlet.txt') as fin:
    hamlet = fin.read().split('\n')
    
line_lengths = []
for line in hamlet:
    line_syllables = 0
    tokens = word_tokenize(line.lower())
    for token in tokens:
        if token in words:
            pron = dictionary[token][0]
            for phon in pron:
                for char in phon:
                    if char.isdigit():
                        line_syllables+=1
    line_lengths.append(line_syllables)

print(sum(line_lengths)/len(line_lengths))
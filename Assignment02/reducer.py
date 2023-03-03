import re

words2count = {}

for line in file:
    line = line.strip().lower()  
    words2 = filter(None, re.split(r'\W+', line))

    for word in words2:
        try:
            words2count[word] += 1
        except KeyError:
            words2count[word] = 1

# sorting by desc
sorted_words = sorted(words2count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(word, count)
import enchant
from collections import defaultdict

def count_non_english_words(file_path):
    non_english_words = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().lower()  
            words = filter(None, re.split(r'\W+', line))
#         for line in file:
#             words = line.strip().split()
            
            for word in words:
                if not enchant.Dict("en_US").check(word):
                    non_english_words[word.lower()] += 1
    return dict(non_english_words)

file_path = 'TextFile02.txt'
non_english_words = count_non_english_words(file_path)
# print(non_english_words)


sorted_output = sorted(non_english_words.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_output:
    print(word, count)


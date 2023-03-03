with open('TextFile01.txt') as f:
    file = f.readlines()
    
for line in file:
    line1 = line.strip()
    words1 = line.split()
    for word in words1:
        print(word,",1")
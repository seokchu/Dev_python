from collections import Counter

T = int(input())
strlist = []
for _ in range(T):
    strlist.append(input())

count = T

for string in strlist:
    strdict = Counter(string)
    indices = {char: [] for char, n in strdict.items() if n >= 2}

    for i, char in enumerate(string):
        if char in indices:
            indices[char].append(i)
    valid_string = True
    
    for idx_list in indices.values():
        if len(idx_list) > 1:
            for j in range(len(idx_list) - 1):
                if idx_list[j + 1] - idx_list[j] != 1:
                    valid_string = False
                    break
            if not valid_string:
                break   
    if not valid_string:
        count -= 1
print(count)
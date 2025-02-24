from collections import Counter

s = input()
s_upper = s.upper()
s_count = Counter(s_upper)
max_value = max(s_count.values())
max_key = [key for key,values in s_count.items() if values == max_value]
if len(max_key) >= 2:
    print('?')
else:
    print(max_key[0])
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

#normal Dict
d = {}
for k,v in s:
    if k not in d.keys(): #create a key in dict if it doesn't exist
        d[k] = 0
    d[k] += 1
print(d.items())

#Using defaultdict form collections
from collections import defaultdict
dd = defaultdict(int)
for k,v in s:
    dd[k] += 1
print(dd.items())


#problem 1
import re
s = str(input())
p = re.compile('a[b]*') 
m = p.search(s)
print(m)
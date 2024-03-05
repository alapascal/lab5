#problem 1
import re
s = str(input())
p = re.compile('a[b]*') 
m = p.search(s)
print(m)

#problem 2
import re
s = str(input())
p = re.compile('ab{3}|ab{2}')
m = p.search(s)
print(m)

#problem 3
import re
s = str(input())
p = re.compile('[a-z]+_{1}[a-z]+')
m = p.search(s)
print(m)

#problem 4
import re
s = str(input())
p = re.compile('[A-Z]+[a-z]+')
m = p.search(s)
print(m)

#problem 5
import re
s = str(input())
p = re.compile('a.*?b$')
m = p.search(s)
print(m)

#problem 6
import re
s = str(input())
p = re.sub('[ ,.]', ':', s)
print(p)

#problem 8
import re
s = str(input())
p = re.findall('[A-Z][^A-Z]*', s)
print(p)

#problem 9
import re
s = str(input())
p = re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
print(p)

#problem 10
import re
s = str(input())
p = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(p)
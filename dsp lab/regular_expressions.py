import re
txt="find all occurencences"
x=re.findall("ce",txt)
print(x)
y=re.search("in",txt)
print(y)


import re
txt="The rain in spain"
x=re.split("\s",txt)
print(x)

import re
txt="Replace all white spaces"
x=re.sub("\s","7",txt)
print(x)


x=re.findall("[arr]",txt)
print(x)

print(re.findall("[0123]",txt))

txt="8 times before 11:45 AM"
print(re.findall("[a-zA-Z]",txt))


txt="hello planet"
x=re.findall("he.*o",txt)
print(x)






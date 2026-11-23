import re
s="car9340384niuii@&*&$%CARTPE"
print(re.sub("[^a-zA-Z0-9]","",s))

print(re.sub("[a-zA-Z0-9]","",s))

print(re.sub("[a-zA-Z]","",s))

print(re.sub("[^a-zA-Z]","",s))

print(re.sub("[^A-Z]","",s))

print(re.sub("[A-Z]","",s))

print(re.sub("[^a-z]","",s))

print(re.sub("[a-z]","",s))

print(re.sub("[0-9]","",s))

print(re.sub("[^0-9]","",s))
9340384

print(re.sub("[^0-9a-z]","",s))

print(re.sub("[0-9a-z]","",s))

print(re.sub("[^0-9A-Z]","",s))

print(re.sub("[0-9A-Z]","",s))
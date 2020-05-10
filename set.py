s = {'apple', 'orange', 'pear', 'banana'}
s2 = set('hello')
s3 = {i for i in range(1, 11)}
s4 = set()

print(s)
print(s2)
print(s3)
print(s4)

a = set('abracadabra')
b = set('alacazam')

c = a - b
d = a | b
e = a & b
f = a ^ b

print(a, b, c, d, e, f, sep='\n')

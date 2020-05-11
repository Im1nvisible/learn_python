def hello(name, word):
    print('Hello ' + name + '. Say ' + word)

hello('John', 'hi')

def get_sum(a, b):
    return a + b

print(get_sum(1, 3))

def set_register(s):
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()
print(set_register('Hello people'))
print(set_register('Hello,people'))
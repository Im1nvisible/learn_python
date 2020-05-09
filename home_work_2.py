#task_1
#-1
words = ['мадам', 'топот', 'test', 'madam', 'world']
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)
print(palindromes)

#-2
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)

#task_2
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindromes = []
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        palindromes.append(word)

print(palindromes)
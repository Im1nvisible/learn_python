#task_1
l1 = [1, 2, 3]
l1 = [x * 2 for x in l1]
print(l1)

#task_2
l3 = [1, 2, 3]
res = 0
for num in l3:
    res += num ** 2
print(res)

#task_3
time1 = 3
time2 = 6.7
time3 = 11.8

print(time1 // 2)
print(time2 // 2)
print(time3 // 2)

#task_4
s = 'Hello World'
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()
print(s)

def get_sum(a, b):
    '''
    return summ elements

    :param a: first operand
    :type a: int
    :param b: second operand
    :type b: int
    :return: return type int
    '''
    return a + b

#print(get_sum(1, 2))

a = 5 #global

def f():
    global a
    a += 1

print(a)
f()
print(a)


num = [1, '2', 3]
#1
def l(num):
    return [i * 2 for i in num]

print(l(num))


#2
def l2(num):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in num if get_mult(i)]

print(l2(num))
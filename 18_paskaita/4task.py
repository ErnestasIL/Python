
def fib_generator(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def filtruoti_lyginius(seka):
    for sk in seka:
        if sk % 2 == 0:
            yield sk

n = 27
fib_seka = list(fib_generator(n))
print(fib_seka)
print('-' * 20)
fib_lyginiai= list(filtruoti_lyginius(fib_seka))
print(fib_lyginiai)

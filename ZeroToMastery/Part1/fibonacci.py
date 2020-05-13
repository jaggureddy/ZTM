def gen_fib(num):
        f1 = 0
        f2 = 1
        for i in range(num):
            yield f1
            temp = f1
            f1 = f2
            f2 = temp + f2


for x in gen_fib(15):
    print(x)

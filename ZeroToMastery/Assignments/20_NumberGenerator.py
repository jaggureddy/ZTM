class gene:
    def gen(self, n):
        for i in range(n + 1):
            if i % 7 == 0:
                yield i


n = int(input(''))
for num in gene().gen(n):
    print(num)

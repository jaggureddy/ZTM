class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())


class X:
    pass


class Y:
    pass


class Z:
    pass


class P(X, Y):
    pass


class Q(Y, Z):
    pass


class R(Q, P, Z):
    pass


print(R.mro())

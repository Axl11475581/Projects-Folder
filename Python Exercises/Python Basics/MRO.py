# MRO - Method Resolution Order

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


"""
We have a class A, and then a class B that inherits from A, but does
nothing, then a class C that also inherits from A, and lastly class D
that inherits from B and C. MRO is a rule that Python follows to determine 
when you run a method, which one to run.  
"""

print(D.num)

"""
We get 1 because the MRO don't go D, B, A instead it goes D, B, C, and then A.
MRO gets what is first in line.
"""

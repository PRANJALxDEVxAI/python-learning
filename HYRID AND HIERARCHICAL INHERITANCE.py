import math

"""HYBRID INHRITENCE"""

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived(BaseClass):
    pass

class Derived3(Derived1 , Derived2):
    pass


"""HIERARCHICAL INHERITANCE"""

class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(D1):
    pass

class D3(D2):
    pass




"""Exact checks of universal Appendix B coefficient bounds; no flow instance."""
from fractions import Fraction as F

z=F(101,100)
h=F(1,100)
j=F(1,20)
H=F(9,2)*z+4*z**3+j*(1+z*z)
Hp=F(9,2)+12*z*z+2*j*z
assert H<9 and Hp<18
assert 2*h*z*z<F(1,2)
assert 324*F(1,4096)<F(1,2)
assert 1+F(1,1000)+F(1,1000)<z
assert 4*z+j<5
assert 1+z*z<3
assert 1+2*z*5<12
assert 4*F(51,100)*z<5
assert 256*486==124416
assert 80*256==20480
# Finite base plus induction: a_(b+1)/a_b <= 1 for b>=2,
# equivalent to b^2+2b-2>=0. Its forward difference is positive.
assert max(F((b+1)**2,2**b) for b in range(3))<=3
assert 2**2+2*2-2>0
assert 2*2+3>0
print('PASS: universal actual-coefficient triangle and norm constants.')
print('NOT CHECKED: global admissibility, pressure bounds, contraction, completed tail.')

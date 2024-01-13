import gmpy2
from Crypto.Util.number import *
import binascii


c = 9908255308151638808626355523286556242109836830117153917
n = 590872612825179551336102196593
e = 1

p = 416064700201658306196320137931
q = 590872612825179551336102196593

n = p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
m = gmpy2.powmod(c, d, n)
print(long_to_bytes(m))
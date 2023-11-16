from collections import namedtuple as _namedtuple

_ECData = _namedtuple('ECData', ['p', 'a', 'b', 'n', 'Gx', 'Gy'])
_repo = {
  'secp192k1': _ECData(
    p=2**192 - 2**32 - 2**12 - 2**8 - 2**7 - 2**6 - 2**3 - 1, 
    a=0, b=3,
    Gx=0xDB4FF10EC057E9AE26B07D0280B7F4341DA5D1B1EAE06C7D, 
    Gy=0x9B2F2F6D9C5628A7844163D015BE86344082AA88D95E2F9D,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFE26F2FC170F69466A74DEFD8D
  ),
  'secp192r1': _ECData(
    p=2**192 - 2**64 - 1,
    a=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFC,
    b=0x64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1,
    Gx=0x188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012,
    Gy=0x07192B95FFC8DA78631011ED6B24CDD573F977A11E794811,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFF99DEF836146BC9B1B4D22831
  ),
  'secp224k1': _ECData(
    p=2**224 - 2**32 - 2**12 - 2**11 - 2**9 - 2**7 - 2**4 - 2 - 1,
    a=0, b=5,
    Gx=0xA1455B334DF099DF30FC28A169A467E9E47075A90F7E650EB6B7A45C,
    Gy=0x7E089FED7FBA344282CAFBD6F7E319F7C0B0BD59E2CA4BDB556D61A5,
    n=0x010000000000000000000000000001DCE8D2EC6184CAF0A971769FB1F7
  ),
  'secp224r1': _ECData(
    p=2**224 - 2**96 + 1,
    a=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFE,
    b=0xB4050A850C04B3ABF54132565044B0B7D7BFD8BA270B39432355FFB4,
    Gx=0xB70E0CBD6BB4BF7F321390B94A03C1D356C21122343280D6115C1D21,
    Gy=0xBD376388B5F723FB4C22DFE6CD4375A05A07476444D5819985007E34,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF16A2E0B8F03E13DD29455C5C2A3D
  ),
  'secp256k1': _ECData(
    p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1,
    a=0, b=7,
    Gx=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    Gy=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
  ),
  'secp256r1': _ECData(
    p=2**224 * (2**32 - 1) + 2**192 + 2**96 - 1,
    a=0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC,
    b=0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B,
    Gx=0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
    Gy=0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5,
    n=0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
  ),
  'secp384r1': _ECData(
    p=2**384 - 2**128 - 2**96 + 2**32 - 1,
    a=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFF0000000000000000FFFFFFFC,
    b=0xB3312FA7E23EE7E4988E056BE3F82D19181D9C6EFE8141120314088F5013875AC656398D8A2ED19D2A85C8EDD3EC2AEF,
    Gx=0xAA87CA22BE8B05378EB1C71EF320AD746E1D3B628BA79B9859F741E082542A385502F25DBF55296C3A545E3872760AB7,
    Gy=0x3617DE4A96262C6F5D9E98BF9292DC29F8F41DBD289A147CE9DA3113B5F0B8C00A60B1CE1D7E819D7A431D7C90EA0E5F,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC7634D81F4372DDF581A0DB248B0A77AECEC196ACCC52973
  ),
  'secp521r1': _ECData(
    p=2**521-1,
    a=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC,
    b=0x0051953EB9618E1C9A1F929A21A0B68540EEA2DA725B99B315F3B8B489918EF109E156193951EC7E937B1652C0BD3BB1BF073573DF883D2C34F1EF451FD46B503F00,
    Gx=0x00C6858E06B70404E9CD9E3ECB662395B4429C648139053FB521F828AF606B4D3DBAA14B5E77EFE75928FE1DC127A2FFA8DE3348B3C1856A429BF97E7E31C2E5BD66,
    Gy=0x011839296A789A3BC0045C8A5FB42C7D1BD998F54449579B446817AFBD17273E662C97EE72995EF42640C550B9013FAD0761353C7086A272C24088BE94769FD16650,
    n=0x01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA51868783BF2F966B7FCC0148F709A5D03BB5C9B8899C47AEBB6FB71E91386409
  )
}

def EllipticCurveRepository(name):
  '''
  Elliptic Curve Repository - standard curves repository function
  Args:
    name: name of the curve (e.g. 'secp256k1') case insensitive
  Return: Tuple (F, E, G, n)
    F: Base field object of E
    E: Elliptic curve corresponding to `name`
    G: Base point given by `name`
    n: Order of `G`
  '''
  from ecpy.fields import FiniteField
  from .EllipticCurve import EllipticCurve
  name = name.lower()
  if name in _repo.keys():
    data = _repo[name]
    F = FiniteField(data.p)
    E = EllipticCurve(F, data.a, data.b)
    G = E(data.Gx, data.Gy)
    n = data.n
    return (F, E, G, n)
  else:
    raise ValueError('Invalid Elliptic Curve Name: %r' % name)


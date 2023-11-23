import hashlib
import unittest
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve.pairing import gen_prime_mod_four
from ecpy.elliptic_curve import EllipticCurve


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_field(self):
        p = int("501794446334189957604282155189438160845433783392772743395579628617109"
                "929160215221425142482928909270259580854362463493326988807453595748573"
                "76419559953437557")
        F = ExtendedFiniteField(p, "x^2+x+1")
        print("F.t: ", F.t)
        print("F.p: ", F.p)
        print("F.n: ", F.n)
        print("order: ", F.order())
        E = EllipticCurve(F, 0, 1)
        print(E)
        print(E.field)
        print("random")
        r = E.random_point()
        print("")
        print(r)
        print(E.get_corresponding_y(7))
        self.assertEqual(True, True)  # add assertion here

    def test_what_happens_when_hash(self):
        m = 'iamIDstring'
        hash_ = hashlib.sha256(str(m).encode("utf-8")).hexdigest()
        ee = int(hash_, 16)  # 16 because in Hex base
        print(hash_)  # is hex encoded string
        print(ee)  # is an integer
        # TODO what happens when we do ee*P ? Is that then a group element?
        p = int("501794446334189957604282155189438160845433783392772743395579628617109"
                "929160215221425142482928909270259580854362463493326988807453595748573"
                "76419559953437557")
        F = ExtendedFiniteField(p, "x^2+x+1")
        E = EllipticCurve(F, 0, 1)
        P = E(3, int("1418077311270457886139292292020587683642898636677353664354101171"
                     "7684401801069777797699258667061922178009879315047772033936311133"
                     "535564812495329881887557081"))
        print(ee * P)
        self.assertEqual(True, True)  # add assertion here

    def test_what_happens_with_eliptic(self):
        p = gen_prime_mod_four(14)
        print(p)

#  TODO find out what this does on input H(E.field(symmetric_tate_pairing(E, sP, pubkey, l) ** r))) = H2(g_id^r)
#  TODO find out what E.field(symmetric_tate_pairing(E, sP, pubkey, l) ** r)) is of type
def H(x):
    return x.x * x.field.p + x.y


if __name__ == '__main__':
    unittest.main()

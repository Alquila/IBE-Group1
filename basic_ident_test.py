import hashlib
import unittest
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve.pairing import gen_prime_mod_four
from ecpy.elliptic_curve import EllipticCurve


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_field(self):
        #23
        #p = gen_prime_mod_four(10)
        p = int("501794446334189957604282155189438160845433783392772743395579628617109"
                "929160215221425142482928909270259580854362463493326988807453595748573"
                "76419559953437557")
        # print("p: ", p)
        # print("l", l)
        F = ExtendedFiniteField(p, "x^2+x+1")
        print("F.t: ", F.t)
        print("F.p: ", F.p)
        print("F.n: ", F.n)
        print("order: ", F.order())
        E = EllipticCurve(F, 0,1)
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
        self.assertEqual(True, True)  # add assertion here

    def test_what_happens_with_eliptic(self):
        p = gen_prime_mod_four(14)
        print(p)



if __name__ == '__main__':
    unittest.main()

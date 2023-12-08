import hashlib
import random
import unittest
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve.pairing import gen_prime_mod_four, symmetric_weil_pairing, symmetric_tate_pairing
from ecpy.elliptic_curve import EllipticCurve
from basic_ident import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        i = 6
        j = 3
        print(i ^ j)
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
        hash_id = int(hash_, 16)  # 16 because in Hex base
        print(hash_)  # is hex encoded string
        print(hash_id)  # is an integer
        # TODO what happens when we do ee*P ? Is that then a group element?
        p = int("501794446334189957604282155189438160845433783392772743395579628617109"
                "929160215221425142482928909270259580854362463493326988807453595748573"
                "76419559953437557")
        F = ExtendedFiniteField(p, "x^2+x+1")
        E = EllipticCurve(F, 0, 1)
        P = E(3, int("1418077311270457886139292292020587683642898636677353664354101171"
                     "7684401801069777797699258667061922178009879315047772033936311133"
                     "535564812495329881887557081"))
        q_id = hash_id * P  # is a point on the elliptic curve
        # print(eep)
        l = (p + 1) // 6
        s = random.randint(1, p - 1)
        P_pub = s * P
        # print("groups")
        # print(sp.group)  # in elliptic curve
        # print(qid.group) # in elliptic curve

        e_qid_ppub = symmetric_weil_pairing(E, P_pub, q_id, l)
        print("e(qid,ppub)")
        print(e_qid_ppub)
        print(type(e_qid_ppub))
        print("e(ppub,qid)")
        e_ppub_qid = symmetric_weil_pairing(E, q_id, P_pub, l)
        print(e_ppub_qid)

        g_id = e_qid_ppub  # is an integer

        print("E.field")
        efield = E.field(e_qid_ppub)
        print(efield)  # seems to be the same as e_qid_sp

        r = random.randint(1, p - 1)
        g_id_r_field = E.field(g_id ** r)
        g_id_r = g_id ** r
        print("raising to r")
        print(e_qid_ppub ** r)
        # print(g_id_r_field)
        # print()

        # extract d_id
        s_qid = s * q_id
        d_id = s_qid

        # decryption U
        rP = r * P
        # e(d_id, U) in decrypt
        e_did_u = symmetric_weil_pairing(E, d_id, rP, l)
        print("compare")
        print("e(d_id, U)", e_did_u)
        print("g_id^r", g_id_r_field)

        # compare other way around
        e_u_did = symmetric_weil_pairing(E, rP, d_id, l)
        e_ppub_qid_r = e_ppub_qid ** r
        print("e(U,d_id)", e_u_did)
        print("e(P_pub, Q_id)^r)", e_ppub_qid_r)
        hmm = H(E.field(e_u_did))
        print(hmm)  # this is now an integer
        self.assertEqual(True, True)  # add assertion here

    def test_what_happens_with_eliptic(self):
        p = gen_prime_mod_four(14)
        print(p)

    def test_stuff(self):
        message = 1122023
        q, F, E, P, s, P_pub, order = setup()
        id_ = "bob.email"

        d_id = extract(P, id_, s)
        u, v = encrypt(E, P, message, id_, P_pub, q, order)

        d = decrypt(E, u, v, d_id, order)

        print("encrypted message: \n" + str(message) + "\n")
        print("decrypted message: \n" + str(d)+ "\n")

        self.assertEqual(message, d)

    def test_basic_indent(self):
        message_strings = ["does it work", "this is a longer string as I dont know how long they can be",
                           'lol', "PlEasE woRK"]
        message_int = [123456789, 1989, 42, 666, 8965432797543467899076543234567893456789345678934567]

        for message in message_strings:
            print("encrypted message: \n" + message)
            basic_ident(message)

        for i in message_int:
            print("encrypted message: \n" + str(i))
            basic_ident(i)

            self.assertEqual(i, i)


#  TODO find out what this does on input H(E.field(symmetric_tate_pairing(E, sP, pubkey, l) ** r))) = H2(g_id^r)
#  TODO find out what E.field(symmetric_tate_pairing(E, sP, pubkey, l) ** r)) is of type
def H(x):
    return x.x * x.field.p + x.y


if __name__ == '__main__':
    unittest.main()

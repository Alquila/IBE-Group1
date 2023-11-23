from ecpy.elliptic_curve.pairing import gen_supersingular_ec, symmetric_weil_pairing
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve import EllipticCurve
import hashlib
import random


def bdh_parameter_generator():
    q = int("501794446334189957604282155189438160845433783392772743395579628617109"
            "929160215221425142482928909270259580854362463493326988807453595748573"
            "76419559953437557")
    F = ExtendedFiniteField(q, "x^2+x+1")
    E = EllipticCurve(F, 0, 1)
    P = E(3, int("1418077311270457886139292292020587683642898636677353664354101171"
                 "7684401801069777797699258667061922178009879315047772033936311133"
                 "535564812495329881887557081"))

    s = int("129862491850266001914601437161941818413833907050695770313188660767"
            "152646233571458109764766382285470424230719843324368007925375351295"
            "39576510740045312772012")
    sP = E(s,
           int("452543250979361708074026409576755302296698208397782707067096515523"
               "033579018123253402743775747767548650767928190884624134827869137911"
               "24188897792458334596297"))


def setup(k):
    E, F, l = gen_supersingular_ec(k)


# Eliptic curve E, points P,Q, m order of P,Q
def useWeil(E, P, Q, m):
    aa = symmetric_weil_pairing(E, P, Q, m)


def h1(id, P):
    """
    Send element to G_1^*
    Args:
        id: element in {0,1}^*
        P: Generator for G_1
    Returns: element in G_1^*
    """
    hash = hashlib.sha256(str(id).encode("utf-8")).hexdigest()
    # hash = hashlib.sha256(id).hexdigest().encode("hex")
    ee = int(hash, 16)
    # TODO send to group
    return hash


def h2(g_id_r):
    """
    Sends element from G_2^* to {0,1}^n for some n
    Args:
        g_id_r: element in G_2^*
    Returns: element in {0,1}^n
    """
    #  TODO send from group to {0,1}^n
    return g_id_r


def encrypt(E, P, m, id, P_pub, q, order):
    """
    Encrypt the message m
    Args:
        E: The Elliptic curve
        P: The generator
        m: the message
        id: The ID of the receiver
        P_pub: The public something
        q: The prime order of G_1 G_2
        order: The order of something ??

    Returns: Encryption of the form (U,V) in G_1^* x {0,1}^n

    """
    # Q_id = H1(id) \in G_1^*
    Q_id = h1(id)
    # choose random r \in Z_q^*
    r = random.randint(1, q)
    # Compute g_id = e(Q_id, P_pub) \in G_2^*
    g_id = symmetric_weil_pairing(E, Q_id, P_pub, q)  # TODO is order of G_1 G_2 q or order=(q+1)/6
    # Compute g_id ^ r
    g_id_r = g_id ** r
    # Compute H2(g_id^r) \in {0,1}^n
    h2_ = h2(g_id_r)
    return r * P, m ^ h2_


def decrypt(E, c, secret_key_d_id, order):
    """
    Decrypt the ciphertext
    Args:
        E: The Elliptic curve
        c: Ciphertext (U,V)
        secret_key_d_id: d_ID = s*H_1(ID)
        order: order of the prime ?

    Returns: the encrypted msg m

    """
    u, v = c

    e_d_u = symmetric_weil_pairing(E, secret_key_d_id, u, order)  # e(d_id, U) element in G_2^*

    h2_ = h2(e_d_u)  # element in {0,1}^n

    return v ^ h2_  # m


def extract(id, s):
    """"
    Given string ID in {0,1}^*, compute Q_ID = H_1(ID) in G_1^* and set private key d_id to be s*Q_ID
    """
    q_id = h1(id)  # in G_1^*
    return s * q_id  # d_ID

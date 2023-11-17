from ecpy.elliptic_curve.pairing import gen_supersingular_ec, symmetric_weil_pairing
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve import EllipticCurve
import hashlib
import random


def bfh_parameter_generator(k):
    # Should output (q, G1, G2, ê)
    print(42)


prim = 5
order = -42
F = ExtendedFiniteField(prim)
E = EllipticCurve(F)
P = E.random_point()


def setup(k):
    E, F, l = gen_supersingular_ec(k)


# Eliptic curve E, points P,Q, m order of P,Q
def useWeil(E, P, Q, m):
    aa = symmetric_weil_pairing(E, P, Q, m)


def h1(id):
    """
    Send element to G_1^*
    Args:
        id: element in {0,1}^*
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


def encrypt(m, id, P_pub):
    # choose random r \in Z_q^*
    r = random.randint(1, prim)
    # Q_id = H1(id) \in G_1^*
    Q_id = h1(id)
    # Compute g_id = e(Q_id, P_pub) \in G_2^*
    g_id = symmetric_weil_pairing(E, Q_id, P_pub, order)
    # Compute g_id ^ r
    g_id_r = g_id ** r
    # Compute H2(g_id^r) \in {0,1}^n
    h2_ = h2(g_id_r)
    return r * P, m ^ h2_


def decrypt(c, secret_key):
    u, v = c

    e_d_u = symmetric_weil_pairing(E, secret_key, u, order)  # element in G_2^*

    h2_ = h2(e_d_u)  # element in {0,1}^n

    return v ^ h2_  # m


def extract(id, s):
    q_id = h1(id)  # in G_2^*
    return s*q_id

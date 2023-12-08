from ecpy.elliptic_curve.pairing import gen_supersingular_ec, symmetric_weil_pairing
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve import EllipticCurve
import hashlib
import secrets


def setup():
    """
    Generate BDH parameters

    Returns: prime q, F, E, random generator P, master-key s, P_pub (sP), order
    """
    # The prime q:
    q = int("501794446334189957604282155189438160845433783392772743395579628617109"
            "929160215221425142482928909270259580854362463493326988807453595748573"
            "76419559953437557")

    # The Finite Field (G2) and EllipticCurve (G1) #TODO Understand
    F = ExtendedFiniteField(q, "x^2+x+1")
    E = EllipticCurve(F, 0, 1)

    # a point of order q
    P = E(3, int("1418077311270457886139292292020587683642898636677353664354101171"
                 "7684401801069777797699258667061922178009879315047772033936311133"
                 "535564812495329881887557081"))

    # Random s in Z_q^*
    s = secrets.randbelow(q)
    # P_pub = sP
    P_pub = s * P

    # Order of points
    order = (q + 1) // 6
    return q, F, E, P, s, P_pub, order


def H1(id_, P):
    """
    Send element to G_1^*
    Args:
        id_: element in {0,1}^*
        P: Generator for G_1
    Returns: point on curve / element in G_1^*
    """
    hash_ = hashlib.sha256(str(id_).encode("utf-8")).hexdigest()
    hash_as_int = int(hash_, 16)
    return hash_as_int * P


# Taken from ecpy library
def H2(g_id_r):
    """
    Sends element from G_2^* to {0,1}^n for some n
    hash coordinates
    Args:
        g_id_r: element in G_2^*
    Returns: element in {0,1}^n
    """
    xy = g_id_r.x + g_id_r.y
    hash_ = hashlib.sha256(str(xy).encode("utf-8")).hexdigest()
    return int(hash_, 16)


# TODO extract g_ID instead of computing everytime
def encrypt(E, P, m, id, P_pub, q, order):
    """
    Encrypt the message m
    Args:
        E: The Elliptic curve
        P: The generator of G_1
        m: the message
        id: The ID of the receiver
        P_pub: The public something
        q: The prime order of G_1 G_2
        order: The order of something

    Returns: Encryption of the form (U,V) in G_1^* x {0,1}^n

    """
    # Q_id = H1(id) \in G_1^*
    Q_id = H1(id, P)
    # choose random r \in Z_q^*
    r = secrets.randbelow(q)
    # Compute g_id = ê(Q_id, P_pub) \in G_2^*
    g_id = symmetric_weil_pairing(E, Q_id, P_pub, order)  # TODO is order of G_1 G_2 q or order=(q+1)/6
    # Compute g_id ^ r
    g_id_r = g_id ** r
    # Compute H2(g_id^r) \in {0,1}^n
    h2_ = H2(g_id_r)
    return r * P, m ^ h2_


def decrypt(E, u, v, secret_key_d_id, order):
    """
    Decrypt the ciphertext
    Args:
        E: The Elliptic curve
        c: Ciphertext (U,V)
        secret_key_d_id: d_ID = s*H_1(ID)
        order: order of the points U and d_ID

    Returns: the encrypted msg m

    """

    e_d_u = symmetric_weil_pairing(E, secret_key_d_id, u, order)  # e(d_id, U) element in G_2^*

    h2_ = H2(E.field(e_d_u))  # element in {0,1}^n

    return v ^ h2_  # m


def extract(P, id_, s):
    """"
    Given string ID in {0,1}^*, compute Q_ID = H_1(ID) in G_1^* and set private key d_id to be s*Q_ID
    """
    q_id = H1(id_, P)  # in G_1^*
    return s * q_id  # d_ID


def basic_ident(message):
    q, F, E, P, s, P_pub, order = setup()
    id = "bob.email"
    is_string = False
    if isinstance(message, str):
        is_string = True
        m_to_bytes = message.encode('utf-8')
        message = int.from_bytes(m_to_bytes, 'little')

    d_id = extract(P, id, s)
    u, v = encrypt(E, P, message, id, P_pub, q, order)

    d = decrypt(E, u, v, d_id, order)

    if is_string:
        d_to_bytes = d.to_bytes((d.bit_length() + 7) // 8, 'little')
        d = d_to_bytes.decode('utf-8')

    print("decrypted message: \n" + str(d))


#message = "does the work if yes why"
#basic_ident(message)

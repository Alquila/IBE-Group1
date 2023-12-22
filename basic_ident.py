from ecpy.elliptic_curve.pairing import find_point_by_order, gen_supersingular_ec, symmetric_weil_pairing
from ecpy.fields import ExtendedFiniteField
from ecpy.elliptic_curve import EllipticCurve
import hashlib
import secrets


def setup():
    """
    Generate BDH parameters

    Returns: prime p, F, E, random generator P, master-key s, P_pub (sP), order
    """
    # The prime q:    
    p = int("40838243888440222194513047318433462181794082107565421749840580958183723553113450391291240027817728253892367020955719075895074492916387884536971247198768837")

    # The Finite Field and EllipticCurve
    F = ExtendedFiniteField(p, "x^2+x+1")
    E = EllipticCurve(F, 0, 1)

    # Order of points
    order = (p + 1) // 6

    # a point of order q
    P = find_point_by_order(E, order)
    
    # Random s in Z_q^*
    s = secrets.randbelow(order-1)+1
    
    # P_pub = sP
    P_pub = s * P
    return p, F, E, P, s, P_pub, order


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


def H2(g_id_r):
    """
    Sends element from G_2^* to {0,1}^n for some n
    hash coordinates
    Args:
        g_id_r: element in G_2^*
    Returns: element in {0,1}^n
    """
    xy = g_id_r.x * g_id_r.field.p + g_id_r.y
    hash_ = hashlib.sha256(str(xy).encode("utf-8")).hexdigest()
    return int(hash_, 16)

def extract(P, id_, s):
    """"
    Given string ID in {0,1}^*, compute Q_ID = H_1(ID) in G_1^* and set private key d_id to be s*Q_ID
    """
    q_id = H1(id_, P)  # in G_1^*
    return s * q_id  # d_ID

def encrypt(E, P, m, id, P_pub, order):
    """
    Encrypt the message m
    Args:
        E: The Elliptic curve
        P: The generator of G_1
        m: the message
        id: The ID of the receiver
        P_pub: The public key TODO: public wtf??¿¿
        order: The order of P, Q

    Returns: Encryption of the form (U,V) in G_1^* x {0,1}^n

    """
    # Q_id = H1(id) \in G_1^*
    Q_id = H1(id, P)
    # choose random r \in Z_q^*
    r = secrets.randbelow(order)
    # Compute g_id = ê(Q_id, P_pub) \in G_2^*
    g_id = symmetric_weil_pairing(E, Q_id, P_pub, order)
    # Compute g_id ^ r
    g_id_r = E.field(g_id) ** r
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


def basic_ident(message):
    p, F, E, P, s, P_pub, order = setup()
    id_ = "pub@company.com"
    is_string = False
    if isinstance(message, str):
        is_string = True
        m_to_bytes = message.encode('utf-8')
        message = int.from_bytes(m_to_bytes, 'little')

    u, v = encrypt(E, P, message, id_, P_pub, order)

    d_id = extract(P, id_, s)
    d = decrypt(E, u, v, d_id, order)

    if is_string:
        d_to_bytes = d.to_bytes((d.bit_length() + 7) // 8, 'little')
        d = d_to_bytes.decode('utf-8')

    print("decrypted message: \n" + str(d))
    return d

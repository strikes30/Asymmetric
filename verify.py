from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key_pub = ECC.import_key(open('student_py_ecc_pub.key', 'rt').read())
message = open('secret.txt', 'rb').read()
signature = open('signature.bin', 'rb').read()
h = SHA256.new(message)
verifier = DSS.new(key_pub, 'fips-186-3')
try:
    verifier.verify(h, signature)
    print("Signature is valid")
except (ValueError, TypeError):
    print("Signature is NOT valid")

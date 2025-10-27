from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC

key = ECC.import_key(open('student_py_ecc.key', 'rt').read()) # chiave ECC
message = open('secret.txt', 'rb').read()
h = SHA256.new(message)
signature = DSS.new(key, 'fips-186-3').sign(h)

with open('signature.bin', 'wb') as f:
    f.write(signature)
print("Signature saved as signature.bin")

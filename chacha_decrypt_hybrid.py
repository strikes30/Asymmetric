import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, ChaCha20

if len(sys.argv) < 4:
    print("Usage: python3 hybrid_decrypt_file_chacha20.py <input> <priv_key_pem> <output>")
    sys.exit(1)

inp, privkey_path, outp = sys.argv[1], sys.argv[2], sys.argv[3]

rsa_key = RSA.import_key(open(privkey_path, 'rb').read())
with open(inp, 'rb') as f:
    nonce = f.read(8)          # ChaCha20 nonce è 8 byte
    enc_chacha_key = f.read(256)  # 2048-bit RSA -> 256 bytes
    ciphertext = f.read()

cipher_rsa = PKCS1_OAEP.new(rsa_key)
chacha_key = cipher_rsa.decrypt(enc_chacha_key)

cipher_chacha = ChaCha20.new(key=chacha_key, nonce=nonce)
data = cipher_chacha.decrypt(ciphertext)

with open(outp, 'wb') as f:
    f.write(data)
print("Wrote:", outp)

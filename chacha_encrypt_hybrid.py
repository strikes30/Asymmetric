import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, ChaCha20
from Crypto.Random import get_random_bytes

if len(sys.argv) < 4:
    print("Usage: python3 hybrid_encrypt_file_chacha20.py <input> <pub_key_pem> <output>")
    sys.exit(1)

inp, pubkey_path, outp = sys.argv[1], sys.argv[2], sys.argv[3]

data = open(inp, 'rb').read()
rsa_key = RSA.import_key(open(pubkey_path, 'rb').read())

chacha_key = get_random_bytes(32)   # 256-bit ChaCha20 key
chacha_nonce = get_random_bytes(8)  # ChaCha20 nonce (8 bytes)
cipher_chacha = ChaCha20.new(key=chacha_key, nonce=chacha_nonce)
ciphertext = cipher_chacha.encrypt(data)

cipher_rsa = PKCS1_OAEP.new(rsa_key)
enc_chacha_key = cipher_rsa.encrypt(chacha_key)

with open(outp, 'wb') as f:
    for x in (chacha_nonce, enc_chacha_key, ciphertext):
        f.write(x)
print("Wrote:", outp)

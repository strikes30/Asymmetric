import sys
import json
from Crypto.PublicKey import ECC

k = ECC.import_key(open(sys.argv[1], 'rb').read())
b = lambda x: x.bit_length()
d = {
    'curve': k.curve,
    'point_x_bits': b(int(k.pointQ.x)),
    'point_y_bits': b(int(k.pointQ.y))
}
if k.has_private():
    d['d_bits'] = b(int(k.d))

print(json.dumps(d, indent=2))

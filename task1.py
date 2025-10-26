import sys
import json
from Crypto.PublicKey import ECC

k = ECC.import_key(open(sys.argv[1], 'rb').read())
d = {
  'curve': k.curve,
  'point_x': int(k.pointQ.x),
  'point_y': int(k.pointQ.y)
}
if k.has_private():
  d['d'] = int(k.d)

print(json.dumps(d, indent=2))

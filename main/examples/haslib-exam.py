import hashlib
import json

string1 = "abc"
string2 = "ab"

"""
hash_sha256 = hashlib.sha256(string1.encode())
print("abc hashed sha-256",hash_sha256.hexdigest())
hash2_sha256 = hashlib.sha256(string2.encode())
print("ab hashed sha-256",hash2_sha256.hexdigest())"""

obj1 = {
      "index": 1,
      "timestamp": 1506057125.900785,
      "transactions": [
            {
                  "sender": "8527147fe1f5426f9dd545de4b27ee00",
                  "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
                  "amount": 5
            }
      ],
      "proof": 324984774000,
      "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
obj2 = {
      "index": 2, # this changed
      "timestamp": 1506057126.000005, #this changed
      "transactions": [
            {
                  "sender": "8527147fe1f5426f9dd545de4b27ee00",
                  "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
                  "amount": 50 #this changed
            }
      ],
      "proof": 324984774000,
      "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
block_string_obj1 = json.dumps(obj1).encode()
hash_sha256 = hashlib.sha256(block_string_obj1)
print("object1 hashed sha-256",hash_sha256.hexdigest())
block_string_obj2 = json.dumps(obj2).encode()
hash2_sha256 = hashlib.sha256(block_string_obj2)
print("object2 hashed sha-256",hash2_sha256.hexdigest())
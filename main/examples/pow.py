"""
Let’s decide that the hash of some integer x multiplied by another y 
must end in 0. So, hash(x * y) = ac23dc...0. And for this simplified 
example, let’s fix x = 5. Implementing this in Python:
"""

from hashlib import sha1, sha256

x = 5
y = 0

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y+=1
    print(y)
print(f'The solution is y= {y}')


#Integrity_Checker
#With buffer

import hashlib 
import sys

#Buffer size can be anything. This reads in
#64 kb chunks

buffer_size = 65546
filename = sys.argv[1]
filehash = hashlib.sha256()
md5hash = hashlib.md5()

with open(filename, 'rb') as ff:
    fileb = ff.read(buffer_size)
    while len(fileb) > 0:
        filehash.update(fileb)
        md5hash.update(fileb)
        fileb  = ff.read(buffer_size)


print("Results Below:")
print("SHA256: " + filehash.hexdigest())
print("md5: " + md5hash.hexdigest())

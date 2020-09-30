#Integrity_Checker v.2
#With buffer

import hashlib 
import sys
#from argparse import ArgumentParser (not used yet)


def hashpump(): 
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

    #MD5 VAR
    md5_save    = filehash.hexdigest()
    sha256_save = md5hash.hexdigest()
    return sha256_save, md5_save




def hashcompare(hash_save):
    #print(hash_save)
    #compares the hash of a file and a provided has

    md5_save = hash_save[0]
    sha256_save = hash_save[1]   
    secondhash = sys.argv[2]

    if sha256_save == secondhash:
        print("sha256 MATCH: \n%s\n%s" % (sha256_save, secondhash))

    elif md5_save == secondhash:
        print("md5 MATCH: \n%s\n%s" % (md5_save, secondhash))
        
    else:
        print("Not a match")
            
    

def main():
    #prs = ArgumentParser()
    #prs.add_argument("-h", "--help", help="Help me please.")
    
    if len(sys.argv) == 1:
        print("python3 IntegrityCheck [filename] [hash (md5 or sha256)]")
        exit(0)
        
    elif len(sys.argv) == 2:
        hashpump()

    elif len(sys.argv) == 3:
        hash_save = hashpump()
        hashcompare(hash_save)
        
    else:
        print("Program broke.")
        exit(1)

main()

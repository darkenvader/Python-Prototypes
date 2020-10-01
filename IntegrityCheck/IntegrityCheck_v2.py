#Integrity_Checker v.2.1
#With buffer

import hashlib 
import sys
from argparse import ArgumentParser

version = 2.1

def hashpump(filename): 
    #Buffer size can be anything. This reads in
    #64 kb chunks

    buffer_size = 65546
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

def compare_sha256(sha256_save, hash_save):
    #compares the hash of a file and a provided has

    sha256_file = hash_save[1]   
    
    if sha256_save == sha256_file:
        print("sha256 MATCH: \n%s\n%s" % (sha256_file, sha256_save))
        
    else:
        print("sha256 not a match")

def compare_md5(md5_save, hash_save):
    #compares the hash of a file and a provided has

    md5_file = hash_save[0]  

    if md5_save == md5_file:
        print("md5 MATCH: \n%s\n%s" % (md5_file, md5_save))
        
    else:
        print("md5 not a match")
        
#This runs first        
def main():
    
    parse = ArgumentParser(description='IntegrityCheck\nhttps://github.com/elyseefranchuk', epilog='Example: IntegrityCheck_v2.py -f app.exe --sha256 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 ')
    parse.add_argument("--sha256", help="Compare hash to sha256")
    
    parse.add_argument("--md5", help="Compare hash to md5")

    parse.add_argument("-f", "--filename", help="File to be fingerprinted", required=True)
    args = parse.parse_args()

    
    #If no arguments are passed, this message will be summoned
    if len(sys.argv) == 1:
        parse.print_help()
        exit(0)
        
    if args.filename:
        filename = args.filename
        hash_save = hashpump(filename)

        if args.sha256:
            sha256_save = args.sha256
            compare_sha256(sha256_save, hash_save)
        
        if args.md5:
            md5_save = args.md5
            compare_md5(md5_save, hash_save)
                                  
    else:
        print("Program broke.")
        exit(1)
    

main()


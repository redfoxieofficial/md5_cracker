import hashlib

md5 = input("Kırılacak MD5: ")
wordlist = input("Wordlist giriniz: ")


dosya = open(wordlist,"r",encoding="utf-8")
oku = dosya.read()

for i in oku:
    hashli_i = hashlib.md5(i.encode('utf-8')).hexdigest()

    if hashli_i == md5:
        print(md5+":"+i)



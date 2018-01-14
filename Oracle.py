import random
rng=random.Random()

def to_dec(num,n):
    num=list(str(num))
    if n<=10:
        for ch in num:
            if not '0'<=ch<=str(n-1):
                return -1
    else:
        for ch in num:
            if ch>="A":
                if not ord(ch)<ord('A')+n-10:
                    return -1
    for i in range(len(num)):
        if '0'<=num[i]<='9':
            num[i]=int(num[i])
        elif num[i]==' ':
            num[i]=rng.randrange(0,10)
        elif 'A'<=num[i]<='Z':
            num[i]=10+ord(num[i])-ord('A')
    dec=0
    for i in range(len(num)):
        dec+=n**i*num.pop()
    return dec
def to_n(num=0,n=2):
    nth=""
    while num != 0:
        rem = num % n
        if rem <= 9:
            nth = str(rem) + nth
        elif rem<=35:
            nth = chr(rem - 10 + ord("A")) + nth
        else:
            nth='?'+nth
        num //= n
    return nth

def encrypt(text="",key=36):
    text=text.upper()
    return to_dec(text,key)
def decrypt(code,key=36):
    text=to_n(code,key)
    for i in range(10):
        text=text.replace(str(i)," ")
    return text.lower()


print("Hi, I'm Oracle.")

while True:
    mode = input("How can I help you?\n")
    if mode=="goodbye":
        print("Goodbye.")
        break
    if mode!="code" and mode!="base" and mode!="help":
        mode=input("You can choose from base or code or help.\n")
    if mode!="code" and mode!="base" and mode!="help":
        print("Goodbye.")
        break
    if mode=="code":
        mode=input("Encrypt or decrypt?\n")
        if mode=="encrypt":
            while True:
                text=input("Tell me your text.\n")
                if text.replace(' ','').isalpha():
                    break
                else:
                    print("Text should only contain alphabets and space.")
            while True:
                key=int(input("What's your key?\n"))
                code=encrypt(text,key)
                if code==-1:
                    print("Can't encrypt with this key. >=36 is recommended.")
                else:
                    print("The code is:",code)
                    break
            pt=input("Save it to a file?\n")
            if pt=='y' or pt=="yes":
                fname=input("Name the file.\n")
                f=open(fname+".txt",'w')
                f.write(str(code))
                f.close()
                print("It's been saved to {}.txt".format(fname))
            else:
                pass
        if mode=="decrypt":
            pt=input("Tell me your code or filename.\n")
            if pt.isdigit():
                code=int(pt)
            else:
                f=open(pt+".txt",'r')
                code=int(f.readline())
                f.close()
            key=int(input("What's your key?\n"))
            text=decrypt(code,key)
            print("The text is:",text)
    elif mode=="base":
        num=input("Tell me the number you want to convert.\n")
        n1=int(input("It's in what base?\n"))
        n2=int(input("Your target base?\n"))
        res=to_n(to_dec(num,n1),n2)
        print("{}({}) = {}({})".format(num,n1,res,n2))
        if '?' in res:
            print("It can't be expressed with only numbers and alphabets")
            print("The additional part is shown with a ?")
    elif mode=="help":
        print("'base' is to convert numbers between different bases.")
        print("'code' is to encrypt and decrypt some words with a key")





import random


global charset
#charset=[str(i) for i in range(10)]+[',']+[chr(i) for i in range(ord('A'),ord('A')+26)]+['.']+[chr(i) for i in range(ord('a'),ord('a')+26)]+['?']
charset='0123456789abcdefghijklmnopqrstuvwxyz,ABCDEF.XYZ?'
#len=48

def binTo32(bin=''):
    nth=''
    while len(bin)!=0:
        temp=bin[-5:]
        bin=bin[:-5]
        nth=charset[int(temp,2)]+nth
    return nth

def randkey():
    rng=random.Random()
    out=[]
    for i in range(6):
        while True:
            j=rng.randrange(0,48)
            if j not in out:
                out.append(j)
                break
    out.sort(reverse=True)
    key=''
    keychar=''
    for i in range(48):
        if i not in out:
            key+='1'
            keychar+=charset[i]
        else:
            key+='0'
    key=binTo32(key)
    key='{:0>10}'.format(key)
    return key,keychar

def getkeychar(key):
    bins=''
    for i in key:
        unit=bin(charset.index(i))[2:]
        bins+='{:0>5}'.format(unit)
    bins=bins[-48:]
    keychar=''
    for i in range(48):
        if bins[i]=='1':
            keychar+=charset[i]
    return keychar
#decTo42
def encrypt(nums, key):
    text=""
    keychar=getkeychar(key)
    for num in nums:
        if num==0:
            text+=keychar[0]*3
        else:
            temp=''
            while num != 0:
                rem = num % 42
                temp= keychar[rem] + temp
                num //= 42
            temp=keychar[0]*(3-len(temp))+temp
            text+=temp
    text+=key
    return text
def decrypt(text):
    key=text[-10:]
    keychar=getkeychar(key)
    nums=[]
    for i in range((len(text)-10)//3):
        sub=text[3*i:3*(i+1)]
        num=keychar.index(sub[0])*42*42+keychar.index(sub[1])*42+keychar.index(sub[2])
        nums.append(num)
    return ''.join([chr(num) for num in nums])
def main():
    print('Secured Chat v1.0')
    print("Instructions:")
    print("To encrypt, input 'i' and <your text>")
    print("To decrypt, input the text directly")
    while True:
        s=input(':')
        if s=='':
            break
        elif s[0]=='i':
            s=s[1:]
            nums=[]
            for ch in s:
                nums.append(ord(ch))
            mykey,mykeychar=randkey()
            msg=encrypt(nums, mykey)
            print(msg)
        else:
            text=decrypt(s)
            print(text)
main()

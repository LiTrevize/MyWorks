import time

def generate_prm_txt(filename,max):
    f=open(filename,"w")
    f.write("2\n3\n")
    n=3
    while n<=max:
        n+=2
        f=open(filename, "r")
        while True:
            read_n=f.readline()
            if len(read_n)==0:
                f=open(filename,"a")
                f.write(str(n)+"\n")
                break
            if n%int(read_n)==0:
                break
        f.close

t0=time.clock()
generate_prm_txt("prime.txt",10000)
t1=time.clock()
print(t1-t0)
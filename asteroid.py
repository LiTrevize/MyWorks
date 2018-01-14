def name(year,month,date,seq):
    ch1=chr(ord('A')+2*(month-1)+date//16)
    ch2=chr(ord('A')+seq%25)
    return str(year)+ch1+ch2+str(seq//25)

print(name(2017,1,30,1745))

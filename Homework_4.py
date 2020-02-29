#1 song creation
def song_creation (a=3, b=3, c=0):
    s1="la"
    d=(s1+'-')*(b-1) + s1
    z = (d + '\n')*(a-1)
    #s2=s1*b
    #b = '-'.join(s2.split())
    if c==0:
        return z+d+'!'
    else:
        return z+d+'.'
s = song_creation (3,2,1)
print(s)

#2
def my_func (*args):
    l=list(args)
    l.sort()
    return l[1]
y = my_func(1,20,300,52,19,20,52)
print(y)

#3 clean text from digits and symbols

from string import ascii_letters, whitespace
def clean(text):
   good_chars = (ascii_letters + whitespace).encode()
   junk_chars = bytearray(set(range(0x100)) - set(good_chars))
   return text.encode('ascii', 'ignore').translate(None, junk_chars).decode()
c=clean("454trgfgdf&&&")
#print(c)



a=('a','b','c')
b=list(a)
b[1]='d'
a=b
print(b)

print(end="\n")

aa=('a','b','c')
bb=list(aa)
bb.append('d')
aa=bb
print(bb)

print(end="\n")

aaa=('a','b','c')
bbb=('d',)
aaa+=bbb
print(aaa)
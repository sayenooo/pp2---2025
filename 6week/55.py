f = open("input.txt","w")
aa = ["jkewf","hew","uie"]
f.write(' ,'.join(aa))
f.close()
f = open("input.txt","r")
a = f.read()
print(a)
dig,loww,upp,spc = 0,0,0,0
fn = input("enter file name to read")
with open(fn) as obj1:
    st = obj1.read(2000)
    for x in st:
        if x.isdigit():
            dig += 1
        elif x.isupper():
            upp += 1
        elif x.islower():
            loww += 1
        elif x.isspace():
            spc += 1

print("digit count: ",dig)
print("upper case count",upp)
print("lower case count",loww)
print("space count",spc)
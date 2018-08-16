'''RollNo=[]
for i in range(1,10):
    RollNo.append(i)

print(RollNo)

x=[1,5,3,8,90,50]
x.sort()
print(x)


empty={}
print (type(empty))
print(empty==dict())

a=dict(one=1, two=2, three=3)
b={"one":1, "two":2, "three":3}
print (a == b)


i = dict(Fname='sonu', Lname='kumar', Degree='MCA')
j={'Fname':'sonu','Lname':'kumar','Degree':'MCA'}
print(i==j)
print(len(i),len(j))

print(i['Fname'])
i['Four']=23
i['Degree']='BCA'
print(i)

d={"CS":[106,107,108],"MATH":[51,113]}
print(d)
print(len(d))


print(d.get("CS"))
print(d["CS"])
english_classes=d.get("ENGLISH",[])
num_english=len(english_classes)
print(english_classes)




b={"one":1, "two":2, "three":3}
print(b)
del b["one"]
print(b)
b.pop("three")
print(b)

b={"one":1, "two":2, "three":3}
print(b.keys())
print(b.values())
print(b.items())
print(len(b.items()))

print(('one',1) in b.items())
for value in b.items():
    print(value)

b={"one":1, "two":2, "three":3}
print(len(b))

print(key in b)
vlaue in b.values()
b.copy 



t =(1,"cat")
print(t)


fish=(1,2,"red","blue")
print(fish[0])

print(len(fish))
print(fish[:2])
print("red" in fish)'''

t=1234,5435,1264,'abc','xyz'
print(type(t))


t=1234,5435,1264
x,y,z=t
print(x)
print(y)
print(z)

#swapping no. method 1
x=5
y=4
(x,y)=(y,x)
print("x=",x,"y=",y)

#swapping no. method 2
a=10
b=20
a=a^b
b=a^b
a=a^b
print("a=",a,"b=",b)


















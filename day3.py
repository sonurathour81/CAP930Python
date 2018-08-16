""" print(len([]))
print(len)

print(len('Python'))

#Memebership function

print('p' in 'Python')

print('P' in 'Python')

print('o' in 'sonu')

print('Apple' in ['Banana','Mango','Grapes'])

print('Banana' in ['Banana','Mango','Grapes'])

#Console I/O
name=input('you name please')
print(name)

print("dont talk in class",name)

a=5
if a>2:
        print("a is greater than 2")
elif a==5:
        print("a is equal to 5")
else:
        print("a is less than 2")


word= input("Please enter a word:")
print(word)
reversed_word=word[::-1]
if word == reversed_word:
    print("you entered a palindrome:")
else:
    print("you did not enter palindrome:")



print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(1))


data=[]
if data:
    process(data)
else:
    print("There is no data")



#Loops

print(range(3))

print(range(5,10))

print(range(2,12,3))

for i in range(10):
 print(i)

for i in range(5,20):
 print(i)


for n in range(10):
    if n==6:
            break
    print(n)

for n in range(10):
    if n%2==0:
        print("even",n)
        continue
    print("odd",n)



def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    
n=input("enter a number")
for x in range(2,int(n)):
    if is_prime(x):
            print(x,"is prime")
    else:
            print(x,"is not prime")


"""








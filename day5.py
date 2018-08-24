'''basket=set('apple')
print(basket)
basket.add('m')
print(basket)
basket.remove('m')
print(basket)
basket.discard('x')
print(basket)
basket.pop()
print(basket)
basket.clear()
print(basket)
len(basket)
print(basket)

a=set("abracadabra")
b=set("alacazam")
c=set("bcsonu")
print(a)
print(b)
print(c)

#Set Diffenence
print(a-b)

#Set of Union
print(a|b)

#Set of Intersection
print(a&b)

# Set of Symmetric differnece
print(a^b)


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for v in knights.values():
    print(v)
'''
a = {'key1':[1,2,3,4], 'key2':[5,6,7,8],'key3':'66.25'}
for k,v in a.items():
    print("key is ",k,"= value is ",v)

print(a['key2'][3])

x=1,2,3,4
print(type(x))

#program latihan dasar python

#output python
print ("OUTPUT PYTHON: ")
print ("Hello, this is my first python project!")
print ("my first python project in", 2026)

#python comments
#komentar ditandai dengan tanda ("#")

#python variables
print ("PYTHON VARIABLES: ")
x, y, z = "math", "chemistry", "biology"
print (x)
print (y)
print (z)

#python data types
print ("PYTHON DATA TYPES: ")
x = str ("learning python")
print (type(x))
x = 2
print (type(x))

#python numbers 
print ("PYTHON NUMBERS: ")
x = float (5)
y = int (2.3)
print (x)
print (y)
print (type(x))
print (type(y))

#python casting
print ("PYTHON CASTING: ")
a = str(7)
b = str("Hi")
print (a)
print (b)

#python strings
print ("PYTHON STRINGS: ")
a = "hi, everyone"
print (len(a)) #hitung panjang
print (a[2] ) #elemen array

for x in "apple":
   print (x) #for loop

text = "never give up" #check string
print ("up" in text) #true or false

#python boolean (true or false)
print ("PYTHON BOOLEAN: ")
print (2 < 1)

a = 40
b = 50
if a > b:
   print ("a lebih besar dari b")
else:
   print ("a tidak lebih besar dari b")

print (bool("cherry")) #true
print (bool(0)) # false

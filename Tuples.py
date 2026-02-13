#cetak tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print('tuple dgn satu item: ')
thistuple = ("apple",)
print(type(thistuple))

print('tuple dgn berbagai tipe data: ')
tuple1 = ("abc", 34, True, 40, "male")

#panjang tuple(menentukan berapa banyak item tuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#membuat tuple [tuple()]
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[0]) #item pertama memiliki indeks 0

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #-1 mengacu pada item terakhir

#rentang indeks
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #Pencarian akan dimulai pada indeks 2 (termasuk) dan berakhir pada indeks 5 (tidak termasuk).

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #kiwi tdk termasuk

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #mengembalikan item dari "cherry" hingga akhir

#memeriksa apakah suatu item ada [in]
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#update tuples
#mengubah tuple menjadi list 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#menambahkan item
#konversi menjadi list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#hapus item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#unpack tuples (menetapkan nilai)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#dengan asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#loop tuples
#for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#looping melalui no indeks
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#dgn while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join tuples (menggabungkan tuples)
#dgn operator +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#mengalikan banyak isi tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



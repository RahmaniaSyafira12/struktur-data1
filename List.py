#list allow duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list item-data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#access list items
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change list items
#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insert items
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#tambahkan item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#sisipkan item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Perluas Daftar
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Tambahkan Objek Iterasi Apa Saja
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove list item
#Hapus Item yang Ditentukan
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#kata pisang pertama terhapus
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#hapus indeks yg ditentukan
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#loop list
#Cetak semua item dalam daftar, satu per satu:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#berdasarkan no indeks
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#dgn while untuk menelusuri semua no indeks
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#sort list
#diurutkan scr alfabetik
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#diurutkan scr numerik
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#diurutkan scr menurun
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#pengurutan terbalik
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#copy list
#metode copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#metode list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#metode operator slice (:)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join list (menggabungkan list)
#menggunakan operator (+)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#menambahkan list2 ke list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#menggunakan extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



#menghitung panjang set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#membuat himpunan
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#access set items (dengan perulangan for atau in)
#for
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#in
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#add set items
#menambah item ke dalam set [add()]
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#menambah item dari set lain [update()]
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#remove set items
#remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#hapus acak [pop()]
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#mengosongkan himpunan [clear()]
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#loop sets[for loop]
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join sets(menggabungkan set)
#menggabungkan seluruh himpunan [union() atau |]
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#menggabungkan beberapa himpunan [union() atau |]
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#menggabungkan himpunan dan tipe data lain (tuple)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#update [update()]
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection (mengembalikan himpunan baru yg duplikat) [intersection() atau &]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#difference(mengembalikan item hp 1 yg tidak ada di hp lain) [difference() atau -]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#symetric difference (menyimpan elemen yg tak terdapat di keduanya) [symetric_difference() atau ^]
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#frozenset (himpunan yg tak dpt diubah)[frozenset()]
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) #memeriksa tipe objek


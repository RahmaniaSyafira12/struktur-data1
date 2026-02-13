#print dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#membuat kamus [dict()]
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#change items or update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#add items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#remove items
#metode pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#metode del
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#metode clear () (mengosongkan kamus)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#loop dictionaries (for loop)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('cetak keys dictionaries: ')
for x in thisdict:
  print(x)

print('cetak nilai dictionaries: ')
for x in thisdict:
  print(thisdict[x])

#copy dictionaries
#copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#ditch()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

print('------------------------------------------------------------------')


#nested dictionaries (kamus bersarang)
#contoh kamus yg berisi tiga kamus
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#mengakses item nested dictionaries
print(myfamily["child2"]["name"]) #menuliskan nama anak ke-2

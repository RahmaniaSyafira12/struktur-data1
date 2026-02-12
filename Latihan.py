#class person
class Person:
  def __init__(self, nama, jenis_kelamin, umur):
    self.nama = nama
    self.jenis_kelamin = jenis_kelamin
    self.umur = umur

  def printname(self):
    print(self.nama, self.jenis_kelamin, self.umur)

#class karyawan yg mewarisi person
class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur, gaji):
        super().__init__(nama, jenis_kelamin, umur)
        self._gaji = gaji
    def get_gaji(self):
        return self._gaji

#class rekening
class Rekening:
    def __init__(self, norek, pin):
        self.norek = norek
        self.__pin = pin
    #getter
    def get_pin(self):
            return self.__pin
    #setter
    def set_pin(self, new_pin):
            self.__pin = new_pin

#Objek
x1 = Person('windah', 'pria', 29)
k1 = Karyawan('windah', 'pria', 29, 10000000)
r1 = Rekening('1234567890', '0987')

print('Nama: ', x1.nama)
print('Jenis Kelamin: ', x1.jenis_kelamin)
print('umur: ', x1.umur)
print('gaji:', k1.get_gaji())
print('Rekening: ', r1.norek) 
print('PIN:', r1.get_pin())

#update PIN
r1.set_pin('1789')
print('PIN baru: ', r1.get_pin())






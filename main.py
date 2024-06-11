# a = 10, a adalah variabel dan 10 adalah nilainya.
#angka integer :
data_integer = 1
print("Data : ", data_integer)
print("- bertipe :", type(data_integer))

#tipe data: angka dengan koma (float)

data_float = 1.5

print("Data : ", data_float)
print("- bertipe :", type(data_float))


#tipe data: kumpulan karakter (string)
data_string = "AFZAH"

print("Data : ", data_string)
print("- bertipe :", type(data_string))

#tipe data: biner true/false(boolean)
data_bool = False

print("Data : ", data_bool)
print("- bertipe :", type(data_bool))

##tipe data khusus

##bilangan kompleks

data_complex = complex(5,6)
print("Data : ", data_complex)
print("- bertipe :", type(data_complex))

#tipe data dari bahasa c

from ctypes import c_double, c_char, c_long

data_c_dobule = c_double(10.5)
print("Data : ", data_c_dobule)
print("- bertipe :", type(data_c_dobule))


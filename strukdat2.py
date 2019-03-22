"""
Gunakan list, tuple dan dictionary yang digunakan
Pada  kode sumber strukdat1.py, jika tidak disertakan
Akan muncul error
"""

# cara mendefinisikan list
sebuah_list = ['Zorin OS', 'Ubuntu', 'FreeBSD', 'NetBSD', 'OpenBSD', 'Backtrack', 'Fedora', 'Slackware']

# cara mendefinisikan tuple
sebuah_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# cara mendefinisikan dictionary
sebuah_dictionary = {'nama':'Wiro Sableng',
                    'prodi':'ilmu komputer',
                    'email':'wirosableng@localhost',
                    'website':'http://www.sitampanggarang.com'
                    }

# mengakses elemennya
print "mengakses semua elemen dengan looping for : "
print "-----------------------------"

for sebuah in sebuah_list:
    print sebuah
print "\n"

for sebuah in sebuah_tuple:
    print sebuah
print "\n"

for sebuah in sebuah_dictionary:
    print sebuah, ':', sebuah_dictionary [sebuah]

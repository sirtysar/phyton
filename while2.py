terus_tanya = True
while terus_tanya :
    temp = raw_input('masukkan angka kurang dari 10  !! : ')
    angka = int(temp)
    if angka < 10:
        terus_tanya = False
    else:
        terus_tanya = True

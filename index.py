print("Hitung luas ruangan")
panjang = int(input("Masukkan Panjang Ruangan :"))
lebar = int(input("Masukkan Lebar Ruangan :"))
satuan = str(input("Masukkkan Satuan (Meter/Inchi):"))

hasil = panjang * lebar

if satuan == "Meter" :  
    
    print("Luas ruangan dengan panjang", panjang, "dan lebar ", lebar , "adalah", hasil , satuan)  
     
elif satuan == "Inchi" :
    
    print("Luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adalah", hasil, satuan)
else :
    print("Input salah")
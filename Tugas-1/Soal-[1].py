name = input("Enter name : ")
umur = int(input("Enter age : "))
tinggi = float(input("Enter heigt : "))

txtnama = "Nama saya {} , ". format(name)
txtumur = "umur saya {} tahun ". format(umur)
txttinggi = "dan tinggi saya {} cm". format(tinggi)
txtgabung = txtnama + txtumur + txttinggi

print(txtgabung)


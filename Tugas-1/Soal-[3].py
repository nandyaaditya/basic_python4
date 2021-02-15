u_teori = float(input("Enter nilai ujian teori : "))
u_praktek = float(input("Enter nilai ujian praktek : "))

if u_teori >= 70 and u_praktek >= 70:
    print("Selamat, anda lulus!")

elif u_teori >=70 and u_praktek <= 70:
    print("Anda harus mengulang ujian praktek.")

elif u_teori <=70 and u_praktek >= 70:
    print("Anda harus mengulang ujian teori.")

elif u_teori <=70 and u_praktek <= 70:
    print("Anda harus mengulang ujian teori dan praktek.")

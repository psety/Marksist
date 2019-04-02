import mysql.connector
import time

# CLASS BLOCK WILL BE HERE 
class Student():
    def __init__(self,id,name,surname,vize1,vize2,final):
        self.id = id
        self.name = name
        self.surname = surname
        self.vize1 = vize1
        self.vize2 = vize2
        self.final = final
        
    def __str__(self):
        return "ID :{}\nName :{}\nSurname :{}\nVize 1:{}\nVize 2:{}\nFinal :{}".format(self.id, self.name, self.surname, self.vize1, self.vize2, self.final)

class Lecture():
    def __init__(self):
        self.BaglantiOlustur()
    def BaglantiOlustur(self):
        self.cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Espr3ss0*",
        database = "mydatabase"
        )
        self.my_cursor = self.cnx.cursor()
        #self.my_cursor.execute("CREATE DATABASE mydatabase")
        #sorgu = "CREATE TABLE IF NOT EXIST students (id_no INTEGER(100), name VARCHAR(255), surname VARCHAR(255), vize1 INTEGER(100), vize2 INTEGER(100), final INTEGER(100))"
        #self.my_cursor.execute(sorgu)
        self.cnx.commit()               #save the changes
        self.my_cursor.execute("SHOW TABLES")
        for x in self.my_cursor:
            print(x)
    def BaglantiKes(self):
        self.cnx.close()
    
    def ListStudents(self):
        sorgu = "SELECT * FROM students"
        self.my_cursor.execute(sorgu)
        sonuc = self.my_cursor.fetchall()
        if len(sonuc) == 0:
            print("No Student Found")
        else:
            for x in sonuc:
                print(x[0],x[1],x[2],x[3],x[4],x[5])
    
    def FindStudentName(self,isim):
        sorgu = "SELECT * FROM students WHERE name = %s"
        self.my_cursor.execute(sorgu,(isim,))
        result = self.my_cursor.fetchall()
        if len(result) == 0:
            print("Students not found ")
        else:
            for x in result:
                print(x[0],x[1],x[2],x[3],x[4],x[5])
    
    def AddStudent(self,student):
        sorgu = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s)"
        self.my_cursor.execute(sorgu,(student.id,student.name,student.surname,student.vize1,student.vize2,student.final))
        self.cnx.commit()
    def DeleteStudent(self,id_no):
        sorgu = "DELETE FROM students WHERE id_no = %s"
        self.my_cursor.execute(sorgu,(id_no,))
        self.cnx.commit()
    def AddVize1(self,id_no):
        sorgu = "SELECT * FROM students WHERE id_no = %s"
        self.my_cursor.execute(sorgu,(id_no,))
        result = self.my_cursor.fetchall()
        print(result)
        if len(result) == 0:
            print("ID has not found")
        else:
            print(result[0][3])
            not1 = int(input("Vize 1 :"))
            #not1 = result[0][3]
            sorgu2 = "UPDATE students SET vize1 =%s"
            self.my_cursor.execute(sorgu2,(not1,))
            self.cnx.commit()
            print("Suceedded..")
    def AddVize2(self,id_no):
        sorgu = "SELECT * FROM students WHERE id_no = %s"
        self.my_cursor.execute(sorgu,(id_no,))
        result = self.my_cursor.fetchall()
        if len(result) == 0:
            print("ID has not found")
        else:
            not2 = int(input("Vize 2 :"))
            #not1 = result[0][3]
            sorgu2 = "UPDATE students SET vize2 =%s"
            self.my_cursor.execute(sorgu2,(not2,))
            self.cnx.commit()
            print("Suceedded..")
    def AddFinal(self,id_no):
        sorgu = "SELECT * FROM students WHERE id_no = %s"
        self.my_cursor.execute(sorgu,(id_no,))
        result = self.my_cursor.fetchall()
        if len(result) == 0:
            print("ID has not found")
        else:
            not3 = int(input("Dönem Sonu :"))
            #not1 = result[0][3]
            sorgu2 = "UPDATE students SET final =%s"
            self.my_cursor.execute(sorgu2,(not3,))
            self.cnx.commit()
            print("Suceedded..")
        
print("""
#########################################
##       Lecture Marking System        ##
##                                     ##
##                                     ##
##  1 - Öğrencileri Listele            ##
##  2 - Öğrenci Sorgula                ##
##  3 - Bi' Öğrenci Ekle               ##
##  4 - ID no ile Vize1'yi gir         ##
##  5 - ID no ile Vize2'yi gir         ##
##  6 - ID no ile Finali gir           ##
##  7 - Öğrenci Sil                    ##
##                                     ##
##           "x" : Exit                ##
##                                     ##
#########################################
""")

stu = Lecture()

while True:
    islem = input ("Lütfen bir işlem seçiniz :")
    if islem == "x" or islem == "X":
        print("Programdan çıkılıyor...")
        time.sleep(2)
        print("Kullandığınız için teşekkür ederiz.")
        time.sleep(1)
        break
    elif islem == "1":
        stu.ListStudents()
    elif islem == "2":
        isim = input("Sorgulanacak ögrenci ismini giriniz: ")
        print("Sorgulama Yapılıyor...")
        time.sleep(2)
        stu.FindStudentName(isim)
    elif islem == "3":
        idnum  = int(input ("Ogrenci Numarası :"))
        name = input("Isim :")
        surname = input("Soyisim :")
        vize1 = 0
        vize2 = 0
        final = 0
        yeni_ogrenci = Student(idnum,name,surname,vize1,vize2,final)
        print("Ogrenci Ekleniyor...")
        print(yeni_ogrenci)
        time.sleep(2)
        stu.AddStudent(yeni_ogrenci)
        print("Öğrenci Eklendi...")
        time.sleep(1)
    
            
    elif islem == "4":
        idno = input("Birinci vize notu girilecek öğrencinin numarasını giriniz : :")
        print("Birinci vize notu giriliyor...")
        time.sleep(2)
        stu.AddVize1(idno)
        print("Birinci vize notu eklendi...")
        time.sleep(1)
    elif islem == "5":
        idno = input("İkinci vize notu girilecek öğrencinin numarasını giriniz : :")
        print("İkinci vize notu giriliyor...")
        time.sleep(2)
        stu.AddVize2(idno)
        print("İkinci vize notu eklendi...")
        time.sleep(1)
    elif islem == "6":
        idno = input("Dönem sonu notu girilecek öğrencinin numarasını giriniz : :")
        print("Dönem sonu notu giriliyor...")
        time.sleep(2)
        stu.AddFinal(idno)
        print("Dönem sonu notu eklendi...")
        time.sleep(1)

    elif islem == "7":
        idno = int(input("Silinecek Öğrencinin Numarasını Giriniz :"))
        cevap = input("Emin Misiniz ? (E/H) :")
        if cevap == "E" or cevap == "e":
            print("Öğrenci siliniyor...")
            time.sleep(2)
            stu.DeleteStudent(idno)
            print("Öğrenci Silindi...")
            time.sleep(1)

    else:
        print("Hatalı Giriş Yaptınız.")


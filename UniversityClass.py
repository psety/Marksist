import mysql.connector
import time
import xlrd
import xlsxwriter
#import wget

#-*- coding: <utf-8> -*-
##CLASS BLOCK WILL BE HERE 
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
        #buraya bir try except at. 
        self.cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Espr3ss0*",
        database = "mydatabase"                 # Comment at First Creation
        )
        self.my_cursor = self.cnx.cursor()
        #self.my_cursor.execute("CREATE DATABASE mydatabase")           #UNCOMMENT AT PHASE1
        #sorgu = "CREATE TABLE IF NOT EXIST students (id_no INTEGER(100), name VARCHAR(255), surname VARCHAR(255), vize1 INTEGER(100), vize2 INTEGER(100), final INTEGER(100))"
        #self.my_cursor.execute(sorgu)
        #self.cnx.commit()               #save the changes
        self.my_cursor.execute("SHOW TABLES")
        for x in self.my_cursor:
            print(x)
    def BaglantiKes(self):
        self.cnx.close()
    def FuckTheSQLTable(self):
        sorgu = "DELETE FROM students"
        self.my_cursor.execute(sorgu)
        self.cnx.commit()
    def ListStudents(self):
        sorgu = "SELECT * FROM students"
        self.my_cursor.execute(sorgu)
        sonuc = self.my_cursor.fetchall()
        if len(sonuc) == 0:
            print("No Student Found")
        else:
            for x in sonuc:
                print(x[0],x[1],x[2],x[3],x[4],x[5])

    def SqlToExcel(self):
        sorgu = "SELECT * FROM students"
        self.my_cursor.execute(sorgu)
        sonuc = self.my_cursor.fetchall()
        excelid = []
        excelnames = []
        excelsurnames = []
        excelvize1 = []
        excelvize2 = []
        excelDonemSonu = []
        xlsxname = input("Enter the name of excel file which will be created : ")
        outWorkbook = xlsxwriter.Workbook(xlsxname +".xlsx") 
        outSheet = outWorkbook.add_worksheet()
        outSheet.write(0,0,"ID")
        outSheet.write("B1","NAMES")
        outSheet.write("C1","SURNAMES")
        outSheet.write("D1","VIZE 1")
        outSheet.write("E1","VIZE 2")
        outSheet.write("F1","DONEM SONU")
        outSheet.write("G1","ORTALAMA")
        #outWorkbook.close()
        #inputWorkbook = xlrd.open_workbook(xlsxname +".xlsx")
        #inputWorksheet = inputWorkbook.sheet_by_index(0)
        for x in sonuc:
            #print(x[0],x[1],x[2],x[3],x[4],x[5])
            excelid.append(x[0])
            excelnames.append(x[1])
            excelsurnames.append(x[2])
            excelvize1.append(x[3])
            excelvize2.append(x[4])
            excelDonemSonu.append(x[5])
        print(len(sonuc))
        for item in range(len(sonuc)):
            #print(excelnames[item])
            outSheet.write(item+1, 0, excelid[item])
            outSheet.write(item+1, 1, excelnames[item])
            outSheet.write(item+1, 2, excelsurnames[item])
            outSheet.write(item+1, 3, excelvize1[item])
            outSheet.write(item+1, 4, excelvize2[item])
            outSheet.write(item+1, 5, excelDonemSonu[item])
        outWorkbook.close()
        #for xx in sonuc: #okuma yapmıyorsun direk yaz sonra kapat.... unutma. 
        #    outSheet.write(inputWorksheet.nrows +1 ,0,xx[0][0])
        #    outSheet.write(inputWorksheet.nrows +1 ,1,xx[0][1])
         #   outSheet.write(inputWorksheet.nrows +1 ,2,xx[0][2])
          #  outSheet.write(inputWorksheet.nrows +1 ,3,xx[0][3])
        #    outSheet.write(inputWorksheet.nrows +1 ,4,xx[0][4])
        #    outSheet.write(inputWorksheet.nrows +1 ,5,xx[0][5])
            #outSheet.write(inputWorksheet.nrows+1,6,x[3])
            #outWorkbook.close()

    def FindStudentSurname(self,isim):
        sorgu = "SELECT * FROM students WHERE surname LIKE %s"
        self.my_cursor.execute(sorgu,('%'+ isim +'%',))
        result = self.my_cursor.fetchall()
        if len(result) == 0:
            print("Students not found ")
        else:
            for x in result:
                print(x[0],x[1],x[2],x[3],x[4],x[5])    
        
    def AddStudent(self,student):
        sorgu2 = "SELECT * FROM students WHERE id_no = %s"
        self.my_cursor.execute(sorgu2,(student.id,))
        result = self.my_cursor.fetchall()
        #n = 0
        if len(result) == 0:
            sorgu = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s)"
            self.my_cursor.execute(sorgu,(student.id,student.name,student.surname,student.vize1,student.vize2,student.final))
            self.cnx.commit()
            print("Öğrenci Eklendi...")
            time.sleep(0.2)
            #n += 1
        #print("Eklenen ogrenci sayisi : {}".format(n))
    def DeleteStudent(self,id_no):
        sorgu = "DELETE FROM students WHERE id_no = %s"
        self.my_cursor.execute(sorgu,(id_no,))
        self.cnx.commit()
    def AddVize1(self,surname):
        sorgu = "SELECT * FROM students WHERE surname = %s"
        self.my_cursor.execute(sorgu,(surname,))
        result = self.my_cursor.fetchall()
        print(result)
        if len(result) == 0:
            print("ID has not found")
        elif len(result) >= 2:          #iki veya daha fazla sonuç için sonuclar listelenip id no ile giriş yapılacak
            idno = int(input("ID NO Giriniz :"))
            sorgu = "SELECT * FROM students WHERE id_no = %s"
            self.my_cursor.execute(sorgu,(idno,))
            result = self.my_cursor.fetchall()
            not1 = int(input("Vize 1 :"))
            sorgu2 = "UPDATE students SET vize1 =%s WHERE id_no = %s"
            self.my_cursor.execute(sorgu2,(not1,idno))
            self.cnx.commit()
            print("Suceedded..")
        else:                           #tek kişi çıkarsa burası çalışacak
            not1 = int(input("Vize 1 :"))
            sorgu2 = "UPDATE students SET vize1 =%s WHERE surname = %s"
            self.my_cursor.execute(sorgu2,(not1,surname))
            self.cnx.commit()
            print("Suceedded..")
    def AddVize2(self,surname):
        sorgu = "SELECT * FROM students WHERE surname = %s"
        self.my_cursor.execute(sorgu,(surname,))
        result = self.my_cursor.fetchall()
        print(result)
        if len(result) == 0:
            print("ID has not found")
        elif len(result) >= 2:          #iki veya daha fazla sonuç için
            idno = int(input("ID NO Giriniz :"))
            sorgu = "SELECT * FROM students WHERE id_no = %s"
            self.my_cursor.execute(sorgu,(idno,))
            result = self.my_cursor.fetchall()
            not2 = int(input("Vize 2 :"))
            sorgu2 = "UPDATE students SET vize2 =%s WHERE id_no = %s"
            self.my_cursor.execute(sorgu2,(not2,idno))
            self.cnx.commit()
            print("Suceedded..")
        else:                           #tek kişi çıkarsa burası çalışacak
            not2 = int(input("Vize 2 :"))
            sorgu2 = "UPDATE students SET vize2 =%s WHERE surname = %s"
            self.my_cursor.execute(sorgu2,(not2,surname))
            self.cnx.commit()
            print("Suceedded..")
    def AddFinal(self,surname):
        sorgu = "SELECT * FROM students WHERE surname = %s"
        self.my_cursor.execute(sorgu,(surname,))
        result = self.my_cursor.fetchall()
        print(result)
        if len(result) == 0:
            print("ID has not found")
        elif len(result) >= 2:          #iki veya daha fazla sonuç için
            idno = int(input("ID NO Giriniz :"))
            sorgu = "SELECT * FROM students WHERE id_no = %s"
            self.my_cursor.execute(sorgu,(idno,))
            result = self.my_cursor.fetchall()
            not3 = int(input("Vize 2 :"))
            sorgu2 = "UPDATE students SET final =%s WHERE id_no = %s"
            self.my_cursor.execute(sorgu2,(not3,idno))
            self.cnx.commit()
            print("Suceedded..")
        else:                           #tek kişi çıkarsa burası çalışacak
            not3 = int(input("Final :"))
            sorgu2 = "UPDATE students SET final =%s WHERE surname = %s"
            self.my_cursor.execute(sorgu2,(not3,surname))
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
##  4 - Vize1 Notlarını Gir            ##
##  5 - Vize2 Notlarını Gir            ##
##  6 - Final Notlarını Gir           ##
##  7 - Öğrenci Sil                    ##
##                                     ##
##           "x" : Exit                ##
##                                     ##
#########################################
""")


stu = Lecture()

while True:   
    islem = input ("Ana Menü için lütfen bir işlem seçiniz :")
    if islem == "x" or islem == "X":
        print("Programdan çıkılıyor...")
        time.sleep(2)
        print("Kullandığınız için teşekkür ederiz.")
        time.sleep(1)
        break
    elif islem == "1":
        stu.ListStudents()
    elif islem == "2":
        soyisim = input("Sorgulanacak ögrenci soyismini giriniz: ")
        print("Sorgulama Yapılıyor...")
        time.sleep(2)
        stu.FindStudentSurname(soyisim)
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
        while True:
                soyisim = input("Birinci Vize İçin Soyadı : ")
                if soyisim == "x" or soyisim =="X":
                        break
                else:
                        stu.AddVize1(soyisim)
                        print("Birinci vize notu eklendi...")
    elif islem == "5":
        while True:
                soyisim = input("İkinci Vize İçin Soyadı : ")
                if soyisim == "x" or soyisim =="X":
                        break
                else:
                        stu.AddVize2(soyisim)
                        print("İkinci vize notu eklendi...")
    elif islem == "6":
        while True:
                soyisim = input("Final Sınavı İçin Soyadı : ")
                if soyisim == "x" or soyisim =="X":
                        break
                else:
                        stu.AddFinal(soyisim)
                        print("Final notu eklendi...")

    elif islem == "7":
        idno = int(input("Silinecek Öğrencinin Numarasını Giriniz :"))
        cevap = input("Emin Misiniz ? (E/H) :")
        if cevap == "E" or cevap == "e":
            print("Öğrenci siliniyor...")
            time.sleep(2)
            stu.DeleteStudent(idno)
            print("Öğrenci Silindi...")
            time.sleep(1)
    elif islem == "101":
        path = "deneme1.xlsx"
        print("Bu kisim excel dosyanin mysql e yazilma kismi icin konulmustur. Ana menuye yazilmamistir.")
        print("Path : {}, Kod icerisinde düzenleme yapılmalıdır.".format(path))
        inputWorkbook = xlrd.open_workbook(path)
        inputWorksheet = inputWorkbook.sheet_by_index(0)
        idnos = list()
        names = list()
        surnames = list()
        remaining = list()
        codeinput = input("Pass ? :")
        if codeinput == "1010":
            for y in range(0, inputWorksheet.ncols):
                for x in range(1,inputWorksheet.nrows):    # Excel dosyasinda baslıklar varsa 1 den başla. 
                    if y == 0:
                      idnos.append(int(inputWorksheet.cell_value(x,y)))
                    elif y ==1:
                        names.append(inputWorksheet.cell_value(x,y))
                    elif y == 2:
                        surnames.append(inputWorksheet.cell_value(x,y))
                    else:
                        remaining.append(inputWorksheet.cell_value(x,y))
                    #print(names)
                SqlTypeList = list()
                SqlTypeList = zip(idnos,names,surnames)
                SqlTypeList = list(SqlTypeList)
                print(SqlTypeList)
                
                for x in SqlTypeList:
                    sqlid = x[0]
                    sqlname = x[1]
                    sqlsurname = x[2]
                    print(x[0],x[1],x[2])
                    sqlvize1 = 0
                    sqlvize2 = 0
                    sqlfinal = 0
                    yeni_ogrenci1 = Student(sqlid,sqlname,sqlsurname,sqlvize1,sqlvize2,sqlfinal)
                    #sorgu = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s)"
                    #print(yeni_ogrenci1)
                    stu.AddStudent(yeni_ogrenci1)

                
    elif islem == "66":
        print("Order 66 will be executed...")
        time.sleep(1)
        print("Database'in emüna koyacaksın...")
        silmeislemi = input("İşlem geri alınamaz. Emin misin ? (E/H) : ")
        if silmeislemi == "e" or silmeislemi =="E":
            DBsifresi = input("Database silme sifresi giriniz :")
            if DBsifresi == "fuck":
                print("Çekerim emaneti...")
                time.sleep(2)
                stu.FuckTheSQLTable()
                print("Sikerim adaleti...")
                time.sleep(2)
    
    elif islem == "999":
        
        stu.SqlToExcel()
        
    else:
        print("Hatalı Giriş Yaptınız.")
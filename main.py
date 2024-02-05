from tkinter import *
from tkinter import filedialog, messagebox
import re
def dosyaSec():
    global root
    global dosyaİsimleri
    dosyaLabelları = []
    dosya_yolu = filedialog.askopenfilenames(initialdir="/")
    print(dosya_yolu)

    x = 0
    y= 125
    sayac = 0
    for i in dosya_yolu:
        dosyaİsimleri.append(i)

    print(dosyaİsimleri)
    for j in range(0,len(dosyaİsimleri)):
        dosyaLabelları.append("")
        dosyaLabelları[j] = Label(root,text=f"{dosyaİsimleri[j]}")
        dosyaLabelları[j].place(y=y, x=x)
        y = y+25

    return dosya_yolu
def dosyaGuncelle():
    dosya_yolu = dosyaİsimleri
    satırListem = []
    #birden fazla dosya seçince, dosya_yolu tuple bir duruma geldi.
    print(f"dosya yolu türü {type(dosya_yolu)}")
    for i in dosya_yolu:
        with open(i, "r", encoding="utf-8") as dosya:
            for j in dosya.readlines():
                satırListem.append(j)

        with open(i,"w",encoding="utf-8") as guncelDosya:
            sayac = 1
            for j in satırListem:
                j = j.replace('"','')
                j = j.replace('""','')
                j = j.replace("'",'')
                j = j.replace("“",'')
                j = j.replace("”",'')
                j = j.replace("‘",'')
                j = j.replace("’",'')
                j = j.strip()
                j = re.sub(r'\[\d+\]','',j) #[Herhangi bir Sayı] yapısı varsa silenecektir. \ escape için kullanılır.
                j = re.sub(r'\s+',' ',j) #Birden fazla boşluk varsa tek boşlukla değiştir.
                print(f"{j} {sayac}")
                sayac = sayac + 1
                if j != "":
                    if j[len(j) - 1] == "-":
                        j = j.removesuffix("-")
                        #i = i.replace("-", '')
                        guncelDosya.write(f"{j}")
                    else:
                        guncelDosya.write(f"{j}\n")

        satırListem.clear()
    messagebox.showinfo("Bilgilendirme", "İşlem Başarıyla Tamamlandı.!")
dosyaİsimleri = []
root = Tk()
root.title("Txt Formatlayıcı Program")
root.geometry("600x400+850+400")
root.configure(bg="lightblue")
txtGirisiAl = Label(root, text="Düzeltmek İstediğiniz Txt Seçiniz")
root.update_idletasks()
label_genislik = txtGirisiAl.winfo_reqwidth()
label_uzunluk = txtGirisiAl.winfo_reqheight()
genislik = root.winfo_width()
uzunluk = root.winfo_height()

print(f"Genislik:{genislik}, Uzunluk: {uzunluk}, label genislik: {label_genislik}, label_uzunluk:{label_uzunluk}")
txtGirisiAl.place(y=25, x=50)
#place'e verilen y değeri aşağıya doğru artar. x değeri ise sağa doğru artar.

dosyayiSec = Button(root,command=dosyaSec,text="Seç")
dosyayiSec.place(y=50,x=50)

dosyalariDuzelt = Button(root,command=dosyaGuncelle,text="Düzenle")
dosyalariDuzelt.place(y=75, x=50)
root.mainloop()



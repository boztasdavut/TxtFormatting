from tkinter import *
from tkinter import filedialog, messagebox
import re

def dosyaSec():
    dosya_yolu = filedialog.askopenfilename(initialdir="/")
    satırListem = []
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        for i in dosya.readlines():
            satırListem.append(i)

    with open(dosya_yolu,"w",encoding="utf-8") as guncelDosya:
        sayac = 1
        for i in satırListem:
            i = i.replace('"','')
            i = i.replace('""','')
            i = i.replace("'",'')
            i = i.replace("“",'')
            i = i.replace("”",'')
            i = i.replace("‘",'')
            i = i.replace("’",'')
            i = i.strip()
            i = re.sub(r'\s+',' ',i) #Birden fazla boşluk varsa tek boşlukla değiştir.
            print(f"{i} {sayac}")
            sayac = sayac + 1
            if i != "":
                if i[len(i) - 1] == "-":
                    i = i.removesuffix("-")
                    #i = i.replace("-", '')
                    guncelDosya.write(f"{i}")
                else:
                    guncelDosya.write(f"{i}\n")

    messagebox.showinfo("Bilgilendirme","İşlem Başarıyla Tamamlandı.!")



root = Tk()
root.title("Txt Formatlayıcı Program")
root.geometry("600x400+850+400")
txtGirisiAl = Label(root, text="Düzeltmek İstediğiniz Txt Seçiniz")
root.update_idletasks()
label_genislik = txtGirisiAl.winfo_reqwidth()
label_uzunluk = txtGirisiAl.winfo_reqheight()
genislik = root.winfo_width()
uzunluk = root.winfo_height()
x = (genislik-label_genislik)/2
y = (uzunluk-label_uzunluk)/2
print(f"Genislik:{genislik}, Uzunluk: {uzunluk}, label genislik: {label_genislik}, label_uzunluk:{label_uzunluk}")
txtGirisiAl.place(y=y, x=x)
#place'e verilen y değeri aşağıya doğru artar. x değeri ise sağa doğru artar.

dosyayiSec = Button(root,command=dosyaSec,text="Seç")
dosyayiSec.place(y=y+25,x=x)


root.mainloop()



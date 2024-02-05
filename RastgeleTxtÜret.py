import random
def rastgeleTxtYaz():
    karakterListesi = [
        'a','b','c','d','e','f',"'",'"','""','“','”','‘','’','-'
        ,'\n','1','2','3','4','5','6','7','8','9'
    ]
    string = ""
    for i in range(0,1000):
        string = string+random.choice(karakterListesi)
    return string
with open("deneme.txt","w",encoding="utf-8") as dosya:
    dosya.write(rastgeleTxtYaz())


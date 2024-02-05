import random
def rastgeleTxtYaz():
    karakterListesi = [
        'a','b','c','d','e','f',"'",'"','""','“','”','‘','’','-'
        ,'\n'
    ]
    string = ""
    for i in range(0,1000):
        string = string+random.choice(karakterListesi)
    return string
with open("deneme.txt","w",encoding="utf-8") as dosya:
    dosya.write(rastgeleTxtYaz())


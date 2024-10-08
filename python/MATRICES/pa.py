'''''
list1 = ["pera-f", "tigre-a","camilo-p","banano-f"]
def funcion(list):
    for i in list:
        if "-f" in i:
            fruta = i.lower()
            resumen = fruta.replace("-f"," ")
            print(resumen)
        elif "-a" in i:
            animal = i.capitalize()
            resumen = animal.replace("-a"," ")
            print(resumen)
        elif "-p" in i:
            resumen = i.replace("-p"," ")
            persona = resumen.upper()
            print(persona)
    
funcion(list1)
'''


def magic(year:int, month:int, day:int):
    contador = 0
    mult = month*day
    if year-mult == 1900:
        print(f"el mes {month} dia {day} del {year} fue una fecha mágica")
    while year-mult == 1900:
        contador += 1
    print(contador)


for año in range(1900, 2000):
    for mes in range(1,13):
        for dia in range(1,30):
            magic(año,mes,dia)
        














    


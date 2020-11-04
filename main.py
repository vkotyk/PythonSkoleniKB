# print ("Hello World")

# promenna = "Hello World"
# print (promenna)

# pozdrav = 42
# print (pozdrav)

# input("Ahoj, jak se jmenuješ? ")
# print ("Těší mě")
# print (f'Aritmetický výraz: {2+2}')

# jmeno = input("Ahoj, jak se jmenuješ? \n")
# print (f'Těší\t mě {jmeno}')

# cislo = int(input("Zadejte prosím číslo:\n"))
# print (type(cislo))
# print (f'Číslo je {cislo+2}')

# cislo2 = input("Zadejte prosím číslo:\n")
# print (type(cislo2))
# print (f'Číslo je {cislo2+str(2)}')

# hledane_cislo = 42
# cislo = int(input("Řekni prosím číslo:\n"))

# if hledane_cislo == cislo:
#     print("Číslo bylo uhodnuto.")
#     print("Ahoj!")
# print ("Po ifu. Neuhodl jsi!")

# poptavane_cislo = 42
# cislo2 = int(input("Řekni prosím číslo:\n"))

# if poptavane_cislo == cislo2:
#     print("Číslo bylo uhodnuto.")
# else:
#     print("Číslo uhodnuto nebylo.")

# vyhledavane_cislo = 42
# cislo3 = int(input("Řekni prosím číslo:\n"))

# if vyhledavane_cislo == cislo3:
#     print("Číslo bylo uhodnuto.")
# elif vyhledavane_cislo < cislo3:
#   print("Tipnuté číslo bylo větší než číslo hádané.")
# else:
#   print("Číslo uhodnuto nebylo.")

# hledam_cislo = 42
# uhodnuto = False

# while not uhodnuto:
#   cislo = int(input("Řekni prosím číslo:\n"))

#   if hledam_cislo == cislo:
#     print ("Číslo bylo uhodnuto.")
#     uhodnuto = True
#     break
#   elif hledam_cislo < cislo:
#     print("Tipnuté číslo bylo větší než číslo hádané.")
#   else:
#     print("Tipnuté číslo bylo menší než číslo hádané.")
# print("po whilu")

# for cislo3 in range(5):
#     print(cislo3)

# hledane_cislo = 42
# uhodnuto = False

# for iterace in range (3):
#   print(f"Začátek kola {iterace + 1}")
#   cislo = int(input("Řekni prosím číslo:\n"))

#   if hledane_cislo == cislo:
#     print ("Číslo bylo uhodnuto.")
#     uhodnuto = True
#     break
#   elif hledane_cislo < cislo:
#     print("Tipnuté číslo bylo větší než číslo hádané.")
#   else:
#     print("Tipnuté číslo bylo menší než číslo hádané.")
# print("po whilu")

# for cislo1 in range (2, 5):
#   print (cislo1)

# for cislo2 in range (100, 9, -7):
#   print (cislo2)

# prazdny_list = []
# plny_list = [1, "nějaký string", 3]
# print(prazdny_list)
# print(plny_list)

# plny_list = [1, "nějaký string", 3, [1,2,3]]
# plny_list.append(10000)
# print(plny_list)
# nova_promenna = plny_list[2]
# print(nova_promenna)

#POZOR - první element má index 0

# plny_list = [1, "nějaký string", 3, [1,2,3]]
# plny_list.append(10000)
# print(plny_list)
# nova_promenna = plny_list[-1]
# print(nova_promenna)

# hledane_cislo = 42
# uhodnuto = False
# tipnuta_cisla = []

# for iterace in range (3):
#   print(f"Začátek kola {iterace + 1}")
#   cislo = int(input("Řekni prosím číslo:\n"))
#   tipnuta_cisla.append(cislo)

#   if hledane_cislo == cislo:
#     print ("Číslo bylo uhodnuto.")
#     uhodnuto = True
#     break
#   elif hledane_cislo < cislo:
#     print("Tipnuté číslo bylo větší než číslo hádané.")
#   else:
#     print("Tipnuté číslo bylo menší než číslo hádané.")

# print(f"Uživatel tipoval následující čísla:{tipnuta_cisla}")
# if uhodnuto:
#     print("Hra byla vyhrána!")
# else:
#   print("Hra byla prohrána. :-( ")


# plny_list = [1, "nějaký string", 3, [1,2,3]]
# for index in range (len(plny_list)):
#   print(f"Index: {index}")
#   print(f"Hodnota list: {plny_list[index]}")

# plny_list = [1, "nějaký string", 3, [1,2,3]] 
# for index, hodnota in enumerate(plny_list):
#  print(f"Index: {index}")
#  print(f"Hodnota list: {hodnota}")

# plny_tuple = (1, "nějaký string", 3, [1,2,3])
# print (dir(plny_list))

# plny_slovnik = {"klic1": "hodnota1", "klic2": 42}
# print(plny_slovnik)
# plny_slovnik["klic3"] = 20000
# print(plny_slovnik)
# print(plny_slovnik.keys())
# print(plny_slovnik.values())

# import random

# hledane_cislo = random.randint (1,100)
# uhodnuto = False
# tipnuta_cisla = []

# for iterace in range (3):
#   print(f"Začátek kola {iterace + 1}")
#   cislo = int(input("Řekni prosím číslo:\n"))
#   tipnuta_cisla.append(cislo)

#   if hledane_cislo == cislo:
#     print ("Číslo bylo uhodnuto.")
#     uhodnuto = True
#     break
#   elif hledane_cislo < cislo:
#     print("Tipnuté číslo bylo větší než číslo hádané.")
#   else:
#     print("Tipnuté číslo bylo menší než číslo hádané.")

# print(f"Uživatel tipoval následující čísla: {tipnuta_cisla}")
# print(f"Hledané číslo bylo: {hledane_cislo}")
# if uhodnuto:
#     print("Hra byla vyhrána!")
# else:
#   print("Hra byla prohrána. :-( ")

# import random

# def vytiskni_mracouna():
#   print(":(")

# def vytiskni_smajlika():
#   print(":)")

# hledane_cislo = random.randint (1,100)
# uhodnuto = False
# tipnuta_cisla = []

# for iterace in range (3):
#   print(f"Začátek kola {iterace + 1}")
#   cislo = int(input("Řekni prosím číslo:\n"))
#   tipnuta_cisla.append(cislo)

#   if hledane_cislo == cislo:
#     print ("Číslo bylo uhodnuto.")
#     vytiskni_smajlika()
#     uhodnuto = True
#     break
#   elif hledane_cislo < cislo:
#     print("Tipnuté číslo bylo větší než číslo hádané.")
#     vytiskni_mracouna()
#   else:
#     print("Tipnuté číslo bylo menší než číslo hádané.")
#     vytiskni_mracouna()

# print(f"Uživatel tipoval následující čísla: {tipnuta_cisla}")
# print(f"Hledané číslo bylo: {hledane_cislo}")
# if uhodnuto:
#     print("Hra byla vyhrána! :) ")
# else:
#   print("Hra byla prohrána. :( ")


# import random

# def vytiskni_smajlika(nalada:bool)-> str:
#   # returns string - emoticon
#   # args: nalada(bool): happy = True, sad = False
#   #returns: str: emoticon

#   smajlik = ""

#   if nalada:
#     smajlik = ":)"
#   else:
#     smajlik = ":("

#   return smajlik

# hledane_cislo = random.randint (1,100)
# uhodnuto = False
# tipnuta_cisla = []

# for iterace in range (3):
#   print(f"Začátek kola {iterace + 1}")
#   cislo = int(input("Řekni prosím číslo:\n"))
#   tipnuta_cisla.append(cislo)

#   if hledane_cislo == cislo:
#     print ("Číslo bylo uhodnuto.")
#     print(vytiskni_smajlika(True))
#     uhodnuto = True
#     break
#   elif hledane_cislo < cislo:
#     print("Tipnuté číslo bylo větší než číslo hádané.")
#     print(vytiskni_smajlika(False))
#   else:
#     print("Tipnuté číslo bylo menší než číslo hádané.")
#     print(vytiskni_smajlika(False))

# print(f"Uživatel tipoval následující čísla: {tipnuta_cisla}")
# print(f"Hledané číslo bylo: {hledane_cislo}")
# if uhodnuto:
#     print("Hra byla vyhrána! :) ")
# else:
#   print("Hra byla prohrána. :( ")

with open("text.txt", "r") as soubor:
  obsah_souboru = soubor.read()
  print(obsah_souboru)
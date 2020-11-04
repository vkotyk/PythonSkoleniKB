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

hledam_cislo = 42
uhodnuto = False

while not uhodnuto:
  cislo = int(input("Řekni prosím číslo:\n"))

  if hledam_cislo == cislo:
    print ("Číslo bylo uhodnuto.")
    uhodnuto = True
    break
  elif hledam_cislo < cislo:
    print("Tipnuté číslo bylo větší než číslo hádané.")
  else:
    print("Tipnuté číslo bylo menší než číslo hádané.")
print("po whilu")


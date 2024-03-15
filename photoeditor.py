from PIL import Image
obrazek = Image.open("motorka.jpg")
sirka, vyska = obrazek.size
x = 0
#while x < sirka:
 #   y = 0
  #  while y < vyska:
   #     r, g, b = obrazek.getpixel((x,y))
    #    prumer = int((r+g+b)/3)
     #   obrazek.putpixel((x,y), (r , b, r))
        #if prumer > 150:
         #   obrazek.putpixel((x,y), (255, 255, 255))
        #else:
         #   obrazek.putpixel((x,y), (0, 0, 0))
     #   y += 1
   # x += 1



###def
def fialovy():
    while x < sirka:
     y = 0
     while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        obrazek.putpixel((x,y), (r , b, r))
        y += 1
    x += 1
    obrazek.show()

def cernobily():
    y=0
    r, g, b = obrazek.getpixel((x,y))
    prumer = int((r+g+b)/3)
    obrazek.putpixel((x,y), (r , b, r))
    if prumer > 150:
        obrazek.putpixel((x,y), (255, 255, 255))
    else:
        obrazek.putpixel((x,y), (0, 0, 0))
        obrazek.show()



# Menu
while True:
    print("\nVyberte si filtr.")
    print("1. Černobílý filtr")
    print("2. Fialový filtr")
    print("3. filtr")

    volba=input("Zvolte filtr pomocí čísla.")

    if volba == "1":
       cernobily()
    elif volba == "2":
       fialovy()
    elif volba == "3":
       print("ahoj")
    else:
       print("Neplatná volba. Zkus to znovu")

  
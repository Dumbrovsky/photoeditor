from PIL import Image
from filters import apply_filter

def display_menu():
    print("\nMenu")
    print("1. Černobílý filtr")
    print("2. Invert filtr")
    print("3. Červeno-modrý filtr")
    print("4. Konec")

def main():
    image_path = "/content/motorka.jpg"  # Fixed image path
    try:
        image = Image.open(image_path)
        while True:
            display_menu()
            choice = input("Zvolte filtr pomocí čísla: ")

            if choice == "1":
                filtered_image = apply_filter(image.copy(), 1)
                filtered_image.show()
            elif choice == "2":
                filtered_image = apply_filter(image.copy(), 2)
                filtered_image.show()
            elif choice == "3":
                filtered_image = apply_filter(image.copy(), 3)
                filtered_image.show()
            elif choice == "4":
                print("Program ukončen.")
                break
            else:
                print("Neplatná volba. Zkuste to znovu.")
        
    except FileNotFoundError:
        print("Soubor nebyl nalezen.")

if __name__ == "__main__":
    main()

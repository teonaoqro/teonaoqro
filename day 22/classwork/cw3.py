#3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები
num = int(input("enter number "))
i=0
while i < num:
    if i % 5 == 0:
        print(str(i)+" 5-ის ჯერადი")
    i = i + 1
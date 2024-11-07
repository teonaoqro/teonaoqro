#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვი და თან გვერძე მიუწერეთ ლუწია თუ კენტი

user_number = int(input("enter number "))

i = 0
while  i < user_number :
    if i % 2 == 0:
        print(str(i) + "is even")
    else:
        print(str(i) + "is odd")

    i = i + 1

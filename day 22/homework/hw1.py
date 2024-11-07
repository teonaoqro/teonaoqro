#  2) პითონში აქამდე რაც კი გვისწავლია ყველაფრის გამოყენებით გააკეთეთ მაქსიმალურად დახვეწილი რეგისტრაციის ფუნქციონალი, ეცადეთ რაც შეიძლება დახვეწოთ და გააუმჯობესოთ დაუმატოთ ბევრი ფუნქციონალები და ასე შემდეგ, აუცილებლად გამოიყენეთ ლუპები


print("registracion form..")

name=input("enter name: ")
surname=input("enter surname: ")
birthday=input("enter birthday: ")
email=input("enter your email: ")
number=input("enter number: ")

nickname=input("enter nickname: ")
a=0
password=input("enter password: ")
while password !="papirusi" and a != 3:
    password=input("reenter password!")
    a=a + 1
    if password == "papirusi":
        print("registracion complited")
    else:
        print("block your account!")

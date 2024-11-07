#1) შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც
 #bank account
print("new bank account")
print("please register!")
name=input("enter your name:")
password=input("enter your password:")
if input("reenter your password! ") == password:
     print("you are welcome!")
     print("1.transfer to someone")
     print("2.transfer to own account")
     print("3.exit")
     num=int(input("enter your operation number"))
     if num == 1:
         name=input("enter someone name")
         surname=input("enter  someone surname")
         money=int(input("enter how much money do you want to transfer"))
         print("tarnsfer complited!")
     elif num == 2:
              account=input("enter accout")
              money=input("how much money do you want to transfer")
              print("transfer complited!")
     elif num == 3:
          question=input("do you want exit?")
          if  question == ("yes"):
              print("good bay")
     else: print("you are welcome!"
                 "1.transfer to someone"
                 "2.transfer to own account"
                 "3.exit")
else:
     print("you cant anouther try!")

 



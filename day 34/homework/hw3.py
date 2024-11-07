#3) დაწერე ფუნქცია, რომელიც იღებს სახელს input()-ით და ბეჭდავს ამ სახელის სიმბოლოების რაოდენობას.
def name_len():
    name=input("enter name : ")
    for i in range(len(name)):
    
     print(len(name))

name_len()

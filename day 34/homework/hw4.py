#4) დაწერე ფუნქცია, რომელიც input()-ით იღებს ორ რიცხვს და ბეჭდავს, რომელია დიდი.
def bigger_number():
    num1=int(input("enter num1 :"))
    num2=int(input("enter num2 :"))
    if num1 > num2:
      print(num1)
    elif num2 > num1:
      print(num2)
    else:
      print("nothing")    

bigger_number()
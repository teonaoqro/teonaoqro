#6)  დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და გამოიყვანს თითოეულს კვადრატში აყვანილს.

   
def square_numbers():
     list=[2,4,6,9,12]
     for i in range(len(list)):
          square=(list[i]) ** 2
          print(square)
square_numbers()
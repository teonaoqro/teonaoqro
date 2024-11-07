# 3) შექმენით თავდაპირველად ცარიელი სია მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი 1-დან ამ რიცხვამდე დაამატეთ ყველა რიცხვი სიაში გამოიყენეთ for loop და append
list=[]
number=(int(input("enter number: ")))
for i in range(1,number):
    list.append(i)
print(list)

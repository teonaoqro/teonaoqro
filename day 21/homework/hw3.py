# 3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაითვალეთ მომხმარებლის შემოტანილ რიცხვამდე რიცხვების საშუალო არითმეტიკული

num=int(input("enter number"))
sum=0
for i in range(1,num+1,1):
    sum = sum + i
    averidge= sum / num+1
print(averidge)
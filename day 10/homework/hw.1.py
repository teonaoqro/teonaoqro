#1) ისწავლეთ random-ი პითონში(ბიბლოეთეკა)


import random
#როდესაც ვიყენებთ random ბიბლიოთეკას,ვქმნით ცვლადს my_list და ცვლადის მნიშვნელობად ვუთითებთ ჩამონათვალს("banana" , "apple" , "melon") შემდეგ print ფუნქცით კომპიუტერი ირჩევს ჩამონათვალიდან ერთ ერთს რენდომულად/შემთხვევითობის პრინციპით.პრინთ ფუნქციის შემდეგ random.choice დაწერა აუცილებელია prinT ფუნქციის სწორი მუშაობისთვის/კოდის სწორად გასაშვებად.
#მაგალითი 1.

my_list = ("banana" , "apple" , "melon")
print(random.choice(my_list))


#random ბიბლიოთეკაში თუ ცვლადის მნიშვნელობად ვუთითებთ ჩამონათვალში ერთ სიტყვას,მაშინ კომპიუტერი print ფუნქციის გამოყენებით ირჩევს ამ სიტყვიდან ასოებს რენდომულად/შემთხვევითობის პრინციპით.
#მაგალითი 2.

x = ("teona")
print(random.choice(x))

#მაგალითი 3.
 
school_items=("Pencil" ,  "ruler" ,  "notebook" ,  "eraser"  ,  "pen")
print(random.choice(school_items))

#მაგალითი 4.

year=(2000,2024,2050)
print(random.choice(year))


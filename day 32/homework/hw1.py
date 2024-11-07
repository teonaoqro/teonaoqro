#1) 1) შექმენით რიცხვებით სავსე სია, შემდეგ დაწერეთ კოდი რომელიც დაბეჭდავს ამ სიიდან ყველაზე უდიდეს რიცხვს გამოგადგებათ for loop ი კარგად დაფიქრდით და გაიაზრეთ.

number_list = [19, 3, 56, 22, 1, 23, 58]

for i in range(len(number_list)):
    largest_number = number_list[i]
    if i > largest_number:
        largest_number = i
print(largest_number)



#2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უდიდესი რიცხვი ამ სიიდან

numbers=[3,5,45,222,12,34,56]
def largest_num(numbers_list):
    max_number  = numbers_list[0]
    for i in range(len(numbers_list)):
        if max_number < numbers_list[i]:
            max_number = numbers_list[i]
    return max_number
print(largest_num(numbers))
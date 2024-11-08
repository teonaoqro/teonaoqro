#3) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ფუნქციამ უნდა დააბრუნოს უმცირესი რიცხვი ამ სიიდან
numbers=[12,45,36,333,78,98,100]
def smallest_number(numbers_list):
    min_number  = numbers_list[0]
    for i in range(len(numbers_list)):
        if min_number > numbers_list[i]:
            min_number = numbers_list[i]
    return min_number
print(smallest_number(numbers))
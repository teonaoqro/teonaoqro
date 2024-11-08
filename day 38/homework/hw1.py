#1) შექმენით კალკულატორის ფუნქცია რომელსაც ექნება სამი პარამეტრი პირველი რიცხვი, მეორე რიცხვი და მოქმედება თუ რა მოქმედება უნდა რომ შესრულდეს ამ ორ რიცხვს შორის რიცხვებიდან და მათემატიკური ოპერატორიდან გამომდინარე დაგიბრუნოთ პასუხი, თუ მაგალითად მომხმარებელამ შემოიტანა 5 და 10 ხოლო მას უნდა ამ ორი რიცხვის დამატება ანუ მესამე პარამეტრი არის "+" პლიუსი ეს ორი რიცხვი შეიკრიბოს 5 + 10 = 15


def calculator(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    elif action == '/':
        if num2 != 0:
            return num1 / num2
    else:
        return "Error: Invalid operator"
print(calculator(3,6,"+"))
print(calculator(44,6,"-"))
print(calculator(222,333,"*"))
print(calculator(123,45,"/"))

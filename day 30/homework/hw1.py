#1) შექმენით სია რომელშიც იქნება მინიმუმ 10 სახელი შემდეგ ამ სიიდან ამოშალეთ ისეთი სახელები რომლის სიგრძეც იქნება 10ზე მეტი და დააბრუნეთ გაფილტრული სია გამოიყენეთ for loop და ნასწავლი ფუნქციები
name_list=["charlotte","cametron","mia","lyra","cameron","elizabet","iosefa","nathaniel","christianoo","ameli"]
name_list1=[]
for i in range(len(name_list)):
    if len(name_list[i]) < 10:
        name_list1.append(name_list[i])
        print(name_list1)
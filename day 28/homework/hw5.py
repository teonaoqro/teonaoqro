#     5) შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 20 ზე მეტი რიცხვები ისე რომ იყოს თან სამის ჯერადი გამოიყენეთ for loop
number_list=[12,24,39,5,21,35,7,12,27,11,18,22,30,42,16,23,29,5,49,38]
for number_list in number_list:
    if number_list > 20 and number_list % 3 == 0:
        print(number_list)
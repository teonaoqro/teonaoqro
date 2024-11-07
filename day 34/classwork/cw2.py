#2) შექმენით ფუნქცია რომელიც მომხმარებელს ეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი
def number_is_even():
   num=int(input("enter num"))
   if num % 2 == 0:
      print("is even")
   else:
      print("is odd")

number_is_even()
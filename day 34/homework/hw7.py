#7) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.
def even_number():
    number=int(input("enter number :"))
    if number % 2 == 0:
       print("true")
    else:
       print("false")

even_number()
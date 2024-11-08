#4) მომხმარებელს შეეკითხეთ სახელი შემდეგ შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ მომხმარებლის სახელს შემდეგ კი დააბრუნეთ მომხმარებლის სახელის პირველი ასო მერამდენეა ანბანში
name=input("enter your name: ")
alphabet=["a","b","c","d","i","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","d","x","y","z"]
def first_letter(name):
  letter = name[0]
  for i in range(len(alphabet)):
    if letter == alphabet[i]:
      return int(alphabet.index(letter)) + 1
print(first_letter(name))

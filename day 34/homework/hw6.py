#6) დაწერე ფუნქცია, რომელიც input()-ით იღებს ტემპერატურას ცელსიუსში და ბეჭდავს ფარენჰეიტში გადაყვანილ მნიშვნელობას.
def celsius_to_Fahrenheit():
    celsius=int(input("enter celsius number :"))
    F = celsius * 9/5 + 32
    print(F)

celsius_to_Fahrenheit()
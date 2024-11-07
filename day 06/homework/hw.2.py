# 2.ახსენით კომენტარებით რა არის case-sensitive language და გააკეთეთ მაგალითიც
#case-sensitive language ნიშნავს ასოების მიმართ მგრძნობიარე,ანუ დიდი და პატარა ასოები ძალიან განსხვავდებიან ერთმანეთისგან.

name="teona "
surname="oqropilashvili"
print(Name + surname)

#შეცდომაა,რადგან print ფუნქციისთვის გადაცემული გვაქვს name ცვლადი დიდი ასოთი(Name)რადგან პითონი case-sensitive ენაა ის არ იცნობს ცვლადს სახელად Name,მისთვის ცნობლია ცვლადი სახელად name

#სწორია


name="teona "
surname="oqropilashvili"
print(name + surname)






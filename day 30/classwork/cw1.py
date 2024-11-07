#1. შექმენით მენტორების სახელების სია და ჩვეულებრივი სახელებისთვის განკუთვნილი სია შემდეგ მომხმარებელს შემოატანინეთ სახელი თუ ეს სახელი იქნება რომელიმე მენტორის სახელი ამ შემთხვევაში ეს სახელი დაემატოს მენტორებისთვის განკუთვნილ სიაში სხვა შემთხვევაში თუარიქნება ეს სახელი მენტორის სახელი დაემატოს ჩვეულებრივი სახელების სიაში შემდეგ კი ორივე დაბეჭდეთ
mentor_list=["gabrieli","daviti","luka","zuka"]
name_list=["mariami","erekle","vano","nikolozi"]
name=input("enter name :")
if name == "gabrieli" or "luka" or "zuka" or "daviti":
    mentor_list.append(name)
else:
    name_list.append(name)

print(mentor_list)
print(name_list)
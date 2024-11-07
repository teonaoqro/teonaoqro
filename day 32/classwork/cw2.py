#2) შექმენით სია სადაც იქნება 10 სახელი შემდეგ ამ სიიდან ამოშლით ყველა იმ სახელს რომელიც იწყება ა ასოზე და დაბეჭდეთ გაფილტრული სია
name_list=["avtandili","erekle","saba","gabrieli","aleqsandre","luka","ioane","lado","kaxaberi","anuki"]
name_start=[]
for i in range(len(name_list)):
    if name_list[i][0] != "a":
        name_start.append(name_list[i])

print(name_start)
        

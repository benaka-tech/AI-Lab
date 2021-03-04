import random 
print("Welcome to Table arrangement system!!!!!!!!!!!!!!")
number=int(input("Enter the no of people"))
lists=int(input("Enter no of people can't sit with each other for social reasons"))
table=input("Enter no of Tables");
print("You have enterted");
print("People=",number);
print("people can't sit with each other for social reasons=",lists)
print("No of Tables",table) 

people = random.sample(range(0, number), number)
listLen=2
value=int(lists/listLen)
print(value)
nosit =[random.sample(range(0, lists), listLen) for _ in range(value)]


print(nosit)
print(people)

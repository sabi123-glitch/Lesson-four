Amount = int(input("Please enter the amount for withdraw :"))

Note_1 = Amount//100
Note_2 = (Amount%100)//50
Note_3 = ((Amount%100)%50)//10

print("notes of 100 dollars", Note_1)
print("Notes of 50 dollars", Note_2)
print("notes of 10 dollars", Note_3)





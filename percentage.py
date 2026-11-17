print ("Enter marks obtained in four subjects")
maths = int(input("maths : "))
English = int(input("english : "))
science = int(input("science : "))
pe = int(input("pe : "))

sum = (maths+English+science+pe)
print ("The sum of the marks is", sum)
percentage = (sum/400)*100
print ("the percentage is", percentage)

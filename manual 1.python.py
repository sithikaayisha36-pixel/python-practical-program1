#student Marks,percentage and grade
name= input("Enter a student name:")
n=int (input("enter number of subjects:"))
total = 0
for i in range(1,n+1):
   mark= float(input("enter markk for subject{i}:"))
   total+=mark
percentage = total/n
if percentage>=90:
    grade="A"
    performance="excellent"   
elif percentage>=80:
    grade="B"   
    performance="very good"
elif percentage>=60:
    grade="C" 
    performance ="average"  
else:
    grade="F"   
    performance="needs improvement"

    print("Acadamic performance")   
    print("student name:",name)
    print("total marks:",total)
    print("percentage:",round(percentage,2),"%")
    print("grade:",grade)
    print("performance:",performance)

name = str(input("please enter your name:"))
lastname = str(input("please enter your last name:"))
age = int(input("please enter your age:"))
year = int(input("please enter your data of birth (just year):"))

veriler = list([name,lastname,age,year])

for veri in veriler: #verilerin içindeki değerleri sırayla veriye aktarmaya yarar.
    print(veri)

if age < 18:
    print("You can't go out because it's too dangerous")
elif age >= 18:
    print("You can go out to street")
  


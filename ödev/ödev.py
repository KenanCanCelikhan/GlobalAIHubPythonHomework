name =str(input("What is your name?")) 
surname =str(input("What is your surname?"))
age =int(input("How old are you?")) 
weight = float(input("What is your weight?"))
live = bool(input("do you like your job?")) 

a=type(name)
b=type(surname)
c=type(age)
d=type(weight)
e=type(live)

metin=f"name {name},surname {surname},age {age}, weight {weight}, like {live}"

metin2=f"name type {a},surname type {b},age type{c},weight type{d},live type{e}"

print(metin)
print(metin2)

students_log=[{"name": "Benjamin","age": 12,"hobbies": ["dancing", "singing", "tennis"]},{"name": "Glory","age": 9, "hobbies": ["reading", "running", "piano"]}]
my_dict = {}
def add ():
    n=str(input("Enter your name"))
    age=int(input("Enter your age"))
    hobbies=str(input(("Enter your hobbies")))
    my_dict ["name"] = n
    my_dict ["age"] = age
    my_dict ["hobbies"] = hobbies
add ()
students_log.append(my_dict)
print(students_log)

#Dictionary Keys	for k in dict:
#Dictionary Values	for v in dict.values():
#Key + Value	for k,v in dict.items():

students = {
    "student1": {
        "name": "Ram",
        "marks": 80
    },
    "student2": {
        "name": "Sita",
        "marks": 90
    }
}

for student, info in students.items(): # we can use .items() to get both the key and value of the dictionary
    print(student)
# we can use .items() to get both the key 
#and value of the dictionary  and we used this for k,v in dict.items():
    for key, value in info.items(): 
        
        print(key, value)
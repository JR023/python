from turtle import update


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = {'x': 10, 'y': 20} 
w=  {'y':30}
#change 10 to 15
x[1][0]=15
print(x)
print('===')
#change Jordan to Bryant
students[0]['last_name']='Bryant'
print(students)
print('===')
#change Messi to Andres
sports_directory['soccer']=['Andres','Ronaldo', 'Rooney']
print(sports_directory)
print('===')
#change 20 to 30
z.update(w)
print(z)
print('===')
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
def iterateDictionary (some_list):
    for iterate in range(len(students)):
        for key in students[iterate]:
            print(students[iterate][key])
    print('===')
iterateDictionary(students)
#get values from dictionary
def iterateDictionary2 (key_name,some_list):
    for iterate2 in some_list:
        print (iterate2[key_name])
    print('===')
iterateDictionary2 ('first_name', students)
#prints the name of each key along with the size of its list, and then prints the associated values within each key's list
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS")
    for location in some_dict['locations']:
        print(location)
    print("")
    print(len(some_dict['instructors']), "INSTRUCTORS")
    for instructor in some_dict['instructors']:
        print(instructor)
printInfo(dojo)
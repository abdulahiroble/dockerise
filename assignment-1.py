from datetime import datetime

BoardOfDirectors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}

management = {"Benny", "Trunte", "Rane"}

employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

notEmployee = BoardOfDirectors.intersection(employees)

# 1.1 
print("Directors who is not an employee:", BoardOfDirectors - employees)


# 1.2 
isEmployee = BoardOfDirectors.intersection(employees)
print("Directors who is also an employee:", isEmployee)

# 1.3 
boardMember = BoardOfDirectors.intersection(management)
print("Member of the borad:", len(boardMember))

# 1.4
print("All members of the management also an employee:", management.issubset(employees))

# 1.5 
print("All members of the management also in the board:", BoardOfDirectors.issubset(management))

# 1.6
fullMember = BoardOfDirectors.intersection(management, employees)
print("Who is an employee, member of the management, and a member of the board?:", fullMember)

# 1.7
onlyEmployee = employees.difference(management, BoardOfDirectors)
print(onlyEmployee)


#################################################################################################

# 2.0

tuple1 = ("Alpha", "Beta", "Gamma")
print("MyTuple:", tuple1)


################################################################################################

# 3.0

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# 3.1
print("Union:", set1.union(set2))

# 3.2
print("Symmetric difference:", set1.symmetric_difference(set2))

# 3.3
print("Difference:", set1.difference(set2))

# 3.4
print("Disjoint:", set1.isdisjoint(set2))

#############################################################################################

# 4.0

datetime_str = '8 Mar 85'

def myFunction():
    datetime_object = datetime.strptime(datetime_str, '%d %b %y')

    newly_formatted_string = datetime_object.strftime("%d/%m/%Y")

    tup = (newly_formatted_string.replace("/", "-"))

    print(tup)

myFunction()

#####################
# 2.2.6 Challenge 1
#####################

def changeschooltype():
    return "High"

def printschooltype(school):
    if school == "Elementary":
        # use "pass" statement when a statement is required syntatically
        # but you do not want any code to execute
        pass
    elif school == "Senior":
        school = changeschooltype() # call function changeschooltype()
    else:
        school = "Unknown"
    print school
    return school

# put three schools into a list
schools = ["Elementary","Senior",""]

# create an empty list for modified schools
new_schools = []

# look through school list
for school in schools:
    new_school = printschooltype(school) # call function printschooltype()
    new_schools.append(new_school) # use list method "append" to add element to the list

# print school list
print schools
print new_schools

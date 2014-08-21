#####################
# 2.2.6 Challenge 1
#####################

def changeschooltype():
    return "High"

def printschooltype(school):
    if school == "Elementary":
        print school
    elif school == "Senior":
        school = changeschooltype() # call function changeschooltype()
        print school
    else:
        print "Unknown"

# put three schools into a list
schools = ["Elementary","Senior",""]

# look through school list
for school in schools:
    printschooltype(school) # call function printschooltype()

# print modified school list
print schools

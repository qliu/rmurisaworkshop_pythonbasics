#####################
# 2.2.6 Challenge 1
#####################

# put three schools into a list
schools = ["Elementary","Senior",""]

# look through school list
for school in schools:
    if school == "Elementary":
        print school
    elif school == "Senior":
        school = "High"
        print school
    else:
        print "Unknown"

# print modified school list
print schools

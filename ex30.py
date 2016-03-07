people = 30
cars = 20
trucks = 10

if cars > people:
    print "we should take the cars."
elif cars < people:
    print "We should not take the cars"
else:
    print "We cant decide"

if trucks > cars:
    print "Thats too many trucks"
elif trucks < cars:
    print "Maybe we could take the trucks"
else:
    print "We still can't decide"

if people > trucks:
    print "Alright lets just take the trucks."
else:
    print "Fine, lets stay home then"

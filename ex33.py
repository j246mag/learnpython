

def loop(user_limit):
    i = 0
    numbers = []

    while i < user_limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

limit = int(raw_input("> "))

loop(limit)


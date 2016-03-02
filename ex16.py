from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you o want that, hit RETURN"

raw_input("?")
print "Opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = target.write(raw_input("line 1: "))
target.write("\n")
line2 = target.write(raw_input("line 2: "))
target.write("\n")
line3 = target.write(raw_input("line 3: "))
target.write("\n")

print "I'm going to write these to the file."

print "And finally, we close it"
target.close()


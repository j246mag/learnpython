
my_name = 'Johannes Magnusson'
my_age = 30 # not a lie
my_height = 178 # centimeters
my_weight = 80 # kg
my_eyes = 'Gray'
my_teeth = 'White'
my_hair = 'Brown'
my_weight_in_pounds = my_weight / 0.45359237
my_height_in_inches = my_height * 0.393700787

print "Let's talk about %s." % my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy" % my_weight
print "Actually that's not too heavy."
print "He's hot %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# tricky line coming up
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "I weigh %s pounds" % my_weight_in_pounds
print "I am %s inches tall" % my_height_in_inches
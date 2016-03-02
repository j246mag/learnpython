from sys import argv

script, user_name = argv
input = ': '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(input)

print "Where do you live %s?" % user_name
lives = raw_input(input)

print "What kind of computer do you have?"
computer = raw_input(input)

print """
Alright, so you said %r about liking me.
And you lin in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


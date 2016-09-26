name = 'Eugene Kadish'
age = 47 # not a lie
height = 68 # inches
weight = 165 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

inch_to_centimeter = 2.54 / 1
lbs_to_kilograms = 0.453592 / 1

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "%s lbs is" % weight, weight * lbs_to_kilograms, "kilograms."
print "%s inches is" % height, height * inch_to_centimeter, "centimeters."
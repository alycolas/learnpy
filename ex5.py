aly_name = 'Lee jingxin'
aly_age = 28 # not a lie
aly_height = 74 # inches
aly_weight = 180 # lbs
aly_eyes = 'Blue'
aly_teeth = 'White'
aly_hair = 'Brown'

print "Let`s talk about %s." % aly_name
print "He`s %d inches tall." % aly_height
print "He`s %d pounds heavy." % aly_weight
print "Actually that`s not too heavy."
print "He`s got %s eyes and %s hair." % (aly_eyes, aly_hair)
print "His teeth are usually %s depending on the coffee." % aly_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	aly_age, aly_height, aly_weight, aly_age + aly_height + aly_weight)

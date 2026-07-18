# string interpolation using concatenation
arms = 2
fingers = 10
print("I have " + str(arms) + " arms and " + str(fingers) + " fingers.")
# I have 2 arms and 10 fingers.

# string interpolation using ,
verb = "jumps"
adjective = "lazy"
print("The brown dog ", verb, " over the ", adjective, " fox.")
# The brown dog  jumps  over the  lazy  fox.

# change adjective
verb = "jumps"
adjective = 5
print("The brown dog ", verb, " over the ", adjective, " fox.")
# The brown dog  jumps  over the  5  fox.

# string interpolation using .format()
var1 = "today"
var2 = "luckiest"
print("Yet {} I consider myself the {} man on the face of this earth.".format(var1, var2))
# Yet today I consider myself the luckiest man on the face of this earth.

# variation 1: change var2
var1 = "today"
var2 = True
print("Yet {} I consider myself the {} man on the face of this earth.".format(var2, var1))
# Yet True I consider myself the today man on the face of this earth.

# variation 2: change order of variables
var1 = "today"
var2 = "luckiest"
print("Yet {} I consider myself the {} man on the face of this earth.".format(var2, var1))
# Yet luckiest I consider myself the today man on the face of this earth.

# variation 3: add index to {}
var1 = "today"
var2 = "luckiest"
print("Yet {1} I consider myself the {0} man on the face of this earth.".format(var1, var2))
# Yet luckiest I consider myself the today man on the face of this earth.

# string interpolation using f-string
var1 = "Up"
var2 = "away"
my_string = f"{var1}, up and {var2}."
print(my_string)
# Up, up and away.

# change var1 to int and change {var1} value
var1 = 7
var2 = "away"
my_string = f"{var1 + 10}, up and {var2}."
print(my_string)
# 17, up and away.

# multi-line f-strings
name = "Calvin"
age = 6
occupation = "student"
sentence = f"My name is {name}. " \
           f"I am {age} years old. " \
           f"I am a {occupation}."
print(sentence)
# My name is Calvin. I am 6 years old. I am a student.

# formatting strings with %
var1 = "Up"
var2 = "away"
print("%s, up and %s" % (var1, var2))
# Up, up and away

# variation 1: change var1 to int
var1 = 7
var2 = "away"
print("%s, up and %i" % (var2, var1))
# away, up and 7

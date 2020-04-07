# We often only want certain code to execute when a particular condition has been met.
# For ex: if my dog is hungary (Some condition), then i will feed the dog (Some action)
# Control Flow syntax makes use of colons and indentation (Whitesoace)
# This indentation system is crucial to python and is what sets it apart from other programming languages
# Syntax
#if some_condition:
#   execute some code
#elif some_other_condition:
#   do something different
#else:
#   do something else

name = "manpreet"

if name == "sunita":
    print("Hello Sunita")
elif name == "manpreet":
    print("Hello manpreet")
elif name == "krishna":
    print("Hello krishna")
else:
    print("Please tell us what's your name")

print("*"*8)

name = "sam"

if name == "sunita":
    print("Hello Sunita")
elif name == "manpreet":
    print("Hello manpreet")
elif name == "krishna":
    print("Hello krishna")
else:
    print("Please tell us what's your name")
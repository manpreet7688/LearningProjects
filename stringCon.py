# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)

a = "Sam"

# If i have to change it into Pam
print(a)
a = a[1:]
print(a)
a= "P" + a
print(a)

newVar = "Hello World"
print(newVar)
print(newVar.count(newVar))
print(newVar.replace('l','n'))
print(newVar.upper())
print(newVar.lower())
print(newVar.capitalize())
print(newVar.split())
print(newVar.split('l'))
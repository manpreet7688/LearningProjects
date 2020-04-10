class CatCategory():

    # Class Object Attribute
    # Same for any instance of class
    species = 'mammal'
    # Define a constructor of the class CatCategory
    def __init__(self,cat_name,cat_breed,is_available):
        # Here self means it belongs to this class
        self.my_cat = cat_name
        self.my_cat_breed = cat_breed
        self.spot = is_available

catcategory_instance = CatCategory(cat_name='Sussie', cat_breed='unknown',is_available='Yes')
#Shows the class attributes when type .
print(catcategory_instance.my_cat)
print(catcategory_instance.my_cat_breed)
print(catcategory_instance.spot)
# Printing class object instance, we dont need to paas this attribute
print(catcategory_instance.species)

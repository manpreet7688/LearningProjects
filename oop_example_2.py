class TravelRoutine():

    jul_aug = "New York"
    rest = 'Stay in Home'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def jan_march(self,place_name):
        print("From jan to march, {} whose age is {} will travel to {}".format(self.name,self.age,place_name))

    def april_june(self,place_name):
        print("From april to june, {} whose age is {} will travel to {}".format(self.name, self.age, place_name))

    def july_aug(self):
        print("From july to aug, {} whose age is {} will travel in {}".format(self.name, self.age, TravelRoutine.jul_aug))

    def rest_of_the_year(self):
        print("Rest of the year, {} whose age is {} will {}".format(self.name, self.age, TravelRoutine.rest))

travel_diary = TravelRoutine('manpreet', 28)
travel_diary.jan_march('London')
travel_diary.april_june('Germany')
travel_diary.july_aug()
travel_diary.rest_of_the_year()
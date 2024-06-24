from Contollers.FoodManager import FoodManager
class MainMenu:
    __Options={1:"Show Restaurants",2:"Show FoodItems",3:"Search Restaurant",4:"Search FoodItem",5:"Logout"}
    def ShowRestaurants(self):
        for res in self.__FoodManager.Restaurants:
            print(f">> {res.Name}=>Rating:{res.Rating}")
        choice=int(input("Please Select the Restaurant : "))

    def ShowFoodItems(self):
        pass
    def SearchRestaurant(self):
        pass
    def SearchFoodItem(self):
        pass
    def Logout(self):
        pass

    def __init__(self):
        self.__FoodManager=FoodManager()
    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f"{option}.{MainMenu.__Options[option]}",end=" ")
            print()
            try:
                choice=int(input("Please enter your Choice : "))
                value=MainMenu.__Options[choice].replace(" ","")
                getattr(self,value)()
            except (ValueError,KeyError):
                print("Invalid input..Please Enter the Valid Choice")



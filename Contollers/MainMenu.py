from Contollers.FoodManager import FoodManager
from Models.Cart import Cart
class MainMenu:
    __Options={1:"Show Restaurants",2:"Show FoodItems",3:"Search Restaurant",4:"Search FoodItem",5:"Logout"}
    def ShowRestaurants(self):
        for i,res in enumerate(self.__FoodManager.Restaurants,1):
            res.DisplayItem(i)
            # print(f">> {res.Name}=>Rating:{res.Rating}")
        choice=int(input("Please Select the Restaurant : "))
        res=self.__FoodManager.Restaurants[choice]
        self.ShowFoodMenus(res.FoodMenus)

    def ShowFoodItems(self,foodItems=None):
        if foodItems is not None:
            for i,foodItem in enumerate(foodItems,1):
                foodItem.DisplayItem(1)
            choices=list(map(int,input("Please choose your Food item (eg 1,2) : ").split(',')))
            cart=Cart(foodItems,choices)
        else:
            pass


    def SearchRestaurant(self):
        resName=input("Enter Restaurant Name : ")
        res=self.__FoodManager.FindRestaurant(resName)
        if res is not None:
            print("Restaurant Found...")
            print(f"Name : {res.Name},Rating : {res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No Restaurant found on the name {resName}")
    def SearchFoodItem(self,foodItems):
        self.ShowFoodItems(foodItems)

    def ShowFoodMenus(self,menus):
        print("\nList of Menus Available : ")
        for i,menu in enumerate(menus,1):
            menu.DisplayItem(i)
            #print(f"{i} => {menu.Name}")
        choice=int(input("Please enter Menu : "))-1
        foodItems=menus[choice-1].FoodItems
        self.SearchFoodItem(foodItems)
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
a=MainMenu()
a.Start()
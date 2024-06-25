from Models.FoodMenu import FoodMenu
from Models.FoodItem import FoodItem
from Models.Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants=self.__PrepareRestaurants()
    def __PrepareFoodItems(self):
        item1=FoodItem("Veg-Biriyani",4,150,"****")
        item2 = FoodItem("Chicken-Biriyani", 4.2, 180, "*****")
        item3 = FoodItem("Mutton-Biriyani", 4.5, 200, "****")
        return [item1,item2,item3]

    def __PrepareFoodMenus(self):
        FoodItems=self.__PrepareFoodItems()
        menu1=FoodMenu("Veg")
        menu1.FoodItems=[FoodItems[0]]
        menu2 = FoodMenu("Non-Veg")
        menu2.FoodItems = [FoodItems[1],FoodItems[2]]
        return [menu1,menu2]

    def __PrepareRestaurants(self):
        FoodMenus=self.__PrepareFoodMenus()
        res1=Restaurant("A2b",5,"Chennai",10)
        res1.FoodMenus=[FoodMenus[0]]
        res2 = Restaurant("MuniyandiVilas", 5, "Bangalore", 20)
        res2.FoodMenus = [FoodMenus[0],FoodMenus[1]]
        res3 = Restaurant("KFC", 5,"Chennai", 15)
        res3.FoodMenus = [FoodMenus[0], FoodMenus[1]]
        return [res1,res2,res3]
    def FindRestaurant(self,name):
        for res in self.Restaurants:
            if res.Name == name:
                return res








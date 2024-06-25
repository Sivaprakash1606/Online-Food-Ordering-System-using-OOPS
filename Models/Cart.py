class Cart:
    def __init__(self,items,choices):
        self.Choices = choices
        self.FoodItems=self.__AddtoCart(items)


    def __AddtoCart(self,items):
        foodDic={}
        for choice in self.Choices:
            if choice>len(items):
                raise KeyError
            if choice in foodDic:
                foodDic[choice]+=1
            else:
                foodDic[choice]=1
        return foodDic

    def ProcessOrder(self,fooditems):
        Total=0
        for item in self.FoodItems:
            price=self.FoodItems[item]*fooditems[item-1].Price
            Total+=price
            print(f"{fooditems[item-1].Name} x {self.FoodItems[item]}={price}")
        print(f"Total :{Total}")
        print("*** Sucessfully order would placed... Thank you ***")






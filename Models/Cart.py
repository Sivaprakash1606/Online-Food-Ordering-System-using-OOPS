class Cart:
    def __init__(self,items,choices):
        self.Choices = choices
        self.FoodItems=items=self.AddtoCart(items)


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

    def ProcessOrder(self):
        pass





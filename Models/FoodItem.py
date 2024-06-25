from Models.AbstractItem import AbstractItem
class FoodItem(AbstractItem):
    def __init__(self,name,rating,price,description):
        super().__init__(name,rating)
        self.Price=price
        self.Description=description

    def DisplayItem(self,start):
        print(f"{start} => Name: {self.Name} Price : {self.Price} Rating : {self.Rating}")

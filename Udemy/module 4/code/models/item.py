class ItemModal():
    """
    Modal used for creating items in the database.
    """
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def json(self):
        return {"name":self.name,"price":self.price}
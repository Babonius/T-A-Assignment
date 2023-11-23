class House:

    total_houses = 0

    def __init__ (self,floors,doors,windows,color,has_garage,adress):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.adress = adress

        House.total_houses += 1
    
    def display_info(self):
        print("House information: ")
        print(f"        -Adress: {self.adress}")
        print(f"        -floors: {self.floors}")
        print(f"        -doors: {self.doors}")
        print(f"        -windows: {self.windows}")
        print(f"        -color: {self.color}")
        print(f"        -garage: {self.has_garage}")
    
    @classmethod
    def display_total_houses(cls):
        print(f"Total number of houses: {cls.total_houses}")

    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False #not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False  # floors, doors, windows should be positive int
    
        return True

    def color_house(self):
        new_color = str(input("Please input a new color: "))
        self.color = new_color

        return self.color

    def adress_house(self):
        new_adress = str(input("Please input a new adress: "))
        self.adress = new_adress
        return self.adress
    
    def garage_house(self):
        if self.has_garage == True :
            print("Garage existed")
        else:
            print("Garage added")
            self.has_garage = True

        return self.has_garage


house1 = House(floors = 2, doors = 3, windows = 6, color = "Blue", has_garage = True, adress = "123 Main St")
house2 = House(floors = 1, doors = 2, windows = 4, color = "Red", has_garage = False,adress = "123 Main St")

house1.display_info()
print("\n")
house2.display_info()
print("\n")
print("\n")
House.display_total_houses()
print("\n")
validation_result1 = House.validate_house(house1)
print(f"House Validation Result: {'Valid' if validation_result1 else'Invalid'}")

house1.color_house()
house1.display_info()
print()

house1.garage_house()
print()

house2.garage_house()
house2.display_info()
print()

house2.adress_house()
house2.display_info()
print()
#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def cobble(self, condition="None"):
        print("Your shoe is as good as new")
        self.condition = "New"


    def get_brand(self):
        print("Retrieving brand")
        return self._brand
    
    def set_brand(self, brand):
        if type(brand) == str and len(brand) >0:
            print(f"Setting brand to {brand}")
            self._brand = brand

    brand = property(get_brand, set_brand)

    def get_size(self):
        print("Retrieving size")
        return self._size
    
    def set_size(self, size):
        if type(size) == int:
            print(f"Setting size to {size}")
            self._size = size

    size = property(get_size, set_size)

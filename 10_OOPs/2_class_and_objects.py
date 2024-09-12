### Classes and Objects : 

class StarCookie : 

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def get(self):
        print(f"Weight : {self.weight}")
        print(f"Color : {self.color}")

s1 = StarCookie(10, 'Red')
s1.get()
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model= model
        self.year= year
        self.color= color

    def drive(self):
           print('car is driving')

    def stop (self):
            print('car has stopped')




car_1= Car('chevy','covetter',2021,'blue') 
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1. color)

car_1.drive()
car_1.stop()
# import numpy as np

# age = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# persebntage = int(input('Enter persentedge of %: '))
# ungest = np.percentile(age, persebntage)



# def numberofage(age, ungest):
#     box = []
#     number = 0
#     for x in age:
#         if x <= ungest:
#             number += 1
#             box.append(x)
#     return f'{ungest} years old make up {persebntage}% of the population and yonger, and their number is: {len(box)}'


# x1 = numberofage(age, ungest)

# print(x1)


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0

#     def accelerate(self):
#         self.speed += 10

#     def brake(self):
#         if self.speed >= 10:
#             self.speed -= 10
#         else:
#             self.speed = 0

#     def get_speed(self):
#         return self.speed

# my_car = Car("Ford", "Mustang", 2022)
# print("Make: ", my_car.make)
# print("Model: ", my_car.model)
# print("Year: ", my_car.year)

# my_car.accelerate()
# my_car.accelerate()
# my_car.accelerate()

# print("Speed: ", my_car.get_speed())

# my_car.brake()

# print("Speed: ", my_car.get_speed())






#------- new Example ---------# 
num1 = {1,2,3}
num2 = {9,8,10}

thed = num1.symmetric_difference(num2)
thea = num1.isdisjoint(num2)
print(thea)
print(thed)


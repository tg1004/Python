def area_of_triangle(h,b):
    area=1/2*b*h
    return area

h=int(input("Enter height"))
b=int(input("Enter base"))

area=area_of_triangle(h,b)
print("Area of the triangle is:",area)


question 2

def area(side1, side2, shape='triangle'):
        if shape=='triangle':
             area=1/2*side2*side1

        elif shape=='rectangle':
            area=side1*side2

        else:
            print("ERROR")
            area='none'
        return area


shape = input("Enter the shape")
total=area(5,10,shape)
print("Area of the",shape, "is:",total)

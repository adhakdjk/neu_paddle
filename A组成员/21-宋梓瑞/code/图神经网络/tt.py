def calculate(x,y):
    for chicken in range(0,x):
        rabbit = x-chicken
        if  y == chicken*2 + rabbit*4:
            return rabbit,chicken
    print("DataErro")

x,y=input().
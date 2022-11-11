a = int(input())
b = int(input())
c = int(input())

x1 = (-b + (b**2 - 4 * a * c)**(1/2))/(2*a)
x2 = (-b - (b**2 - 4 * a * c)**(1/2))/(2*a)

print(x1, x2)
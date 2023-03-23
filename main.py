def improved_average():
    a = int(input("enter a first number:"))
    b = int(input("enter a second number:"))
    c = int(input("enter a third number:"))
    d = int(input("enter a fourth number:"))
    e = int(input("enter a fifth number:"))
    array = [a, b, c, d, e]
    mean = (a+b+c+d+e)/5
    median = array[2]
    mode = 3*median-2*mean
    print("mode of given number:", mode)
    print("median of given number:", median)
    print("mean of given number", mean)










































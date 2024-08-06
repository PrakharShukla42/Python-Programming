def is_Armstrong(num):
    size = len(str(num))
    hold = num
    sum = 0
    while(hold>0):
        digit = hold % 10
    sum += digit**size
    hold //= 10
    if(sum==num):
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
is_Armstrong(153)
is_Armstrong(1)
is_Armstrong(99)

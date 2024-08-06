a=1
def myfunction():
    global a
    print('global value of a before changing:',a)
    a=2
    print('modified value of a is:',a)
myfunction()
print('global value of after changing is :',a)

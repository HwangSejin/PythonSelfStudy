var1 = 5
# def some_func():
#     var2 = 6
#     def some_inner_func():
#         var = 7

count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

def some_func():
    print("You are welcome to some_func")
    #print(var)
some_func()


def some_func1():
    print("Inside some_func")
    # def some_inner_func():
    #     var = 10
    #     print("Inside inner function, value of var", var)
    # some_inner_func1()
#     print("Try printing var from outer function: ", var)
some_func1()
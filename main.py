from task1 import kwargsAcceptFun
kwargsAcceptFun(name="Asilbek", age=19, city="Tashkent", occupation="Student")
print()



from task2 import typeBasedTransformer
typeBasedTransformer(name="Asilbek",age=19,flag=True,data_list=[1, 2, 3],data_tuple=(7, 9, 11),data_dict={"a": 1, "b": 2})
print()



import random
from task1 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i
    
if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()

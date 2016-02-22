'''
Created on 2016. 2. 19.

@author: leejinwon
'''
# 3. Function
# ref. : https://wikidocs.net/60
print('[ex] function --------------------------')
def print_list(a):
    for i in a:
        print i
        
        
print_list([1,2,3,4,5,6])

# 3.1 Recursive 
print('[ex] recursive --------------------------')
def add(a, b):
    print a + b
    
def multiply(a, b):
    print a * b
    
def addNMultiply(a, b):
    add(a, b)
    multiply(a, b)
    
def countdown(n):
    if n == 0:
        print "it's done"
    else:
        print n
        countdown(n-1)
        
countdown(5)        

# 3.2. practice
print('[ex] practice 9 * 9 --------------------------')
i = 1
j = 1
result = 0

def multiply2(i, j):
    result = i * j
    print i, " * ", j, " = ", result 
    if (i == 9 and i == j): 
        print "it's done"
    else:    
        if j == 9:
            i = i + 1
            j = 1
        else:
            j = j + 1
        multiply2(i, j)    
               
multiply2(i,j);        
    
    
# 3.3. local value, global value
# ref. : https://wikidocs.net/62

val = 'this is local value'
print('[ex] local / global value --------------------------')
def localValTest():
    val = 9
    print val 
    
localValTest()
print val       

# Way to make global value in function
print('[ex] Way to make global value in function --------------------------')
def globalInFunction():
    global lVal
    lVal = 10
    print "lVal's value is", lVal

globalInFunction()
print lVal   


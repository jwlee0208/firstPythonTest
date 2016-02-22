'''
Created on 2016. 2. 19.

@author: leejinwon
'''
# 2. control construct
# 2.1. while
# ref. : https://wikidocs.net/56
print('[ex] while --------------------------')
num = 1
while num <= 100:
    print(num);
    num = num + 1
    
# 2.2. if
# ref. : https://wikidocs.net/57
print('[ex] if --------------------------')
a = 10000
b = 20000

if a > b:
    print('a')
elif a == b:
    print('a == b')
else:
    print('b')    
        
# 2.3. for
# ref. : https://wikidocs.net/58
print('[ex] for --------------------------')
family = ['mother', 'father', 'me', 'sister']  
for x in family:
    print('%s %s' % (x, len(x)) )   
    
      
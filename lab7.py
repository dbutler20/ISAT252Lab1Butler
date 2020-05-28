"""
Lab 7
"""

#3.1
i=0
while i<6:
    if i!=3:
        print(i)
    i=i+1
    
#3.2
i=1
result=1
while i<=5:
    result=result*i
    i=i+1
    print(result)
    
#3.3
i=1
result2=0
while i<=5:
    result2=result2 +1
    i= i+1
print(result2)

#3.4
i=3
result1=1

while i<=8:
    result1=result1*i
    i=i+1
print(result1)

#3.5
i=4
results=1
while i<=8:
    results=results*i
    i=i+1
print(results)

#3.6
num_list=[12,32,43,35]
while num_list:
    num_list.remove(num_list[0])
print(num_list)

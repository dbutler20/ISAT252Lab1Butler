"""
Lab 6

"""
#3.1
for num in range(6):
    if num !=3:
        print(num)
    
#3.2
result_32=1

for num in range(1,6):
    result_32=result_32*num
print(result_32)
    
#3.3
result_33=0
for num in range(1,6):
    result_33=result_33+num
print(result_33)

#3.4
result_34=1
for num in range(3,9):
    result_34=result_34*num
print(result_34)

#3.5
result_35=1
result_335=1
for num in range(1,9):
    result_35=result_35*num
    
for num in range(1,4):
    result_335=result_335*num

    
    result=(result_35)/result_335
print(result)

#3.6
result=0
for word in 'this is my 6th string'.split():
    #print(word)
    result=result+1
    
print(result)

#3.7
my_tweet= {
    'favorite_count':1138,
    'lang':'en',
    'coordinates':(-75,40),
    'entities':{'hashtags':['Preds','Pens','SingintoSpring']}
    
}
result=0
for hashtag in my_tweet['entities']['hashtags']:
    result=result+1
    print(result)
    
    
    
    
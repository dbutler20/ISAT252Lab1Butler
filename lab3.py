"""
Lab 3
ISAT 252
5/20/20
"""
#3.1
str_list=['a','b','e','d','c']
str_list.sort()
print(str_list)

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(list(str_list)[2])

#3.5
my_list=['1','123','123','b','B','False',False,123,None,'None']
my_unique_letters=set(my_list)
print(my_unique_letters)
print(len(my_unique_letters))
#3.6
print(len("This is my third python lab"))

#3.7
num_list=[12,32,43,35]
num_list.sort()
print((num_list[3]))
print((num_list[0]))

#3.8
game_board=[[0,0,0],[0,0,0],[0,0,0]]
print(game_board)
game_board[1]=[0,1,0]
print(game_board)




m = 3
n = 2
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alpha1= alpha[:n]
seat = [[f"{j}{i+1}" for i in range(m)] for j in alpha1]
st=[]
for i in seat:
	st = st+i
print(st)


indexed = {f"{k}":[i,'N'] for (i,k) in enumerate(st)} #{'A1': [0, 'N'], 'A2': [1, 'N'], 'B1': [2, 'N'], 'B2': [3, 'N']}

print(indexed)

def update_dict_recursive(indexed, seat_nums='None'):
    if seat_nums == 'None':
        return('No seats provided')
    seat_num = seat_nums[0]
    if not seat_nums:
        return
    if seat_num not in seat_nums:
    	return(f'seat not found {seat_num}')
    else:
        indexed[seat_num][1] = 'B'
        update_dict_recursive(indexed, seat_nums[1:])
    
update_dict_recursive(indexed, ['A1','A2','A10'])
print(f'after {indexed}')
# Working on a scenario where an incorrect seat or out of bound seat number is passed along with existing ones,
# Here is the output along with the error
# ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
# {'A1': [0, 'N'], 'A2': [1, 'N'], 'A3': [2, 'N'], 'B1': [3, 'N'], 'B2': [4, 'N'], 'B3': [5, 'N']}
# Traceback (most recent call last):
#   File "<string>", line 31, in <module>
#   File "<string>", line 29, in update_dict_recursive
# ERROR!
# File "<string>", line 29, in update_dict_recursive
#   File "<string>", line 28, in update_dict_recursive
# KeyError: 'A10'

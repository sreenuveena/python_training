#greeting = 'hello, hi, hey'
#greeting = ['hello','hi','hey']

#print(greeting)
#print(greeting[2])

#greeting = ['hello','hi','hey']

# print(greeting.index('hey'))
# list_2 = ['bye','hola']

# to add an item use append
# greeting.append('hola')
# greeting.insert(1,'hola')
# greeting.extend(list_2)

#greeting.remove('hey')
# removed = greeting.pop(1)
# print(removed)

# nums = [2,4,6,1,5,3]

# nums.sort(reverse=true)
# print(nums)

# sorted_nuums = sorted(nums)
# print(sorted_nums)


#print('hi' in greeting)

# for i in greeting:
#	 print(i)

# Access a list

# for i in greeting:
# 	print('hello')

# for index, item in enumerate(greeting):
# 	print(index, item)	

# print(greeting)

# from list to string
greeting = ['hello','hi','hey']

new_str = '-'.join(greeting)
print(type(new_str))

#print(new_str)

#from str to list
new_list = new_str.split('-')
print(type(new_list))

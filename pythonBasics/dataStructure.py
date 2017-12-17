#python Data Structures

#tuples
rate = ("Good",10,10.2)
rate2 = rate +("bad",-10,-10.2)

print(rate2)
#slice tuple
print(rate2[1:3])
print(rate[2])
#length
print(len(rate2))
#sort
rate3 = (1,4,3,2,6,9,10,5)
print(sorted(rate3))
#nested Tuple
print(rate2[0][2])




#list
list=["munna",10.1,200,("Good",2)]
#mutables in list
list.extend(["pop",30])
print(list)
list.append(["popnew",40])
#delete fom List
del(list[3])
print(list)
#clone list
list2 = list[:]
# changes in list2 will not effect list 1
del(list2[3])
print("new list",list2)
print("old list",list)

#@author  mohammed Fathauddin
#since 2017-12

#simple Print
print('hello world')

#simple Print Multiple times
print('hello world'*2)

#simple Print with n-power times
print('hello world'*(2**4))


#varible Declarations
x= 1
y = 20
x=x+y
print("result = ")
print(x)


#while Loop
x= 1
while x<10:
    print(x)
    x+=1

#for Loop ==============
#list
x = [1,5,6,7,8,2,3,4,5,16]
for i in x:
    if i>5:
        print(i)
#using Range [FROM 1 To 10]
for x in range(1,11):
    print(x)
#=====================


#if/else/elif condition
x= 10
y= 20

if x>y :
    print("X is great")
    if x > 5 :
        print(" And X is great than five")
elif x > 5 :
    print("X is great than five")
else:
    print("Y is great")

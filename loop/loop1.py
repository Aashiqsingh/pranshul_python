
# i = 1
# for i in range(i,10+1):
#     print(i,end=" ") 


# i = 1
# for i in range(i,10+1):
#     print("*")


# factorial number 

# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i 
# print(fact)


# for i in range(10):
#     print(i)


# for i in range(1,10):
#     print(i)

# for i in range(1,10,3):
#     print(i)


# for i in range(10,1,-2):
#     print(i)

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print("\n")


# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")


for i in range(5):
    for j in range(5):
        if i == 0 or j == 0 or i == 4 or j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
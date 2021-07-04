

# try:
#   a = int(input("enter the no to start with : "))
#   b = int(input("enter the no to end : "))
# except:
#     print("Enter only int value...")

#     if (a > b):
#         print(
#             "The last no should be greater always. Correct the input")


# for num in range(a,b+1) :
#     if num > 1:
#         for c in range(2, num) :
#             if (num % c) == 0:
#                 break
#             else:
#                 print(num)
#                 break     

##############   FILE OPERATION    ################  
# from itertools import izip
# with open('res.txt','w+')as f3,open('fruit.txt','w+')as f2, open('alpha.txt','w+')as f1 :
#     for line1,line2 in zip(f1,f2):
#         f3.write("{} {}\n".format(line1.rstrip(),line2.rstrip()))
# with open('alpha.txt','w') as r:
#     r.write('a for \n')
#     r.write('b for \n')
#     r.write('c for \n')
with open('fruit.txt') as f,open('alpha.txt') as f2,open('res.txt','w')as res :
    for line1,line2 in zip(f,f2) :
            res.write("{} {}\n".format(line2,line1))

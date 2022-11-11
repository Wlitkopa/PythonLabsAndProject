# import random
#
# prison = []
#
# # inp = int(input("Enter the prison size: "))
#
# # for i in range(inp):
# #     prison.append(random.randint(0, 1))
#
# # inp = int(input("Please enter: \n1 - cell open \n0 - cell closed\n2 - finish input\n"))
# #
# # while inp != 2:
# #     prison.append(inp)
# #     inp = int(input())
#
# # print(prison)
# freed = 0
# prison = [1, 1, 0, 0, 0, 1, 0]
# inp = len(prison)
#
# for i in range(inp):
#     if prison[i] == 1:
#         freed += 1
#         for j in range(inp):
#             print(prison)
#             if prison[j] == 1:
#                 prison[j] = 0
#             else:
#                 prison[j] = 1
#         # print(prison)
#     print("\n")
#
# print('number of freed: ', freed)






import random

prison = []

# inp = int(input("Enter the prison size: "))

# for i in range(inp):
#     prison.append(random.randint(0, 1))

inp = int(input("Please enter: \n1 - cell open \n0 - cell closed\n2 - finish input\n"))

while inp != 2:
    prison.append(inp)
    inp = int(input())
freed = 0
print(prison)
for i in range(inp):
    if prison[i] == 1:
        freed += 1
        for j in range(inp):
            print(prison)
            if prison[j] == 1:
                prison[j] = 0
            else:
                prison[j] = 1
        print(prison)

print('number of freed: ', freed)



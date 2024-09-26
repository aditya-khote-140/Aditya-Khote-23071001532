# WAP to find greatest number in the list in which list consist of 10 elements.

# a=[-10,-30,-20,-40,-60,-50,-70,-90,-80,-1]

# print("Greatest num is :",max(a))

a = [10, 30, 20, 40, 60, 50, 70,90, 80, 1]

greatest = a[0]
index = [0]

for i in range(1,len(a)):
    if a[i] > greatest:
        greatest = a[i]
        index = i
print("Greatest num is :", greatest, "and index is ",index)

#take a list by your self of 10 number find out the number of even number and odd number in the list.
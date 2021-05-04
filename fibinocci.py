"""Write a program to print the fibonacci series.The number of terms to be printed will be determined by the number that the user inputs.
Input Format
The input is just one line, where the user enters an integer number.The program has to print as many fibonacciseries terms as that of the number entered.

Sample
Input
4
Sample
Output
0
1
1
2"""

l = int(input("enter the limit"))
list1 = []
a = 0
b = 1
c = a + b
list1.append(a)
list1.append(b)
list1.append(c)
cnt = 0
while cnt <= l:
    a = b
    b = c
    c = a + b
    list1.append(c)
    cnt += 1

for i in range(l):
    print(list1[i])





## A for Loop with Errors

f""""
Assume some program has been written for the task of adding all integers
i = 1,2,...,10 and printing the final result:

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum = Sum + x
print 'sum:', sum

a.) identify the errors in the program by just reading the code.
b.) write a new version of the program with errors corrected.
    run this program and confirm that it gives the correct output.
"""

answer = 0
for i in range(1, 10):
    answer += i         ## answer = answer + i

print('answer', answer)
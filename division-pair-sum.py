**Division Pair Sum**

Given an array of n elements and a number m, we need to find all distinct pairs existing in the array whose pair sum is divisible by the given number m.

Print the total number of such pairs. Distinct pairs means (1, 2) and (2, 1) are the same, i.e., ordering of the pairs doesn't matter.

**Example Input**

10 9 4 5 7 2 8 20 21

15

**Output**

4

**Explanation**

The following pairs give a sum divisible by 15: 10,5, 10,20, 9,21, 7,8

**Input Format**

The first line of input contains T, the number of test cases. In the next 2*T lines:

1.The first line contains n followed by n elements of the array

2.The next line contains m

**Output Format**

Print T lines for all the required outputs
"""

p=int(input())
for k in range(p):
    c=0
    l=list(map(int,input().split()))
    l=list(dict.fromkeys(l))
    n=int(input())
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[i]+l[j])%n==0:
                c=c+1
    print(c)

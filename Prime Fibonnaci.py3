"""
Prime Fibonnaci 

Problem Description
Given two numbers N1 and N2.

Find prime numbers between N1 and N2, then
Make all possible unique combinations of numbers from the prime numbers list you found in step 1.
From this new list, again find all prime numbers.
Find smallest A and largest B number from the 2nd generated list, also count of this list.
Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series 
respectively till the count (Number of primes in the 2nd list).
Print the last number of a Fibonacci series as an output
Constraints

2 <= N1, N2 <= 100

N2 – N1 >= 35

Examples:






Input:  N1 = 2, N2 = 40
Output: 13158006689
Explanation:
First prime list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

Combination of all the primes = [23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 32, 35, 37, 311, 313, 319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719, 723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]

Second prime list=[193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117, 223, 1123, 229, 37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723, 317]

smallest (A) = 23

largest (B) = 3719
Therefore, the last number of a Fibonacci series i.e. 34th Fibonacci number in the series that has 23 and 3719 as the first 2 numbers is 13158006689

Input: N1 = 30, N2 = 70
Output: 2027041
Explanation:

First prime list = [31, 37, 41, 43, 47, 53, 59, 61, 67]

Second prime list generated form combination of 1st prime list = [3137, 5953, 5347, 6761, 3761, 4337, 6737, 6131, 3767, 4759, 4153, 3167, 4159, 6143]
Smallest prime in 2nd list=3137
Largest prime in 2nd list=6761
Therefore, the last number of a Fibonacci series i.e. 14th Fibonacci number in the series that has 3137 and 6761 as the first 2 numbers is 2027041
"""
def prime(n):
 flag = 0
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   flag = 1
   break
 return flag
n = input().split()
m = input().split()
n=int(n)
m=int(m)
Prime1=[]

for i in range(n,m+1):
 if prime(i)==0:
  Prime1.append(i)

Prime2=[]

for i in Prime1:
 for j in Prime1:
  cross_prod = int(str(i)+str(j))
  if prime(cross_prod)==0 and cross_prod not in Prime2:
   Prime2.append(cross_prod)

num1=min(Prime2)
num2=max(Prime2)

for i in range(len(Prime2)-2):
 sum=num1+num2
 num1=num2
 num2=sum
print(sum,end="")
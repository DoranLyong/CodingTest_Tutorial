"""
[ref] https://codeup.kr/problem.php?id=1038

Question:
    1. take two integers 
    2. print the sum of them 
"""
import sys 


x, y = map(int, sys.stdin.readline().rstrip().split())


print(x + y)   # 123 + (-123)

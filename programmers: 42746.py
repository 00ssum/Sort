#시간 초과 나온 코드
from itertools import permutations
def solution(numbers):
    numbers=list(map(str,numbers))
    arr=list(map("".join, permutations(numbers,len(numbers))))
    arr.sort()
    answer = arr[-1]
    return answer
  
  #----------------------------------------
# 참고한 코드
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = list(map(str,numbers)) #문자열로 변환
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
# 프로그래머스 Lv.1 1845번 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter

def solution(nums):
    cnt = len(Counter(nums))
    max_cnt = len(nums)//2
    
    return max_cnt if cnt > max_cnt else cnt

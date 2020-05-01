
def is_safe ( stones, k ):
    for step in range(len(stones)-k+1):
        if stones[ step : step+k ] == [0]*k:
            return False
    return True


def solution_timeover1 ( stones, k ):
    print(stones)
    answer = 0
    while is_safe(stones,k):
        answer += 1
        stones = list(map(lambda x: x-1 if x>0 else x, stones))
        print(stones)

    return answer

# 시간초과
# O(N^2)


def solution_timeover2 ( stones, k ):
    sub_stones = []
    for step in range(len(stones)-k+1):
        stone = max( stones[ step: step+k ] )
        sub_stones.append(stone)
    
    return min(sub_stones)
    
# 시간초과
# O(N*K)

def solution_timeover3 ( stones, k ):
    answer = float('inf')
    for step in range(len(stones)-k+1):
        stn = max( stones[ step: step+k ] )
        if stn < answer:
            answer = stn
    return answer

# 시간초과
# O(N*K)



def solution_13 ( stones, k ):
    
    if k == 1:
        return min(stones)

    answer = max(stones[ :k])
    idx = stones.index(answer)
    
    while idx+k < len(stones):
        max_stone = max(stones[idx+1 : idx+1+k])
        idx = stones.index(max_stone, idx+1, idx+1+k)
        if answer > max_stone:
            answer = max_stone

    return answer

# test case #13 에서 시간초과


def is_end_case( stones, k, n ):

    stones.append(float('inf'))
    cnt = 0
    prev_cnt = -1
    
    for stone in stones:
        if stone < n:
            cnt += 1
        else:
            if cnt > prev_cnt:
                prev_cnt = cnt
            cnt = 0
    
    return prev_cnt >= k


def solution( stones, k ):
    min_stone = min(stones)
    max_stone = max(stones)

    while min_stone <= max_stone:
        mid = (min_stone + max_stone) // 2
        if is_end_case( stones, k, mid ):
            max_stone = mid 
        else:
            answer = mid
            min_stone = mid

    return answer
    
#print(solution([2,4,5,3,2,1,4,2,5,1],3))


def binary_search (target, N):
    low, high = min(N), max(N)

    while True:
        
        mid = (low+high) // 2
        print(low, mid, high)
        if target == mid:
            return mid

        elif target > mid: # up condition
            low = mid+1

        else: # down condition
            high = mid-1



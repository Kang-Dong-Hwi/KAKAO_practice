def solution(N, stages):
    N = [ [0,0] ]*N
    answer = []
    failrate = []

    for stg in range(len(N)):
        N[stg] =  [stages.count(stg+1), len( list( u for u in stages if u > stg ))] 
        #[non-clear, clear]    

    for n in range(len(N)):
        if N[n][1]:
            rate = float( N[n][0] / N[n][1] )
        else:
            rate = 0
        failrate.append( [ n, rate ] )

    answer = sorted(failrate, key = lambda x: x[1], reverse = True)
    answer = [i[0]+1 for i in answer]
    return answer


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
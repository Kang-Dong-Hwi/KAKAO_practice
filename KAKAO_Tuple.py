def solution(s):

    s = s[ 2 : len(s)-2 ].split('},{')
    
    for i in range(len(s)):
        subset = s[i].split(',')
        s[i] = subset
    
    s = [[int(i) for i in j] for j in s]
    s.sort(key=len)
    ## 원소의 크기순 정렬 ##

    answer = [s[0][0]]
    for sb in s[1::]:
        for element in sb:
            if element not in answer:
                answer.append(element)
                break
        
    return answer

def solution(s):
    answer = len(s)
    half = int( len(s) / 2 )

    for i in range(1, half + 1):

        div =  len(s) // i
        sub = []

        for j in range(div):
            sub.append( s[ i*j: i*(j+1) : 1 ] )

        k = 0
        cmp = sub[0]
        length = len(s)
        cnt = 1

        while( k != len(sub)-1 ):
            if(cmp == sub[k+1]):
                cnt = cnt + 1
                k = k + 1
                length = length - i

            else:
                cmp = sub[k+1]
                k = k + 1

                if( cnt != 1 ):
                    length = length + len( str(cnt))
                    cnt = 1

        if( cnt != 1 ):
            length  = length + len( str(cnt))

        if( answer > length ):
            answer = length

    return answer
    
# '''
# string = 'a'*99
# print(len(string))
# print(solution(string))
# '''

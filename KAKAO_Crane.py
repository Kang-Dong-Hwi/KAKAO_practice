
def solution(board, moves):

    moves = [i-1 for i in moves]
    result = [0]
    answer = 0

    for col in moves:
        for row in range(len(board)):
            if board[row][col] != 0:
           #if board[row][col]: 
                if result[-1] == board[row][col]:
                    answer += 2
                    result.pop()
                else:
                    result.append( board[row][col] ) 
                board[row][col]= 0
                break
        print(result, answer)
    return answer

# transpose Mat
#   (board)^t = 
#               [list(i) for i in list(zip(*board))]
#



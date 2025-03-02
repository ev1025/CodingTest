def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i =='left':
            answer[0]-=1
        elif i=='right':
            answer[0]+=1
        elif i=='down':
            answer[1]-=1
        else:   
            answer[1]+=1
            
        if abs(answer[0]) > abs(board[0]//2):
            if answer[0] > 0:
                answer[0] = board[0]//2
            else:
                answer[0] = -(board[0]//2)

        if abs(answer[1]) > abs(board[1]//2):
            if answer[1] > 0:
                answer[1] = board[1]//2
            else:
                answer[1] = -(board[1]//2)
    return answer
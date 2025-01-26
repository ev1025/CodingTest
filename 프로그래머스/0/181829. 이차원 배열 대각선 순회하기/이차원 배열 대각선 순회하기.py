def solution(board, k):
    i = len(board)
    j = len(board[0])
    return sum([board[n][s] for n in range(i) for s in range(j) if s+n<=k])
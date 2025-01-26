def solution(board, k):
    return sum([board[n][s] for n in range(len(board)) for s in range(len(board[0])) if s+n<=k])
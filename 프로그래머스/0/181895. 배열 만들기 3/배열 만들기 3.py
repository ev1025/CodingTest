def solution(arr, intervals):
    answer = sum([arr[intervals[i][0]:intervals[i][1]+1] 
                  for i in range(len(intervals))],[])
    
    return answer
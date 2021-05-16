score = 0
score_ready = []

def solution(board:list, moves:list):
    answer = 0
    
    for move in range(len(moves)):
        for i in range(len(board)):
            doll = board[i][moves[move]-1]
            if doll!=0:
                score_ready.append(doll)
                board[i][moves[move]-1]=0
                
                for i in range(len(board)):
                    print(board[i])
                print(score_ready,"\n")
                break

    # print(score_ready)
    return answer

4,3,1,1,3,2,
print(solution([[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]],
                [1,5,3,5,1,2,1,4]))
# def SetScore(doll):
#     global score
#     if score_ready[len(score_ready)-1] == doll:
#         score_ready.remove(score_ready[len(score_ready)-1])
#         score += 1
#     else:
#         score_ready.append(doll)

# def solution(board, moves):
#     for move in range(len(moves)):
#         for i in range(len(board)):
#             if board[i][moves[move]-1] != 0:
#                 SetScore(board[i][moves[move]-1])
#                 print(board[i])
#                 break

#     return score

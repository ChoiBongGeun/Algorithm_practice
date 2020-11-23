def solution(begin, target, words):
    answer = 0
    if target in words:
        for i in range(len(words)):
            check =0
            for j in range(len(words[i])):
                print(begin[j],words[i][j], check)
                if begin[j] != words[i][j]:
                    check +=1
                else:
                    continue
            if check >=2:
                return 0
            else:
                answer +=1
                begin = words[i]
    
    else:
        return 0
    return answer

words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
begin = 'hit'
target = 'cog'
print(solution(begin,target,words))
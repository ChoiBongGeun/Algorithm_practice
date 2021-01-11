def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        match=''
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                match += skill_trees[i][j]
                #skill_trees에서 skill에 있는것만 match에 넣어주었따
            else:
                pass
        if match in skill[:len(match)]:
            #순서대로 있는것 뿐만 아니라 첫번째 부터 있어야하기 때문에 in skill이 아닌 skill[:len(match)]:을 통해 첫번째 부터 있는지 확인해주었다
            answer +=1

                
    return answer


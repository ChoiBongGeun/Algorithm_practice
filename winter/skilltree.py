def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        match=''
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                match += skill_trees[i][j]
            else:
                pass
        if match in skill[:len(match)]:
            answer +=1

                
    return answer

skill = "CBD"	
skill_trees =["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))
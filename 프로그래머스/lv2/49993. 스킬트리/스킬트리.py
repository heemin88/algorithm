def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx = float('inf')
        cnt = 0
        success= True
        for s in skill:
            if s in skill_tree:
                idx = skill_tree.index(s)
                if idx < cnt : #실패 
                    success= False
                    break
                else:
                    cnt = idx 
            else:
                cnt= float('inf')
        if success:
            answer +=1
        
            
        
        
    return answer
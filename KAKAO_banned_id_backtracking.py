# 1. back_tracking 
# 2. delete overlaped case

case_set = []

def isbanned(user, banned_user):
    if len(user) != len(banned_user):
        return False
    for a,b in zip(user, banned_user):
        if b != '*' and a != b:
            return False
    return True


def addcase( i , case ):
    if not case:
        return True
    elif i not in case:
        return True


def cases ( suspects, index, case ):
    global case_set
    if index == len(suspects):
        case_set.append(set(case))
    else:
        for i in suspects[index]:        
            if addcase(i,case):
                case.append(i)
                cases( suspects, index+1, case )
                case.pop()
                

def solution (user_id, banned_id):
    suspects = []

    for b in banned_id:
        suspects.append([])
        for user in user_id:
            if isbanned(user, b):
                suspects[-1].append(user_id.index(user))
    
    cases( suspects, 0, [])         #backtracking
    answer = [str(s) for s in case_set]
    answer = list(set(answer))      #delete overlaped case
    return len(answer) 



#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
#               ["fr*d*", "*rodo", "******", "******"]))

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"],
                 ["*rodo", "*rodo", "******"]))


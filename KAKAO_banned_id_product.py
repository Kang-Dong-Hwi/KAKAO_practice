from itertools import product

# 1. itertools.product -> combination
# 2. delete overlaped cases using set type

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)


    result = list(product(*result))

    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add(tuple(set(r)))

    return len(answer)


print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"],
                 ["*rodo", "*rodo", "******"]))
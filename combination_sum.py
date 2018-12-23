def combination_sum(candidates, target):
    res = []
    candidates = sorted(candidates)
    def helper(remaining, in_progress):
        print(remaining, in_progress)
        if remaining == 0:
            res.append(in_progress[::-1])
            return 
        for candidate in candidates:
            if candidate <= remaining and (not in_progress or candidate <= in_progress[-1]):
                helper(remaining - candidate, in_progress + [candidate])    
    helper(target, [])
    return res

print(combination_sum([2, 6, 7, 3], 7))
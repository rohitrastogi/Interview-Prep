def solve_sort(target, candidates):
    candidates = sorted(candidates)
    for i in range(len(candidates) - 2):
        left = i + 1
        right = len(candidates) - 1
        subproblem_target = target - candidates[i]
        while left < right:
            if candidates[left] + candidates[right] == subproblem_target:
                return True
            elif candidates[left] + candidates[right] < subproblem_target:
                left += 1
            else:
                right -= 1
    return False

def solve_hash(target, candidates):
    for i in range(len(candidates) - 2):
        subproblem_target = target - candidates[i]
        seen = set()
        for j in range(i + 1, len(candidates)):
            if subproblem_target - candidates[j] not in seen:
                seen.add(candidates[j])
            else:
                return True
    return False


print(solve_hash(10, [5, 8, 4, 7, 9]))

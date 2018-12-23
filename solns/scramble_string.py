
def solve(s1, s2):
    memo = {}

    def is_scramble(s1, s2):
        res = False
        #base case for a single character 
        if s1 == s2:
            return True
        #short circuit for clearly bad inputs
        if sorted(s1) != sorted(s2):
            return False

        #ate, tea
        for i in range(1, len(s1)):
            if (is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])) or (is_scramble(s1[:i], s2[len(s2) - 1 - i:]) and is_scramble(s1[i:], s2[:len(s2) - i])):
                res = True
                break 
        memo[(s1, s2)] = res
        return res
    
    return is_scramble(s1, s2)

#same pattern as parenthesis question
'''
differences: 
only execute loop body if input[i] is an operator
res.append(execute_operator(a, b, op))

'''
def generate_scrambles(input_s):
    memo = {}
    def scramble(s):
        if s in memo:
            return memo[s]

        #base case for a single character 
        if len(s) == 1:
            return [s]
        res = []

        #ate, tea
        for i in range(1, len(s)):
            left = scramble(s[:i])
            right = scramble(s[i:])
            for i in left:
                for j in right:
                    res.append(i + j)
                    res.append(j + i)

        memo[s] = list(set(res))
        return memo[s]

    res = scramble(input_s)
    print(memo)
    return res

print(len(generate_scrambles('teasd')))
    
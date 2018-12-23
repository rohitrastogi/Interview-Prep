#wordladder (modified bfs)

def solve(begin, end, word_list):
    queue = []
    used = set( (begin, 1) )
    queue.append( (begin, 1) )
    while queue:
        curr, depth = queue.pop()
        if curr == end:
            return depth
        reachable = list(filter(lambda x: is_reachable(curr, x), word_list))
        for word in reachable:
            if word not in used:
                used.add( (word, depth + 1) )
                queue.append( (word, depth + 1) )
    return 0

def is_reachable(begin, word):
    count = 0
    for i in range(len(begin)):
        if begin[i]!=word[i]:
            count += 1
        if count > 1:
            return False
    return count == 1

words = ['hot', 'dot', 'lot', 'cog']

# def construct_dict(word_list):
#     d = {}
#     for word in word_list:
#         for i in range(len(word)):
#             s = word[:i] + "_" + word[i+1:]
#             d[s] = d.get(s, []) + [word]
#     return d
print(solve('hit', 'cog', words))
#print(construct_dict(words))





    
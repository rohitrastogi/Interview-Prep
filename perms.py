def generate_perms(s):
    arrangements = []
    def perm_helper(prefix, rest):
        if not rest:
            arrangements.append(prefix)
        else:
            for i, val in enumerate(rest):
                perm_helper(prefix + val, rest[:i] + rest[i+1:])
               
    perm_helper('', s)
    return arrangements
        

def generate_unique_perms(s):
    arrangements = []
    def perm_helper(prefix, rest):
        seen = set()
        if not rest:
            arrangements.append(prefix)
        else:
            for i, val in enumerate(rest):
                if val not in seen:
                    perm_helper(prefix + val, rest[:i] + rest[i+1:])
                seen.add(val)
               
    perm_helper('', s)
    return arrangements

print(generate_unique_perms('aba'))
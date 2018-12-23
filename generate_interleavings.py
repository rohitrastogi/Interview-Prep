s1 = 'ab'
s2 = 'cd'

def generate_interleavings(s1, s2, s3):
    return (helper(s1, s2, s3, 0, 0, ''))

def helper(s1, s2, s3, s1_index, s2_index, in_progress):
    ans = False
    progress_length = len(in_progress)
    
    if s3 == in_progress and s1_index is len(s1) and s2_index is len(s2):
        return True

    if in_progress == s3[:progress_length]:
        if s1_index < len(s1):
            ans = ans or helper(s1, s2, s3, s1_index + 1, s2_index, in_progress + s1[s1_index])

        if s2_index < len(s2):
            ans = ans or helper(s1, s2, s3, s1_index, s2_index + 1, in_progress + s2[s2_index])
    else:
        ans = ans or False 
    return ans

print(generate_interleavings(s1, s2, 'dcba'))
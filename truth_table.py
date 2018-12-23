def generate_truth_table_gen(n):
    def helper(in_progress):
        if len(in_progress) == n:
            yield in_progress
        else:
            for key in generate_truth_table(n-1):
                yield key + "F"
                yield key + "T"
    return helper("")


def generate_truth_table(n):
    key_space = []
    def helper(in_progress):
        if len(in_progress) == n:
            key_space.append(in_progress)
        else:
            helper(in_progress + "F")
            helper(in_progress + "T")
    helper("")
    return key_space

print(generate_truth_table(3))
# for key in generate_truth_table(3):
#     print(key)
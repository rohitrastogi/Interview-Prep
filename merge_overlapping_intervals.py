#merge overlapping intervals

#input: list of lists - inner list has size of exactly 2
#SOLUTION 1: O(NLOGN)
def merge(intervals):
    res = []
    sorted_intervals = sorted(intervals, key = lambda x: x[0])
    #list of size 2
    comp_interval = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        curr_upper = sorted_intervals[i][1]
        curr_lower = sorted_intervals[i][0]
        if curr_lower > comp_interval[1]:
            res.append(comp_interval[1] - comp_interval[0] + 1)
            comp_interval = sorted_intervals[i]
        elif curr_upper > comp_interval[1]:
            comp_interval[1] = curr_upper
    res.append(comp_interval[1] - comp_interval[0] + 1)
    return res

def populate_intervals(s):
    first_and_last = {}
    for i, char in enumerate(s):
        if char in first_and_last:
            first_and_last[char][1] = i
        else:
            first_and_last[char] = [i, i]
    return first_and_last.values()
            
def partition_labels_1(s):
    return merge(populate_intervals(s))

#SOLUTION 2: O(N)
def partition_labels_2(s):
    res = []
    start = 0
    end = 0
    last = {}
    for i, char in enumerate(s):
        last[char] = i
    for j, char in enumerate(s):
        end = max(end, last[char])
        if j == end:
            res.append(end - start + 1)
            start = end + 1
    return res


test = "ababcbacadefegdehijhklij"
print(partition_labels_1(test))
print(partition_labels_2(test))
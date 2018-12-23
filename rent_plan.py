'''
Given a movie title string and a list of movie strings, return the 'longest sequence of movies that you can rent'.
A 'sequence of movies that you can rent' is defined by the following:
    The last word in a rented movie title must be the first word of the next rented movie title in the sequence.
'''

def longest_rent_plan(inventory, start):
    longest_plan = []
    recur(start, [start], inventory, longest_plan)
    return longest_plan
    
def recur(title, curr_plan, inventory, longest_plan):
    search_word = title.split()[-1]
    possible_titles = find_matching_titles(inventory, curr_plan, search_word)
    if not possible_titles:
        if len(curr_plan) > len(longest_plan):
            longest_plan[:] = curr_plan
            
    for p_title in possible_titles:
        # curr_plan.append(p_title)
        recur(p_title, curr_plan + [p_title], inventory, longest_plan)
    
    #RUNS WHEN POSSIBLE TITLES IS EMPTY (backtrack)
    # curr_plan.pop()

def find_matching_titles(inventory, curr_plan, search_word):
    visited = set(curr_plan)
    res = []
    for movie in inventory:
        if movie.split()[0] == search_word and movie not in visited:
            res.append(movie)
    return res

start = 'I hate this'
inventory = [
    'this food tastes like my asshole',
    'this is the end',
    'end is good',
    'bah bah black sheep',
    'good dogs can herd sheep',
    'sheep make the sound bah',
    'good things happen to good people',
    'good meets evil',
    'evil is bad',
    'bad has three letters',
    'letters to my college roommate'
]

# SHOULD BE: ['I hate this', 'this is the end', 'end is good', 'good meets evil', 'evil is bad', 'bad has three letters', 'letters to my college roommate']
print(longest_rent_plan(inventory, start))
 
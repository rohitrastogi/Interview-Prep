#champagne tower
#DP
#(tree representation IS INCORRECT -> GOES AT DEPTH FIRST LEVEL -> middle cups do no properly accumulate middle cups)

# class Cup():
#     def __init__(self):
#         self.how_full = 0
#         self.left_child = None
#         self.right_child = None
#         self.left_sibling = None
#         self.right_sibling = None

#     def create_left_child(self):
#         if self.left_sibling:
#             child = self.left_sibling.right_child
#             self.left_child = child
#         else:
#             self.left_child = Cup()

#     def create_right_child():
#         self.right_child = Cup()
#         right_child.left_sibling = self.left_child
#         self.left_child.right_sibling = right_child

#     def pour(self, how_much):
#         if self.how_full + how_much < 1:
#             self.how_full += how_much
#         else:
#             self.how_full = 1
#             self.create_left_child()
#             self.create_right_child()
#             pour(self.left_child, (how_much-1)/2)
#             pour(self.right_child, (how_much-1)/2)

#     def query(self, query_glass, query_row):
#         cup = self
#         row = 0
#         glass = 0  
#         while cup:
#             if (row == query_row):
#                 break
#             row += 1
#             cup = cup.left_child
#         if not cup:
#             return 0

#         while cup:
#             if (glass == query_glass):
#                 break
#             glass += 1
#             cup = cup.left_sibling

#         if cup:
#             return cup.how_full
#         else:
#             return 0
    


# def solution(num_poured, query_glass, query_row):
#     cup = Cup()
#     cup.pour(num_poured)
#     return cup.query(query_glass, query_row)

#matrix representation 
def solve(poured, query_glass, query_row):
    DP = [[0.0 for cup in range(i)] for i in range(1, query_row + 2)]
    DP[0][0] = poured
    for row in range(query_row + 1):
        for cup in range(row + 1):
            remainder = (DP[row][cup] - 1.0)/2.0
            if remainder > 0:
                DP[row+1][cup] = remainder
                DP[row+1][cup + 1] = remainder
    return min(1 , DP[query_row][query_glass])


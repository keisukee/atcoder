import sys
sys.setrecursionlimit(500000)

N = list(map(int, input().split()))
heights = list(map(int, input().split()))

max_count = 0

def calculate_max_area(heights):
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            current_height = heights[stack.pop()]
            current_width = i - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        stack.append(i)

    while stack[-1] != -1:
        current_height = heights[stack.pop()]
        current_width = len(heights) - stack[-1] - 1
        max_area = max(max_area, current_height * current_width)
    return max_area

max_count = calculate_max_area(heights)

print(max_count)

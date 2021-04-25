one = list(input())
two = list(input())
three = list(input())

keys = {}
remain_keys = {i: True for i in range(0, 10)}

for char in one:
    keys[char] = -1
for char in two:
    keys[char] = -1
for char in three:
    keys[char] = -1

def is_head(one, two, three, char):
    return one[0] == char or two[0] == char or three[0] == char

# one, two, three, keys, keys_list, idx, remain_keys
def solve_sudoku(keys_list, combi, idx, used_nums):
    # [0,1,...,9]
    if idx == len(keys_list):
        result, combi = meet_condition(one, two, three, combi)
        # print('result', result)
        if result:
            for c in combi:
                print(c)
        return result

    for num in range(0, 10):
        if num in used_nums:
            continue

        # 先頭の場合は0を使用しない
        if num == 0 and is_head(one, two, three, keys_list[idx]):
            continue

        used_nums[num] = True
        combi[keys_list[idx]] = num
        if solve_sudoku(keys_list, combi, idx + 1, used_nums):
            return True
        combi[keys_list[idx]] = -1
        del used_nums[num]

    return False

def meet_condition(one, two, three, combi):
    num_one = [str(combi[char]) for char in one]
    num_one = int(''.join(num_one))

    num_two = [str(combi[char]) for char in two]
    num_two = int(''.join(num_two))

    num_three = [str(combi[char]) for char in three]
    num_three = int(''.join(num_three))
    # print('num_one', num_one)
    # print('num_two', num_two)
    # print('num_three', num_three)
    result = [num_one, num_two, num_three]
    return num_one + num_two == num_three, result

keys_list = list(keys.keys())
combi = {}
used_nums = {}
if solve_sudoku(keys_list, combi, 0, used_nums):
    # print('solve')
    pass
else:
    print('UNSOLVABLE')
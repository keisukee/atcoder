from collections import Counter
K = int(input())
one = list(input())
two = list(input())
one.pop()
two.pop()
one = list(map(int, one))
two = list(map(int, two))
total = Counter(one + two)
one_counter = Counter(one)
two_counter = Counter(two)

def calc_score(cards_counter):
    score = 0
    for i in range(1, 10):
        if i in cards_counter:
            score += i * (10 ** cards_counter[i])
        else:
            score += i
    # print('score', score)
    return score

def can_win(one, two, total, max_count, num_one, num_two):
    if total[num_one] == max_count or total[num_two] == max_count:
        return False
    if num_one == num_two and total[num_one] >= max_count-1:
        return False

    one[num_one] += 1
    two[num_two] += 1
    one_score = calc_score(one)
    two_score = calc_score(two)
    one[num_one] -= 1
    two[num_two] -= 1

    return one_score > two_score

win_count = 0

for i in range(1, 10):
    for j in range(1, 10):
        if can_win(one_counter, two_counter, total, K, i, j):
            if i == j:
                remain = K - total[i]
                win_count += (remain * (remain-1))
            else:
                win_count += (K-total[i]) * (K-total[j])

# print(win_count)
remain_card_total_count = 9 * K - 8
print(win_count / (remain_card_total_count * (remain_card_total_count-1)) )
N, M = list(map(int, input().split()))
friendsList = [[] for _ in range(N)]
friendsOfFriendsCount = [0 for _ in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    friendsList[a-1].append(b-1)
    friendsList[b-1].append(a-1)

for idx, friends in enumerate(friendsList):
    count = 0
    notCountList = set(friends + [idx])
    # print('notCountList', notCountList)
    for friend in friends:
        for friendOfFriend in friendsList[friend]:
            if friendOfFriend in notCountList:
                continue
            # print('count', idx, friendOfFriend)
            notCountList.add(friendOfFriend)
            count += 1
    friendsOfFriendsCount[idx] = count

# for i in range(len(friendsList)):
#     print(str(i) + '.', friendsList[i])
# print('')
# for i in range(len(friendsOfFriendsCount)):
#     print(str(i) + '.', friendsOfFriendsCount[i])

for i in range(len(friendsOfFriendsCount)):
    print(friendsOfFriendsCount[i])

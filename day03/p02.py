import collections

schedule = [(6, 8), (7, 10), (11, 12), (6, 7), (10, 12), (8, 10), (7, 8), (8, 9), (9, 12),
            (9, 10), (6, 12), (10, 11)]


# solution 1
def find_best_time():
    schedule.sort()
    time_dict = []
    for i in schedule:
        # i[0] i[1] 의 차이만큼 dict에 1씩 추가. i[0] <= < i[1]
        for j in range(i[0], i[1]):
            time_dict.append(j)
    print('celebs\' time ::', time_dict)
    cnt = collections.Counter(time_dict)
    print('end?', cnt)  # Counter({9: 5, 7: 4, 8: 4, 10: 4, 11: 4, 6: 3})
    print('end?', cnt.most_common(1))  # [(9, 5)]
    print('best time to meet celebrities is', cnt.most_common(1)[0][0], 'o\' clock')  # 9


# solution 2
def fine_best_time2():
    schedule.sort()
    time_dict = []
    index = 0
    while index < len(schedule):
        for i in range(schedule[index][0],
                       schedule[index][1]):
            time_dict.append(i)
        index += 1
    answer = collections.Counter(time_dict).most_common(1)[0][0]
    print('best time to meet celebrities is', answer, 'o\' clock')


# find_best_time()
fine_best_time2()

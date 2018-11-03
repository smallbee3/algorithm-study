# p.237


europe = {}
europe['W'] = [0.5, 7]
europe['G'] = [0.5, 6]
europe['N'] = [1, 9]
europe['B'] = [2, 9]
europe['S'] = [0.5, 8]
# 아래처럼 값이 주어지면 탐욕알고리즘의 한계를 보여준다. (만족이 더 낮아짐)
# europe['S'] = [1, 15]


def greedy_travel():

    traveling_days = 2
    traveling_nation_list = []
    not_traveling_nation_list = []

    satisfiction = 0
    days_sum = 0

    # 총 합산 여행 일 수가 여행 가능 일 수와 같을 때 (넘는 것은 아래 코드에서 이미 제외됨)
    # 또는 모든 여행가능 국가를 고려해서 더 이상 고려할 국가가 없을 때 while문 종료
    while days_sum < traveling_days and\
            len(traveling_nation_list + not_traveling_nation_list) != len(europe):

        # 계산한 value가 가장 큰 best_nation 찾기
        max_value = 0
        best_nation = None
        for nation in europe:
            # 만족 / 여행 일수를 통해 얻은 value값으로 best_nation 판단
            # (책 답안에서는 만족만으로 추측)
            value = europe[nation][1] / europe[nation][0]
            if nation not in (traveling_nation_list + not_traveling_nation_list) \
                    and value > max_value:
                max_value = value
                best_nation = nation

        # best_nation의 여행 일수가 남은 여행 일수보다 적으면 여행하고
        if traveling_days - days_sum >= europe[best_nation][0]:
            days_sum += europe[best_nation][0]
            satisfiction += europe[best_nation][1]
            traveling_nation_list.append(best_nation)
        # 그렇지 않다면 현재 여행 일정 상 여행을 가지 못하는 국가 리스트에 추가한다.
        else:
            not_traveling_nation_list.append(best_nation)

    print(f'여행 일수: {days_sum}')
    print(f'여행 만족도: {satisfiction}')
    print(f'여행 국가: {traveling_nation_list}')
    print(f'여행 가려다가 고려했지만 일정상 못간 국가: {not_traveling_nation_list}')


greedy_travel()

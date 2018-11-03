
# Hash table for storing stations
stations = {}

# Station name & the state where people can hear the station's broad cast
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])


def greedy():
    # states set that we are going to broadcast
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

    # The list of visited staion
    final_stations = set()

    while states_needed:

        best_station = None
        states_covered = set()

        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)
        # best_station을 stations hash table에서 빼지 않아도 된다
        # 위 for문에서 이미 best_station으로 정해진 station을 다시 검사한다고 하더라도
        # 해당 station이 cover할 수 있는 state가 없기 때문에 그냥 지나가고 만다.

    return final_stations


print(greedy())

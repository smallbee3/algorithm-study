
# (1) Graph
graph = {}
# node start
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# node a
graph['a'] = {}
graph['a']['final'] = 1
# node b
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['final'] = 5
# node final
graph['final'] = {}

# (2) Cost
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['final'] = infinity
# 내가 추가한 것
costs['start'] = 0

# (3) Parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# (4) Processed
processed = []


# 책 내용을 잘못이해하고 가장 가격이 싼 노드가 아니라
# 가장 최근 선택한 노드에서 가장 가중치가 작은
# node를 고르는 것으로 착각하고 만든 불필요한 코드

# def closest(node):
#     key_list = list(graph[node].keys())
#     close_key = key_list[0]
#     close_value = graph[node][close_key]
#     for key in key_list[1:]:
#         if close_value > graph[node][key]:
#             close_value = graph[node][key]
#             close_key = key
#     return close_key


def update_costs_and_parents(node):

    neighbor_list = list(graph[node].keys())
    for i in neighbor_list:
        if costs[i] > graph[node][i] + costs[node]:
            costs[i] = graph[node][i] + costs[node]
            parents[i] = node


def next_node(node_dict):
    for i in processed:
        if i in node_dict:
            del node_dict[i]

    min_key = list(node_dict.keys())[0]
    min_value = costs[min_key]
    for key in list(node_dict.keys())[1:]:
        if min_value > costs[key]:
            min_value = costs[key]
            min_key = key
    return min_key


def dijkstra(str, fin):

    # next_node 함수에서 쓰이는 node_dict를 여기서 만들어서 계속해서 del node_dict 과정이
    # 중복되지 않도록 함.
    # But, 이 코드가 next_node 내부가 아닌 밖에 동떨어져 있다는 점에서 좀 꺼림직함..
    node_dict = graph.copy()
    del node_dict[str]
    del node_dict[fin]

    while len(graph.keys()) - 2 > len(processed):
        print(costs)
        print(parents)
        node = next_node(node_dict)
        print(node)

        update_costs_and_parents(node)
        processed.append(node)

    print(f'최종가격: {costs[fin]}')

    shortest_list = [fin]
    node = fin
    while parents[node] != str:
        shortest_list.insert(0, parents[node])
        node = parents[node]
    shortest_list.insert(0, str)
    print(f'경로 : {shortest_list}')


dijkstra('start', 'final')


# 181126 Result after 1 hour of coding
# Till now this is my simplest code ever
# (Above code delete key in graph dict)

def find_the_cheepest_node(costs):
    min_distance = float('inf')
    min_node = None
    # for i in graph.keys():
    for i in costs:
        if i in processed:
            continue
        if costs[i] < min_distance:
            min_distance = costs[i]
            min_node = i
    return min_node


def update_neighbors_costs_and_parents(node):
    # print(graph[node])
    neighbors = graph[node]
    for i in neighbors:
        print(i)
        if costs[i] > costs[node] + graph[node][i]:
            costs[i] = costs[node] + graph[node][i]
            parents[i] = node
            # print(costs[i])


def dijkstras(str, fin):
    final = fin
    node = str
    processed.append(node)

    while len(processed) < len(list(graph.keys())):
        closest_node = find_the_cheepest_node(costs)
        update_neighbors_costs_and_parents(closest_node)
        processed.append(closest_node)

    print(f'costs: {costs[final]}')
    path = []
    while True:
        path.insert(0, final)
        if not parents.get(final):
            break
        final = parents[final]
    print(f'paths: {path}')


dijkstras('start', 'final')

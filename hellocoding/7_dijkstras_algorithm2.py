
# (1) Graph
graph = {}
# node 악보
graph['악보'] = {}
graph['악보']['LP'] = 5
graph['악보']['포스터'] = 0
# node LP
graph['LP'] = {}
graph['LP']['기타'] = 15
graph['LP']['드럼'] = 20
# node 포스터
graph['포스터'] = {}
graph['포스터']['기타'] = 30
graph['포스터']['드럼'] = 35
# node 기타
graph['기타'] = {}
graph['기타']['피아노'] = 20
# node 드럼
graph['드럼'] = {}
graph['드럼']['피아노'] = 10
# node final
graph['피아노'] = {}

# (2) Cost
infinity = float('inf')
costs = {}
costs['LP'] = 5
costs['포스터'] = 0
costs['기타'] = infinity
costs['드럼'] = infinity
costs['피아노'] = infinity
# 내가 추가한 것
costs['악보'] = 0

# (3) Parents
parents = {}
parents['LP'] = '악보'
parents['포스터'] = '악보'
parents['기타'] = None
parents['드럼'] = None
parents['피아노'] = None

# (4) Processed
processed = []


# 181126 My new code

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


def dijkstra(str, fin):
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


dijkstra('악보', '피아노')


# def update_costs_and_parents(node):
#     neighbor_list = list(graph[node].keys())
#     for i in neighbor_list:
#         if costs[i] > graph[node][i] + costs[node]:
#             costs[i] = graph[node][i] + costs[node]
#             parents[i] = node
#
#
# def next_node(node_dict):
#     for i in processed:
#         if i in node_dict:
#             del node_dict[i]
#
#     min_key = list(node_dict.keys())[0]
#     min_value = costs[min_key]
#     for key in list(node_dict.keys())[1:]:
#         if min_value > costs[key]:
#             min_value = costs[key]
#             min_key = key
#     return min_key
#
#
# def dijkstra(str, fin):
#
#     # next_node 함수에서 쓰이는 node_dict를 여기서 만들어서 계속해서 del node_dict 과정이
#     # 중복되지 않도록 함.
#     # But, 이 코드가 next_node 내부가 아닌 밖에 동떨어져 있다는 점에서 좀 꺼림직함..
#     node_dict = graph.copy()
#     del node_dict[str]
#     del node_dict[fin]
#
#     while len(graph.keys()) - 2 > len(processed):
#         print(costs)
#         print(parents)
#         node = next_node(node_dict)
#         print(node)
#
#         update_costs_and_parents(node)
#         processed.append(node)
#
#     print(f'최종가격: {costs[fin]}')
#
#     shortest_list = [fin]
#     node = fin
#     while parents[node] != str:
#         shortest_list.insert(0, parents[node])
#         node = parents[node]
#     shortest_list.insert(0, str)
#     print(f'경로 : {shortest_list}')
#
#
# dijkstra('악보', '피아노')

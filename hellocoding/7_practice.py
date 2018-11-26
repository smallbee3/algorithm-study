
# 1. A
# (1) Graph
graph = {}
# node start
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
# node a
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
# node b
graph['b'] = {}
graph['b']['d'] = 7
# node c
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['final'] = 3
# node d
graph['d'] = {}
graph['d']['final'] = 1
# node final
graph['final'] = {}

# (2) Cost
infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['final'] = infinity

# (3) Parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['b'] = None
parents['fin'] = None

# (4) Processed
processed = []


# 2. B
# (1) Graph
# graph = {}
# # node start
# graph['start'] = {}
# graph['start']['a'] = 10
# # node a
# graph['a'] = {}
# graph['a']['c'] = 20
# # node b
# graph['b'] = {}
# graph['b']['a'] = 1
# # node c
# graph['c'] = {}
# graph['c']['b'] = 1
# graph['c']['final'] = 30
# # node final
# graph['final'] = {}
#
# # (2) Cost
# infinity = float('inf')
# costs = {}
# costs['a'] = 10
# costs['b'] = infinity
# costs['c'] = infinity
# costs['final'] = infinity
#
# # (3) Parents
# parents = {}
# parents['a'] = 'start'
# parents['b'] = None
# parents['c'] = None
# parents['b'] = None
# parents['fin'] = None
#
# # (4) Processed
# processed = []


# 3. C
# (1) Graph
# graph = {}
# # node start
# graph['start'] = {}
# graph['start']['a'] = 2
# graph['start']['b'] = 2
# # node a
# graph['a'] = {}
# graph['a']['b'] = 2
# # node b
# graph['b'] = {}
# graph['b']['c'] = 2
# graph['b']['final'] = 2
# # node c
# graph['c'] = {}
# graph['c']['a'] = -1
# graph['c']['final'] = 2
# # node final
# graph['final'] = {}
#
# # (2) Cost
# infinity = float('inf')
# costs = {}
# costs['a'] = 2
# costs['b'] = 2
# costs['c'] = infinity
# costs['d'] = infinity
# costs['final'] = infinity
#
# # (3) Parents
# parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['c'] = None
# parents['fin'] = None
#
# # (4) Processed
# processed = []


def update_costs_and_parents(node):
    neighbor_list = list(graph[node].keys())
    for i in neighbor_list:
        if costs[i] > graph[node][i] + costs[node]:
            costs[i] = graph[node][i] + costs[node]
            parents[i] = node


def next_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if node not in processed and lowest_cost > costs[node]:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(str, fin):
    node = next_node(costs)
    while node is not None:
        print(costs)
        print(parents)

        update_costs_and_parents(node)
        processed.append(node)
        node = next_node(costs)
        print(node)

    print(f'최종가격: {costs[fin]}')
    shortest_list = [fin]
    node = fin
    while parents[node] != str:
        shortest_list.insert(0, parents[node])
        node = parents[node]
    shortest_list.insert(0, str)
    print(f'경로 : {shortest_list}')


dijkstra('start', 'final')


# 181027 다익스트라 알고리즘에서 배우고 갈 것.
# 1. list.insert(0, element)
# 2. 해시테이블 안의 해시테이블 (딕셔너리 안의 딕셔너리)
#     Graph
#     graph = {}
#     # node start
#     graph['start'] = {}
#     graph['start']['a'] = 2
#     graph['start']['b'] = 2
#
# 3. graph[node].keys()
#
# 4. lowest_cost = float('inf')
#
# 5. node = next_node(costs)처럼 costs를 parameter로 전달하는 것과 
#    전달된 costs의 내부 값을 변경할 수 있는 사실

# 필수 알고리즘 with 파이썬  *정오표 리스트*


필수 알고리즘 with 파이썬 책으로 열심히 코딩테스트 공부를 하고 있는 독자로서\
좋은 책의 내용에도 불구하고 오탈자 또는 기타 잘못된 내용 때문에 어려움을 겪는 분들이 있을 것 같다는 생각에\
제가 정리한 1판 1쇄의 정오표를 공유하고자 합니다.

<br>

*(본 내용은 이 책의 저자나 출판사와 아무 관련없는 비공식 문서입니다. 틀린 내용이 있을 수 있습니다.)*

*("위에서/아래서몇번째줄"이라는 안내문구는 공백을 제외하고 세었습니다.)*

<br>

*최근 업데이트 : 2018.11.27*


<br>


## p.28
(위에서5번째줄)

이처럼 알고리즘을 최적화하기 위해서는 알고리즘의 `전체 성능이` O 표기법을 먼저 구하고,

> **전체 성능인**
<br>


## p.32
(위에서7번째줄)

`print`

> **print()**
<br>



## p.36
(아래서1번째줄)

그리고 나서 인수로 받은 data를 저장할 `node_node`를 선언한다.

> **new_node**
<br>



## p.47
(아래서7번째줄)

`print`

> **print()**
<br>



## p.52
(위에서15번째줄)

 ```python
 # 첫번 째 노드를 삭제하는 예외상황 처리
 if pre_node.data == del_data:
	# 첫번 째 노드를 두번 째 노드로 가리키게 한다
	node1 = next_node
	del pre_node
	return
```
`node1` = next_node

> **node_A**
<br>



## p.61
(아래서6번째줄)

연산자 스택이 `비워`있으므로

> **비어**
<br>



## p.62
(위에서1번째그림)

`1 * 2 + 3`

> **1 + 2 * 3**
<br>



## p.62
(아래서2번째줄)

연산자보다 `더 크다면` 어떻게 될까?

> **우선순위가 더 높다면**
<br>



## p.64
(위에서1번째줄)

`while(i < len):`

> while i < len:
<br>



## p.64
(위에서6번째줄)

괄호 연산이 있는 경우는 `do-while`문을 추가로 사용하기 때문이다.

> **do-while문의 기능을 수행하는 while True와 if ~ break 문울** 추가로 사용하기 때문이다.\
(python에는 do-while문이 없음)
<br>



## p.66
(위에서12번째줄)

```python
def get():
    return queue.pop()
```
`return queue.pop()`

> return queue.pop(0)
<br>



## p.66
(아래서2번째줄)

앞의 코드는 `stack`이라는 이름의 리스트를 선언하고, 파이썬의 리스트의 멤버 함수인 append()를 이용\
하여 `스택`의 `push()` 함수의 기능을 구현하고 있다. 또한 `스택`의 `pop()` 기능은 동일한 이름의 pop() 멤버

> 앞의 코드는 **queue**이라는 이름의 리스트를 선언하고, 파이썬의 리스트의 멤버 함수인 append()를 이용\
하여 **큐**의 **put()** 함수의 기능을 구현하고 있다. 또한 **큐**의 **get()** 기능은 동일한 이름의 pop() 멤버
<br>



## p.67
(위에서5번째줄)

현재 queue의 모습\
[1, 2, 3, 4]\
POP > `4`\
POP > `3`\
POP > `2`\
POP > `1`

> POP > 1\
> POP > 2\
> POP > 3\
> POP > 4
<br>



## p.80
(아래서2번째줄)

트리 구조에서 트리 구조를 `순회하는 방법에는` 가운데 노드를 먼저 방문하고

> **전위 순회하는 방법은**
<br>


## p.81
(위에서2번째줄)

`이와 같이` 순서로 방문을 하게 되면 방문한 결과는 다음과 같은 순서가 된다.

> **이와 같은**
<br>



## p.81
(위에서7번째줄)

```python
def preorder_traverse(node):
    if node is None: return
    print(node.data, end='-> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)
```

> print(node.data, end='-> ') **if node.data != 'G' else print(node.data)**
<br>



## p.83
(위에서5번째줄)

```python
def inorder_traverse(node):
    if node is None: return
    preorder_traverse(node.left)
    print(node.data, end='-> ')
    preorder_traverse(node.right)
```

> print(node.data, end='-> ') **if node.data != 'G' else print(node.data)**
<br>



## p.84
(위에서1번째줄)

```python
def postorder_traverse(node):
    if node is None: return
    preorder_traverse(node.left)
    preorder_traverse(node.right)
    print(node.data, end='-> ')
```

> print(node.data, end='-> ') **if node.data != 'A' else print(node.data)**
<br>



## p.85
(위에서5번째줄)

```python
def levelorder_traverse(node):
    global levelq
    levelq.append(node)
    while len(levelq) != 0;
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data, end='-> ')
        # child put
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)
```

print(visit_node.data, end='-> ')

> print(visit_node.data, end='-> ') if visit_node.data != 'G' else print(visit_node.data)
<br>



## p.87
(위에서11번째줄)

```python
def init_tree():
global root

new_node = Node('A')
root = new_node

new_node = Node('B')
root.left = new_node

new_node = Node('C')
root.right = new_node

new_node_1 = Node('D')
new_node_2 = Node('E')
node = root.left
node.left = new_node_1
node.right = new_node_2

new_node_1 = Node('F')
new_node_2 = Node('G')
node = root.right
node.left = new_node_1
node.right = new_node_2
```

> 아래 코드로 수정
```python
def init_tree():
    global root

    new_node = Node('A')
    root = new_node

    new_node = Node('B')
    root.left = new_node

    new_node = Node('C')
    root.right = new_node

    new_node_1 = Node('D')
    new_node_2 = Node('E')
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node('F')
    new_node_2 = Node('G')
    node = root.right
    node.left = new_node_1
    node.right = new_node_2
```
<br>



## p.88
(위에서11번째줄)
```
if __name__ == '__main__':
init_tree()
print("<Preorder Traverse>")
preorder_traverse(root)
print("\n")
print("<Inorder Traverse>")
inorder_traverse(root)
print("\n")
print("<Postorder Traverse>")
postorder_traverse(root)
print("\n")
print("<Leveorder Traverse>")
levelorder_traverse(root)
print("\n")
```

> 아래 코드로 수정
```python
if __name__ == '__main__':

    init_tree()
    print("<Preorder Traverse>")
    preorder_traverse(root)
    print("\n")
    print("<Inorder Traverse>")
    inorder_traverse(root)
    print("\n")
    print("<Postorder Traverse>")
    postorder_traverse(root)
    print("\n")
    print("<Levelorder Traverse>")
    levelorder_traverse(root)
    print("\n")

    levelorder_traverse(node)

```
<br>



## p.91
(아래서6번째줄)

```python
if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1,10))
    print("<Before Sort>")
    print(list)

```

> range(10) -> range(100)\
> random.randint(1,10) -> random.randint(1,100)
>
> 아래 코드로 수정


```python
if __name__ == '__main__':
    list = []
    for i in range(100):
        list.append(random.randint(1,100))
    print("<Before Sort>")
    print(list)

```
<br>



## p.94
(아래서6번째줄)

8.3 삽입 정렬 알고리즘(`Insert` Sort Algorithm)

> **Insertion**
<br>



## p.104
(위에서5번째줄)

앞의 시간들은 `선택` 정렬 프로그램의 절대적인 실행 시간이 될 수 없다.

> **거품**
<br>



## p.110
(위에서2번째줄)

좋지않은 알고리즘은 거품 정렬이지만 `일반 모드의` 경우에는 선택 정렬이 삽입 정렬보다 성능이 더 좋았

> **일반적인**
<br>

from collections import deque

def person_is_seller(name: str):
    return name[-1] == 'm'

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johny'] = []


def graph_search():
    search_deque = deque()
    search_deque += graph['you']
    searched = [] # 存储已经搜索过的人，避免出现死循环的情况，因为可能会互相指
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is seller')
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    return False

graph_search()


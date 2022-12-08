# Greedy Best First Search
# Lambda is used to create anonymous(no name of function) methods in python / java eg:: key = lambda x:x[1]

graph = {
    'a':[('b',12), ('c',4)],
    'b':[('d',7),('e',3)],
    'c':[('f',8),('g',2)],
    'd':[],
    'e':[('h',0)],
    'f':[('h',0)],
    'g':[('h',0)]
}

open = []
closed = []

def gbfs(start, target, graph, open=[], closed=[]):
  if start not in closed:
    print(start)
    closed.append(start)

  open = open + [x for x in graph[start] if x[0][0] not in closed]
  print([x for x in graph[start] if x[0][0] not in closed])
  open.sort(key=lambda x:x[1])
  #print(open)

  if open[0][0] == target:
    print(open[0][0])
  else:
    processing = open[0]
    print(processing)
    open.remove(processing)
    gbfs(processing[0], target, graph, open, closed)

gbfs('a','h',graph)

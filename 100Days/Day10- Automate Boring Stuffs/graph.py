from collections import deque


class Graph():

    def __init__(self):
        self._graph = {}

    def add(self, vertex_st, vertex_end):
        if vertex_st not in self._graph:
            self._graph[vertex_st] = {vertex_end}
        else:
            self._graph[vertex_st].add(vertex_end)
    
    def delete_link(self,vertex_st,vertex_end):
        vertices_to_st = self._graph[vertex_st]
        if(vertex_end in vertices_to_st):
            vertices_to_st.remove(vertex_end)
            return vertex_end
        return None

    def bfs(self, vertex_st):
        visited = []
        qu = deque([vertex_st])
        while(len(qu) != 0):
            vertex_st = qu.pop()
            print('visiting : '+ vertex_st)
            visited.append(vertex_st)
            if vertex_st in self._graph:
                vertices = self._graph[vertex_st]
                for vert in vertices:
                    if vert not in visited and vert not in qu:
                        qu.append(vert)

    def is_reachable(self,vertex_st, vertex_end):
        visited = []
        qu = deque([vertex_st])
        while(len(qu) != 0):
            vertex_st = qu.pop()
            if(vertex_st == vertex_end):
                return True
            visited.append(vertex_st)
            if vertex_st in self._graph:
                vertices = self._graph[vertex_st]
                for vert in vertices:
                    if vert not in visited and vert not in qu:
                        qu.append(vert)
        return False

    @property
    def graph(self):
        return self._graph


if __name__ == "__main__":
    graph = Graph()
    graph.add('a', 'b')
    graph.add('a', 'c')
    graph.add('b', 'c')
    graph.add('c', 'd')
    graph.add('b', 'e')
    print(graph.graph)
    graph.bfs('a')

    print(graph.is_reachable('a','d'))
    print(graph.is_reachable('d','e'))

    print(graph.delete_link('a','c'))
    print(graph.graph)
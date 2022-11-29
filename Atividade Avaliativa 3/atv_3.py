class Grafo:
    

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):

        self.grafo[u-1][v-1] = 1

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])


g = Grafo(7)

g.adiciona_aresta(0, 2)
g.adiciona_aresta(0, 4)
g.adiciona_aresta(1, 3)
g.adiciona_aresta(2, 7)
g.adiciona_aresta(3, 6)
g.adiciona_aresta(4, 5)
g.adiciona_aresta(4, 7)
g.adiciona_aresta(5, 1)
g.adiciona_aresta(5, 7)
g.adiciona_aresta(5, 4)
g.adiciona_aresta(6, 0)
g.adiciona_aresta(6, 2)
g.adiciona_aresta(6, 4)
g.adiciona_aresta(7, 3)
g.adiciona_aresta(7, 5)

g.mostra_matriz()
'''An Internet service provider company wants to lay fiber lines to connect n cities labeled 0 ton-
1. Write a function FiberLink(distance_map) that accepts a weighted adjacency list
distance_map in the following format:-
1 distance_map = {
2
source_index: [(destination_index, distance (km)),
(destination_index, distance)...],
3
4
5
source_index: [(destination_index, distance),
(destination_index, distance),..]
6}
The function returns the minimum length of fiber required to connect all n cities.'''

def kruskal(WList):
    (edges,component,TE)=([],{},[])
    for u in WList.keys():
        edges.extend([(d,u,v) for (v,d) in WList[u]])
        component[u] = u
    edges.sort()
    for (d,u,v) in edges:
        if component[u] != component[v]:
            TE.append((u,v))
            c = component[u]
        for w in WList.keys():
            if component[w] == c:
                component[w] = component[v]
    return(TE)

def FiberLink(distance_map):
    R = kruskal(distance_map)
    S = 0
    for e in R:
        for ed in distance_map[e[0]]:
            if ed[0]==e[1]:
                S += ed[1]
    return S
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))
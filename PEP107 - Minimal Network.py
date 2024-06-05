def saving(network):
    network_sum = 0
    for v1 in range(len(network)):
        for v2 in range(len(network)):
            if network[v1][v2] != "n":
                network_sum += network[v1][v2]
    network_sum = network_sum // 2
    edges = []
    for ver1 in range(len(network)):
        for ver2 in range(len(network)):
            if network[ver1][ver2] != "n":
                edges.append((network[ver1][ver2],ver1,ver2))
    edges = sorted(edges)

    connected_vertices = [0]
    minimal_edges = []
    while len(connected_vertices) < len(network):
        for edge in edges:
            if edge[1] in connected_vertices and edge[2] not in connected_vertices:
                minimal_edges.append(edge)
                connected_vertices.append(edge[2])
                break
    mini = 0
    for min_edge in minimal_edges:
        mini += min_edge[0]
    return network_sum - mini

f = open("0107_network.txt","r")
file = str(f.read())
network = []
current_vertice = []
current_num = ""
for ch in file:
    if ch == "-":
        current_num += "n"
    elif ch == ",":
        if current_num == "n":
            current_vertice.append(current_num)
        else:
            current_vertice.append(int(current_num))
        current_num = ""
    elif ch == "\n":
        if current_num == "n":
            current_vertice.append(current_num)
        else:
            current_vertice.append(int(current_num))
        network.append(current_vertice)
        current_vertice = []
        current_num = ""
    else:
        current_num += ch

print(saving(network))

#answer = 259679

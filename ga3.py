

def three_min_spanning_trees(input_file_path, output_file_path):
    graph, v = get_graph(input_file_path)


    # Step 1: Compute all MSTs with minimal weight w1
    T_mst_matrix, w1 = get_mst(graph, v)

    print(T_mst_matrix, w1)
    pass
    # # Initialize a set to store candidate trees
    # candidates = set()

    # # Step 2: Generate candidates by swapping edges
    # for T in T_mst_list:
    #     for f in graph.edges():
    #         if f not in T.edges():
    #             # Add f to T to form a cycle
    #             cycle = find_cycle(T, f)
    #             for e in cycle:
    #                 if e != f and e in T.edges():
    #                     # Form a new tree by swapping e and f
    #                     T_prime = T.copy()
    #                     T_prime.remove_edge(e)
    #                     T_prime.add_edge(f)
    #                     w_prime = total_weight(T_prime)
    #                     candidates.add((w_prime, T_prime))

    # # Step 3: Remove duplicates and sort candidates by weight
    # unique_candidates = list(candidates)
    # unique_candidates.sort(key=lambda x: (x[0], x[1].edges()))

    # # Step 4: Select T1, T2, and T3 from the sorted candidates
    # T1 = unique_candidates[0][1]
    # w1 = unique_candidates[0][0]
    # T2 = None
    # T3 = None

    # for w, T_candidate in unique_candidates[1:]:
    #     if T_candidate.edges() != T1.edges():
    #         T2 = T_candidate
    #         w2 = w
    #         break

    # for w, T_candidate in unique_candidates[2:]:
    #     if T_candidate.edges() != T1.edges() and T_candidate.edges() != T2.edges():
    #         T3 = T_candidate
    #         w3 = w
    #         break

    # # Output the weights of T1, T2, and T3
    # return w1, w2, w3




def get_graph(input_file_path):
    f = open(input_file_path)
    matrix = []

    N = int(f.readline())

    for i in range(N):
        line = f.readline().strip()
        line = line.replace(',', ' ')

        tokens = line.split()

        row = list(map(int, tokens))

        matrix.append(row)

    f.close()
    return matrix, N

def is_valid_edge(i, j, inMST):
    if i == j:
        return False
    if inMST[i] == inMST[j]:
        return False
    
    return True


def get_mst(matrix, v):
    inMST = [False] * v

    #Starting Vertex
    inMST[0] = True

    MST_edges = []

    edge_count = 0
    mincost = 0

    while edge_count < v -1:

        # Find minimum weight valid edge.
        min_weight = float('inf')
        a = -1
        b = -1
        for i in range(v):
            for j in range(v):
                if matrix[i][j] < min_weight:
                    if is_valid_edge(i, j, inMST):
                        min_weight = matrix[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            print("Edge %d: (%d, %d) cost: %d" % (edge_count, a, b, min_weight))
            edge_count += 1
            mincost += min_weight
            inMST[b] = inMST[a] = True
            MST_edges.append((a,b))

    return inMST, mincost

three_min_spanning_trees('./test2', './outpur1')
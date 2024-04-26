import timeit

start_time = timeit.default_timer()

def shortest_path(graph, start, end):
    memo = {}  # Dictionary untuk menyimpan jarak terpendek dari setiap vertex ke end
    memo[end] = 0  # Jarak dari end ke end adalah 0
    path = {}  # Dictionary untuk menyimpan jalur terpendek dari setiap vertex ke end

    def dp(vertex):
        if vertex in memo:
            return memo[vertex]
        shortest = float('inf')
        next_vertex = None
        for neighbor, distance in graph[vertex].items():
            cost = distance + dp(neighbor)
            if cost < shortest:
                shortest = cost
                next_vertex = neighbor
        memo[vertex] = shortest
        path[vertex] = next_vertex
        return shortest

    dp(start)  # Memanggil fungsi dp untuk mengisi memo dan path

    result = []
    curr_vertex = start
    steps = 0  # Inisialisasi jumlah langkah atau iterasi
    while curr_vertex != end:
        result.append(curr_vertex)
        curr_vertex = path[curr_vertex]
        steps += 1  # Menginkrementasikan jumlah langkah pada setiap iterasi
    result.append(end)

    total_distance = memo[start]  # Jarak terpendek dari start ke end adalah nilai memo[start]

    return result, total_distance, steps

graph = {
    "IS": {"A": 314, "B": 285, "C": 236},
    "A": {"D": 402, "E": 733, "F": 206},
    "B": {"D": 643, "E": 508, "F": 430},
    "C": {"D": 382, "E": 564, "F": 136},
    "D": {"G": 610, "H": 416, "I": 201},
    "E": {"G": 156, "H": 182, "I": 363},
    "F": {"G": 642, "H": 356, "I": 291},
    "G": {"FS": 159},
    "H": {"FS": 168},
    "I": {"FS": 262},
    "FS": {}
}

start = "IS"
end = "FS"
dynamic_path, total_distance, steps = shortest_path(graph, start, end)

print("Bejo's Dynamic Programming Path and Distance")
print("============================================")
print("Path:", ' -> '.join(dynamic_path))
print("Total step:", steps)
print("Total distance:", total_distance, "meter")

stop_time = timeit.default_timer()
execution = stop_time - start_time

print("\nLama eksekusi program:", '{:.10f}'.format(execution), "detik")

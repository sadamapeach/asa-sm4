import timeit

start_time = timeit.default_timer()

def shortest_path(graph, start, end):
    result = []  
    result.append(start) 
    total_distance = 0  
    steps = 0  # Variable to keep track of the step count
    
    while end not in result:
        steps += 1  # Increment step count
        curr_vertex = result[-1]
        short_path = min(graph[curr_vertex].values())
        total_distance += short_path  
        for vertex, distance in graph[curr_vertex].items():
            if distance == short_path:
                result.append(vertex)
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
greedy_path, total_distance, steps = shortest_path(graph, start, end)

print("Bejo's Greedy Path and Distance")
print("===============================")
print("Path:", ' -> '.join(greedy_path))
print("Total step:", steps)
print("Total distance:", total_distance, "meter")

stop_time = timeit.default_timer()
execution = stop_time - start_time

print("\nLama eksekusi program:", '{:.10f}'.format(execution), "detik")
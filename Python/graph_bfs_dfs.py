class Vertex:
	def __init__(self, key):
		self.key = key
		self.adj = []

	def add_neighbor(self, neighbor):
		if neighbor not in self.adj:
			self.adj.append(neighbor)

class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, key):
		if key not in self.vertices:
			self.vertices[key] = Vertex(key)

	def add_edge(self, from_key, to_key):
		if from_key not in self.vertices:
			self.add_vertex(from_key)
		if to_key not in self.vertices:
			self.add_vertex(to_key)
		self.vertices[from_key].add_neighbor(to_key)
		self.vertices[to_key].add_neighbor(from_key)  # For undirected graph

	def get_vertices(self):
		return list(self.vertices.keys())

	def get_edges(self):
		edges = []
		seen = set()
		for vertex in self.vertices.values():
			for neighbor in vertex.adj:
				if (neighbor, vertex.key) not in seen:
					edges.append((vertex.key, neighbor))
					seen.add((vertex.key, neighbor))
		return edges
	
	def bfs(self, start_key):
		if start_key not in self.vertices:
			return []

		visited = set()
		queue = [start_key]
		order = []

		while queue:
			current = queue.pop(0)
			if current not in visited:
				visited.add(current)
				order.append(current)
				queue.extend([n for n in self.vertices[current].adj if n not in visited])

		return order
	
	def dfs(self, start_key):
		if start_key not in self.vertices:
			return []

		visited = set()
		stack = [start_key]
		order = []

		while stack:
			current = stack.pop()
			if current not in visited:
				visited.add(current)
				order.append(current)
				stack.extend([n for n in self.vertices[current].adj if n not in visited])

		return order
	
if __name__ == "__main__":
	g = Graph()
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 4)
	g.add_edge(3, 4)
	g.add_edge(4, 5)

	print("Vertices:", g.get_vertices())
	print("Edges:", g.get_edges())
	print("BFS from 1:", g.bfs(1))
	print("DFS from 1:", g.dfs(1))
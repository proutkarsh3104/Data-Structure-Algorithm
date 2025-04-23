def add_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
    return False
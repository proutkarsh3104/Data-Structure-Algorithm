def remove_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        except ValueError:
            pass
        return True
    return False
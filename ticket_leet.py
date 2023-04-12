path_options=[]
path=[]
visited=[]
dict={}


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        for i in flights:
            try:
                if len(dict[i[0]]) > 0:
                    l1 = [i[1], i[2]]
                    l2 = dict[i[0]]
                    l2.append(l1)
                    dict[i[0]] = l2
            except:
                dict[i[0]] = [[i[1], i[2]]]
        flight_all_paths = self.search(flights, src, dst, k, dict, path, visited,n)
        final_paths = self.max_hops_path(flight_all_paths, k)
        final_cost = self.calc_cost(final_paths)

        return final_cost

    def search(self,flights, src, dst, k, dict, path, visited,n):
        for k, v in dict.items():
            if k == src:
                for i in v:
                    if i[0] not in path and i[0] not in visited:
                        path.append(k)
                        visited.append(k)
                    if i[0] not in visited:
                        visited.append(i[0])
                        path.append(i[0])
                        if self.dfs_graph(visited, dict[i[0]],path):
                            path_options.append(path)
        backtrack_array = path[:]
        if len(backtrack_array) > 3:

            for i in range(1, len(backtrack_array) - 2, 1):
                path, visited = backtrack_array[0:i + 1], backtrack_array[0:i + 2]
                if self.dfs_graph(visited, dict[i],path):
                    path_options.append(path)

        elif len(backtrack_array) == 3:
            path = backtrack_array[0:2]
            visited = backtrack_array[0:3]
            node = dict[backtrack_array[1]]
            if self.dfs_graph(visited, node,path):
                path_options.append(path)
            path = backtrack_array[0:1]
            visited = backtrack_array[0:2]
            node = dict[backtrack_array[0]]
            if self.dfs_graph(visited, node,path):
                path_options.append(path)
        else:
            path = backtrack_array[0]
            visited = backtrack_array[0:2]
            node = backtrack_array[1]
            if self.dfs_graph(visited, node,path):
                path_options.append(path)
        return path_options

    def dfs_graph(self, visited, graph_node,path):
        try:

            for i in graph_node:
                if i[0] == dst and i[0] not in visited:
                    path.append(i[0])
                    visited.append(i[0])
                    # self.cost=self.cost+i[1]
                    # self.path.append(self.cost)
                    return True
                else:

                    if i[0] not in visited:
                        # self.cost=self.cost+i[1]
                        path.append(i[0])
                        visited.append(i[0])
                        if self.dfs_graph(visited, dict[i[0]],path):
                            return True
        except:
            return False

    def max_hops_path(self, flight_all_paths, max_hops):

        final_paths = []
        for i in flight_all_paths:
            l1 = i[:]
            l1.remove(src)
            l1.remove(dst)
            if len(l1) == max_hops:
                final_paths.append(i)
        return final_paths

    def calc_cost(self, final_paths):
        cost = 0
        for i in (final_paths):
            for j, k in zip(i, range(0, len(i))):
                if k + 1 != len(i):
                    for m in dict[j]:
                        if [j, m[0]] == [j, i[k + 1]]:
                            cost = cost + m[1]
        return cost

if __name__=="__main__":
    flights =\
    [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src=0
    dst=3
    k=1
    n=4
    sol=Solution()
    print(sol.findCheapestPrice(n, flights, src, dst, k))

import copy


class solution():
    def __init__(self,flights,source,dest,dict):
        self.source=source
        self.dest=dest
        self.flights=flights
        self.visited=[]
        self.path=[]
        self.cost=0
        self.path_options=[]
        dict = {}
        for i in self.flights:
            try:
                if len(dict[i[0]]) > 0:
                    l1 = [i[1], i[2]]
                    l2 = dict[i[0]]
                    l2.append(l1)
                    dict[i[0]] = l2
            except:
                dict[i[0]] = [[i[1], i[2]]]
        self.dict=dict

    def search(self):
        for k,v in self.dict.items():
            if k==self.source:
                for i in v:
                    if i[0] not in self.path and i[0] not in self.visited:
                        self.path.append(k)
                        self.visited.append(k)
                    if i[0] not in self.visited:
                        self.visited.append(i[0])
                        self.path.append(i[0])
                        self.cost=self.cost+i[1]
                        if self.dfs_graph(self.visited,self.dict[i[0]]) :
                            self.path_options.append(self.path)
        backtrack_array=list.copy(self.path)
        if len(backtrack_array)>3:

            for i in range(1,len(backtrack_array)-2,1):
                self.path,self.visited,self.cost=backtrack_array[0:i+1],backtrack_array[0:i+2],0
                if self.dfs_graph(self.visited,self.dict[i]):
                    self.path_options.append(self.path)

        elif len(backtrack_array)==3:
            self.path=backtrack_array[0:2]
            self.visited=backtrack_array[0:3]
            node=self.dict[backtrack_array[1]]
            if self.dfs_graph(self.visited,node):
                self.path_options.append(self.path)
            self.path=backtrack_array[0:1]
            self.visited = backtrack_array[0:2]
            node=self.dict[backtrack_array[0]]
            if self.dfs_graph(self.visited, node):
                self.path_options.append(self.path)
        else:
            self.path=backtrack_array[0]
            self.visited = backtrack_array[0:2]
            node = backtrack_array[1]
            if self.dfs_graph(self.visited, node):
                self.path_options.append(self.path)
        return self.path_options

    def dfs_graph(self,visited,graph_node):
        try:
            for i in graph_node:
                if i[0]==self.dest and i[0] not in self.visited :
                    self.path.append(i[0])
                    self.visited.append(i[0])
                    # self.cost=self.cost+i[1]
                    # self.path.append(self.cost)
                    return True
                else:

                    if i[0] not in self.visited:
                        # self.cost=self.cost+i[1]
                        self.path.append(i[0])
                        self.visited.append(i[0])
                        if self.dfs_graph(self.visited,self.dict[i[0]]):
                            return True
        except:
            return False
    def max_hops_path(self,flight_all_paths,max_hops):
        final_paths=[]
        for i in flight_all_paths:
            l1=copy.deepcopy(i[:])
            l1.remove(self.source)
            l1.remove(self.dest)
            if len(l1)==max_hops:
                final_paths.append(i)
        return final_paths

    def calc_cost(self,final_paths):
        cost=0
        for i in (final_paths):
            for j,k in zip(i,range(0,len(i))):
                if k+1!=len(i):
                    for m in self.dict[j]:
                        if [j,m[0]]==[j,i[k+1]]:
                            cost=cost+m[1]



        return cost



            

if __name__=="__main__":
    flights, source, dest, dict,max_hops=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,{},1
    sol=solution(flights, source, dest, dict)
    flight_all_paths=sol.search()
    final_paths=sol.max_hops_path(flight_all_paths,max_hops)
    print(flight_all_paths,final_paths)
    print(sol.calc_cost(final_paths))





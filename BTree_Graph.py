#loading Btree list into a Graph
class Solution:
    def __init__(self,root):
        self.graph_dict={}
        self.root=root
        self.pairs=[]
    def convert_btree_graph(self):
        for i in range(len(root[1:])):
            if i % 2 == 0 and i != len(root[1:]) - 1:
                self.pairs.append([root[1:][i],root[1:][i+1]])

        return self.pairs


    def graph_pairs(self):
        for i,j in zip(self.root,self.pairs):
            self.graph_dict[i]=j
        return self.graph_dict






if __name__=="__main__":
    root = [1, 2, 3, "", 5]
    sol=Solution(root)
    print(sol.convert_btree_graph())
    print(sol.graph_pairs())
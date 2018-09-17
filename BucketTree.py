from Bucket import *
from Node import *
from Rule import *

class BucketTree():
    def __init__(self, RuleSet = None, thr = 5):
        self.root = Node()

        self.dims = self.gen_dim()
        # dim got

        self.root.splitNode(dims, thr)

        self.thr = thr

    root = Node()       # The root node of bucketTree
    dims = []           # The dimension of cut
    thr = 0             # The threshold of one bucket

    # cal the dim of split
    def gen_dim(self):
        dims = []
        init = [0, 0, 0, 0]
        for x in range(4):
            for y in range(4):
                init[x] += 1
                init[y] += 1
                dims.append(init)
                init = [0, 0, 0, 0]
        return dims

# Problem Link:https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

# method 1: Hash Map + Dynamic Array(list)
class RandomizedSet:

    def __init__(self):
        self.numlist = []  # store elements
        self.nummap = {}  # map its index in numlist

    def insert(self, val: int) -> bool:
        if val in self.nummap:
            return False

        # new element placed at the end of list
        self.nummap[val] = len(self.numlist)
        self.numlist.append(val)
        return True

    def remove(self,
               val: int) -> bool:  # find the index of element we want to remove -> swap with the last element of the list, update map -> pop the last
        if val not in self.nummap:
            return False

        index = self.nummap[val]
        last = self.numlist[-1]
        self.numlist[index] = last
        self.nummap[last] = index

        self.numlist.pop()

        del self.nummap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numlist)

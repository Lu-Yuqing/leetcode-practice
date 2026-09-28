# LeetCode Practice
when do binary tree related questions, always think of if it can be solved by recursion.

# Tree
Binary Search Tree(BST): 左大右小，左子树的每个节点值都要小于这个节点的值，右子树的每个节点的值都要大于这个节点的值
BST in-order Traversal 的结果是单调递增序列

# Linked List
singly linked list: 1 pointer per node(next), forward only, deletcion: O(n) without predecessor pointer, O(1) with predecessor

doubly linked list: 2 ponters per node(next, prev), forward & backward, delection: O(1) using node.prev

# Algorithms - Kahn: Indegree + BFS, Topological sorting
每次只做眼前没有任何限制的事情；做完之后，把依赖这件事情的后续限制通通减掉；一旦某件事的限制降为 0，就把它拿来继续做

Kahn算法标准四部
统计所有节点的入度：
扫描所有依赖关系边，计算出每个点各自的初始入度。

收集初始起点：
找出所有 入度 == 0 的节点，把它们全扔进一个先进先出的队列（Queue）中。

循环消除依赖（BFS 过程）：

从队列头部弹出一个节点（记作当前完成的事项）。

将它加入拓扑结果集（或计数器加 1）。

遍历它指向的所有后续邻居节点，把这些邻居节点的入度分别减 1（表示这条边被移除了，前置要求被满足了一个）。

如果某个邻居节点的入度被减到了 0，说明它的前置条件已经彻底被清空，立刻把这个邻居也加入队列。

判环与结果验证：

当队列为空时，检查弹出的节点总数：

若总数 == 节点总数：排序成功，输出的节点顺序就是一个合法的拓扑序列。

若总数 < 节点总数：图中存在环（死锁）。因为环上的节点入度永远不可能减到 0，所以它们永远进不了队列

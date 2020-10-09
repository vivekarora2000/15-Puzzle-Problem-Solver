

The approach I use to solve the 15 puzzle problem is using A* search algorithm with h2
(Manhattan Distance) as my heuristic function. To solve the problem I created a node class
with attributes - state, parent , children, depth, path cost etc . Then I made a heuristic
function for Manhattan Distance. So the search expands the node n with the lowest f(n).
The only major issue is that the space complexity of the algorithm is exponential

We know that A* is optimal if h(n) used is consistent.To
show this I’ll first show that if h(n) is consistent then the values of f(n) along any path are
non decreasing. Suppose n’ is successor of n.
f(n’) = g(n’) + h(n’) = g(n) + c(n,a,n’) + h(n’) >= g(n) + h(n) = f(n)
Also whenever A* selects a node n for expansion , the optimal path to that solution has
been found , this is because had this not been the case there would have to be another
frontier node n’ on the optimal path from start node to n. So by graph separation property
because f is non decreasing along any path, n’ would have a lower f-cost than n and
would’ve been selected first.
Seeing these 2 properties we can say A* is optimal.

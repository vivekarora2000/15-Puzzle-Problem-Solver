import time
from heapq import *



class Node:
    def __init__(self, state, parent, operator, depth, path_cost):
        self.state = state
        self.parent = parent
        self.children = list()
        self.operator = operator
        self.depth= depth
        self.path_cost = path_cost


    def __lt__(self, other):
        return self.path_cost < other.path_cost


    def is_Equivalent(self, state):
        if self.state == state:
            return True
        else:
            return False


    def moves(self):
        new_state = self.state[:]
        blank_index = self.state.index(0)


        if blank_index not in [0, 1, 2, 3]: # UP
            temp = new_state[blank_index - 4]
            new_state[blank_index - 4] = new_state[blank_index]
            new_state[blank_index] = temp
            child = Node(new_state, self, "Up", self.depth + 1, self.path_cost)
            self.children.append(child)


        new_state = self.state[:]
        if blank_index not in [12, 13, 14, 15]:  # DOWN
            temp = new_state[blank_index + 4]
            new_state[blank_index + 4] = new_state[blank_index]
            new_state[blank_index] = temp
            child = Node(new_state, self, "Down", self.depth + 1, self.path_cost)
            self.children.append(child)

        new_state = self.state[:]
        if blank_index not in [0, 4, 8, 12]:  # LEFT
            temp = new_state[blank_index - 1]
            new_state[blank_index - 1] = new_state[blank_index]
            new_state[blank_index] = temp
            child = Node(new_state, self, "Left", self.depth + 1, self.path_cost)
            self.children.append(child)


        new_state = self.state[:]
        if blank_index not in [3, 7, 11, 15]:  # RIGHT
            temp = new_state[blank_index + 1]
            new_state[blank_index + 1] = new_state[blank_index]
            new_state[blank_index] = temp
            child = Node(new_state, self, "Right", self.depth + 1, self.path_cost)
            self.children.append(child)

            
def A_Star(initialConfig, finalConfig):
    pq =[]
    f={}
    explored={}
    closed=set()
    t=0
    heappush(pq,Node(initialConfig, None, "", 0, 0))
    while pq:
        node = heappop(pq)
        
        if(tuple(node.state) in closed):
            continue
            
        if(node.parent):
            explored[tuple(node.state)] = tuple(node.parent.state)
            closed.add(tuple(node.state))
        else:
            explored[tuple(node.state)] = None
            
        if node.is_Equivalent(finalConfig):
            return path_solution(node),t
        
        new_d = node.depth + 1
        node.moves()
 
        for child in node.children:
        
            if tuple(child.state) in closed:
                continue
            if tuple(child.state)in f:
                move, m = f[tuple(child.state)]
                if move <= new_d:
                    continue
            else:
                m = h2(child.state,finalConfig)
            f[tuple(child.state)] = (new_d, m) 
            t+=1
            cost = new_d + h2(child.state, finalConfig)
            child.path_cost = cost
            heappush(pq,child)
    return ([], t)


           

def path_solution(Node):
    node = Node
    directions = []
    directions.append(node.operator)
    depth = node.depth
    while node.parent is not None:
        node = node.parent
        directions.append(node.operator)
    directions.pop()
    directions.reverse()
    return directions


def h2(initialConfig, finalConfig):
    h2_val=0
    for i in range(16):
            if initialConfig[i]!=finalConfig[i] and initialConfig[i]!=0:
                val = initialConfig[i]
                i_pos = i//4
                j_pos = i%4
                a = val // 4
                b = val % 4
                h2_val += abs(a-i_pos) + abs(b-j_pos)
    return h2_val



def FindMinimumPath(initialState,goalState):
    d={'0':0,'1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,
       '7': 7,'8': 8,'9': 9,'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}
    
    initialConfig = [item for sublist in initialState for item in sublist]
    finalConfig = [item for sublist in goalState for item in sublist]
    
    for i in range(len(initialConfig)):
        initialConfig[i] = d[initialConfig[i]]
        
    for i in range(len(finalConfig)):
        finalConfig[i] = d[finalConfig[i]]
        
    minPath,nodesGenerated=A_Star(initialConfig, finalConfig)
    return minPath, nodesGenerated



#**************   DO NOT CHANGE ANY CODE BELOW THIS LINE *****************************


def ReadInitialState():
    with open("initial_state4.txt", "r") as file: #IMP: If you change the file name, then there will be an error when
                                                        #               evaluators test your program. You will lose 2 marks.
        initialState = [[x for x in line.split()] for i,line in enumerate(file) if i<4]
    return initialState

def ShowState(state,heading=''):
    print(heading)
    for row in state:
        print(*row, sep = " ")

def main():
    initialState = ReadInitialState() 
    ShowState(initialState,'Initial state:')
    goalState = [['0','1','2','3'],['4','5','6','7'],['8','9','A','B'],['C','D','E','F']]
    ShowState(goalState,'Goal state:')
    
    start = time.time()
    minimumPath, nodesGenerated = FindMinimumPath(initialState,goalState)
    timeTaken = time.time() - start
    
    if len(minimumPath)==0:
        minimumPath = ['Up','Right','Down','Down','Left']
        print('Example output:')
    else:
        print('Output:')

    print('   Minimum path cost : {0}'.format(len(minimumPath)))
    print('   Actions in minimum path : {0}'.format(minimumPath))
    print('   Nodes generated : {0}'.format(nodesGenerated))
    print('   Time taken : {0} s'.format(round(timeTaken,4)))

if __name__=='__main__':
    main()

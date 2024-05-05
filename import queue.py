import queue

# Node class to represent the state of the problem
class Node:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

# Helper function to check if a state is valid
def is_valid_state(node):
    if node.missionaries < 0 or node.missionaries > 3:
        return False
    if node.cannibals < 0 or node.cannibals > 3:
        return False
    if node.missionaries < node.cannibals and node.missionaries > 0:
        return False
    if 3 - node.missionaries < 3 - node.cannibals and 3 - node.missionaries > 0:
        return False
    return True

# Helper function to generate valid successors
def generate_successors(node):
    successors = []
    if node.boat == 'left':
        successors.append(Node(node.missionaries - 2, node.cannibals, 'right', node))
        successors.append(Node(node.missionaries - 1, node.cannibals - 1, 'right', node))
        successors.append(Node(node.missionaries, node.cannibals - 2, 'right', node))
        successors.append(Node(node.missionaries - 1, node.cannibals, 'right', node))
        successors.append(Node(node.missionaries, node.cannibals - 1, 'right', node))
    else:
        successors.append(Node(node.missionaries + 2, node.cannibals, 'left', node))
        successors.append(Node(node.missionaries + 1, node.cannibals + 1, 'left', node))
        successors.append(Node(node.missionaries, node.cannibals + 2, 'left', node))
        successors.append(Node(node.missionaries + 1, node.cannibals, 'left', node))
        successors.append(Node(node.missionaries, node.cannibals + 1, 'left', node))
    return [succ for succ in successors if is_valid_state(succ)]

# A* Search
def heuristic(node):
    return node.missionaries + node.cannibals

def a_star():
    start_node = Node(3, 3, 'left')
    frontier = queue.PriorityQueue()
    frontier.put((0, start_node))
    explored = set()
    while not frontier.empty():
        _, current_node = frontier.get()
        if current_node == goal_node:
            path = [current_node]
            while current_node:
                path.insert(0, current_node)
                current_node = current_node.parent
            return path
        explored.add(current_node)
        for successor in generate_successors(current_node):
            if successor not in explored:
                priority = heuristic(successor)
                frontier.put((priority, successor))
    return None

goal_node = Node(0, 0, 'right')

print("\nA* Search:")
a_star_path = a_star()
if a_star_path:
    for node in a_star_path:
        print(f"{node.missionaries},{node.cannibals},{node.boat}")
else:
    print("No solution found.")


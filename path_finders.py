from tree import Node


class KnightPathFinder:
    def __init__(self, tup=()):
        self._root = Node(tup)
        self._considered_positions = set()

    def get_valid_moves(self, pos):
        valid_moves = [(-1, 2), (1, 2), (-2, -1), (2, 1),
                       (-1, -2), (1, -2), (-2, 1), (2, -1)]

        valid_endpoints = [
            (pos[0] + move[0], pos[1] + move[1])
            for move in valid_moves
            if ((pos[0] + move[0] in range(8)) and (pos[1] + move[1] in range(8)))
        ]
        return valid_endpoints

    def new_move_positions(self, pos):
        new_moves = []
        for move in self.get_valid_moves(pos):
            if (move not in self._considered_positions):
                new_moves.append(move)

        self._considered_positions.update(new_moves)

        return set(new_moves)

    def build_move_tree(self):
        queue = []
        queue.append(self._root)
        while queue:
            current_node = queue.pop(0)
            adjPos = self.new_move_positions(current_node._value)

            nodeList = [Node(pos) for pos in adjPos]
            [current_node.add_child(node) for node in nodeList]

            queue.extend(nodeList)

    def find_path(self, end_position):
        pass

    def trace_to_root(self):
        pass


finder = KnightPathFinder((4, 4))
finder.build_move_tree()
print(finder._root.children)

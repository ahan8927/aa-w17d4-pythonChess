from tree import Node

class KnightPathFinder:
    def __init__(self, tup = ()):
        self._root = Node(tup)

        self._considered_positions = set()

    def get_valid_moves(self, pos):
        valid_moves = [(-1, 2), (1, 2), (-2, -1), (2, 1), (-1, -2), (1, -2), (-2, 1), (2, -1)]

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
        pass

    def find_path(self, end_position):
        pass

    def trace_to_root(self):
        pass




finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((4,4)))

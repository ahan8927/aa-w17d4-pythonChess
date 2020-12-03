class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node, call_parent = False):
        if (node not in self._children):
            self._children.append(node)
            if not call_parent:
                node.parent = self


    def remove_child(self, node):
        if node != None:
            self._children.remove(node)
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if not parent:
            self._parent = parent
            return
        if self._parent:
            self._parent.remove_child(self)
        self._parent = parent
        parent.add_child(self, True)









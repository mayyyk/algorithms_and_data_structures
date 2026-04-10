class RootNode:  # BST structure
    def __init__(self):
        self._root_node = None

    def search(self, key):
        curr_node = self._root_node
        while curr_node is not None and curr_node._key != key:
            if key < curr_node._key:
                curr_node = curr_node._child_left
            else:
                curr_node = curr_node._child_right
        if curr_node != None:
            return curr_node._value
        else:
            return None

    def insert(self, key, value):
        if self._root_node is None:
            self._root_node = TreeNode(key, value)
        curr_node = self._root_node
        prev_node = None

        while curr_node is not None:
            if key == curr_node._key:
                curr_node._value = value
                return

            if key < curr_node._key:
                if curr_node._child_left is None:
                    curr_node._child_left = TreeNode(key, value)
                    return
                else:
                    curr_node = curr_node._child_left

            if key > curr_node._key:
                if curr_node._child_right is None:
                    curr_node._child_right = TreeNode(key, value)
                    return
                else:
                    curr_node = curr_node._child_right

    def delete(self, key):
        self._root_node = self.__delete_recursive(self._root_node, key)

    def __delete_recursive(self, node, key):
        if node is None:
            return None

        if key < node._key:
            node._child_left = self.__delete_recursive(node._child_left, key)
        elif key > node._key:
            node._child_right = self.__delete_recursive(node._child_right, key)
        elif key == node._key:
            if node._child_left is None and node._child_right is None:
                return None
            elif node._child_left is not None and node._child_right is None:
                return node._child_left
            elif node._child_left is None and node._child_right is not None:
                return node._child_right
            elif node._child_left is not None and node._child_right is not None:
                new_node = node._child_right
                while new_node._child_left is not None:
                    new_node = new_node._child_left

                node._key = new_node._key
                node._value = new_node._value
                node._child_right = self.__delete_recursive(
                    node._child_right, new_node._key
                )
        return node

    def print_as_list(self):
        res_list = []
        curr_node = self._root_node
        if curr_node is None:
            print("")
            return

        self.__print_recursive(curr_node, res_list)

        print(res_list)

    def __print_recursive(self, node, res_list):
        if node is None:
            return
        self.__print_recursive(node._child_left, res_list)
        res_list_el = f"{node._key} {node._value},"
        res_list.append(res_list_el)
        self.__print_recursive(node._child_right, res_list)

    def print_tree(self):
        print("==============")
        self.__print_tree(self._root_node, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node._child_right, lvl + 5)

            print()
            print(lvl * " ", node._key, node._value)

            self.__print_tree(node._child_left, lvl + 5)

    def height(self):
        if self._root_node is not None:


class TreeNode:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._child_left = None
        self._child_right = None


def main():
    bst = RootNode()
    bst.insert(50, "A")
    bst.insert(15, "B")
    bst.insert(62, "C")

    bst.print_tree()

    bst.print_as_list()

    print(bst.search(24))

    bst.insert(20, "AA")


main()

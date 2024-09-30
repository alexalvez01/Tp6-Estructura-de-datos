from cola import Queue

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value

    def __init__(self):
        self.root = None

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            counter_superhero = 0
            counter_villain = 0
            if root is not None:
            
                if root.other_value.get('superhero') is True:
                    counter_superhero = 1
                elif root.other_value.get('superhero') is False:
                    counter_villain = 1
            
                left_superheroes, left_villains = __contar_super_heroes(root.left)
                right_superheroes, right_villains = __contar_super_heroes(root.right)
            
                counter_superhero += left_superheroes + right_superheroes
                counter_villain += left_villains + right_villains
            return counter_superhero, counter_villain

        return __contar_super_heroes(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('superhero') is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('superhero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    def inorden_superheroes_descendente(self, root):
        if root is not None:
            self.inorden_superheroes_descendente(root.right)
            if root.other_value.get('superhero') is True:
                print(root.value)
            self.inorden_superheroes_descendente(root.left)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    root.right, value_delete = __delete(root.right, value)
                else:
                    value_delete = root.value
                    if root.left is None:
                        return root.right, value_delete
                    elif root.right is None:
                        return root.left, value_delete
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, value_delete
                
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value

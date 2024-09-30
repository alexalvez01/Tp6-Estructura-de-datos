from cola import Queue

class BinaryTree:

    class __Node:
        def __init__(self, value, defeated_by=None, description=None, captured_by=None):
            self.value = value
            self.defeated_by = defeated_by
            self.description = description
            self.captured_by = captured_by
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_node(self, value, defeated_by=None, description=None):
        def __insert(root, value, defeated_by=None, description=None):
            if root is None:
                return BinaryTree.__Node(value, defeated_by=defeated_by, description=description)
            elif value < root.value:
                root.left = __insert(root.left, value, defeated_by, description)
            else:
                root.right = __insert(root.right, value, defeated_by, description)
            return root

        self.root = __insert(self.root, value, defeated_by, description)


    def show_info(self, key):
        node = self.search(key)
        if node:
            print(f"-Nombre: {node.value}")
            print(f"-Derrotado por: {node.defeated_by}")
            print(f"-Descripción: {node.description}")
            print(f"-Capturado por: {node.captured_by}")
        else:
            print(f"{key} no encontrado.")

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
            return None

        return __search(self.root, key)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"{root.value}, derrotado por: {root.defeated_by}")
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def add_description(self, key, description):
        node = self.search(key)
        if node:
            node.description = description
        else:
            print(f"{key} no encontrado.")


    def top_defeaters(self, top_n):
        def __count_defeaters(root, defeaters_count):
            if root:
                if root.defeated_by:
                    defeaters_count[root.defeated_by] = defeaters_count.get(root.defeated_by, 0) + 1
                __count_defeaters(root.left, defeaters_count)
                __count_defeaters(root.right, defeaters_count)

        defeaters_count = {}
        __count_defeaters(self.root, defeaters_count)
        sorted_defeaters = sorted(defeaters_count.items(), key=lambda x: x[1], reverse=True)
        for i in range(min(top_n, len(sorted_defeaters))):
            print(f"---{sorted_defeaters[i][0]} derrotó a {sorted_defeaters[i][1]} criaturas.")


    def creatures_defeated_by(self, defeater):
        def __creatures_defeated_by(root):
            if root:
                if root.defeated_by == defeater:
                    print(root.value)
                __creatures_defeated_by(root.left)
                __creatures_defeated_by(root.right)

        __creatures_defeated_by(self.root)

    def undefeated_creatures(self):
        def __undefeated_creatures(root):
            if root:
                if not root.defeated_by:
                    print(root.value)
                __undefeated_creatures(root.left)
                __undefeated_creatures(root.right)

        __undefeated_creatures(self.root)

    def capture_creature(self, key, captor):
        node = self.search(key)
        if node:
            node.captured_by = captor
        else:
            print(f"{key} no encontrado.")

    def creatures_captured_by(self, captor):
        def __creatures_captured_by(root):
            if root:
                if root.captured_by == captor:
                    print(root.value)
                __creatures_captured_by(root.left)
                __creatures_captured_by(root.right)

        __creatures_captured_by(self.root)

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

        self.root, delete_value = __delete(self.root, value)
        return delete_value

 
    def by_level(self):
        queue = Queue()
        if self.root:
            queue.arrive(self.root)

        while queue.size() > 0:
            node = queue.attention()
            print(f"Nombre: {node.value}, Capturado por: {node.captured_by}, Derrotado por: {node.defeated_by}")
            if node.left:
                queue.arrive(node.left)
            if node.right:
                queue.arrive(node.right)
        return queue
                
creatures_tree = BinaryTree()
creatures_tree.insert_node("Ceto")
creatures_tree.insert_node("Tifón", defeated_by="Zeus")
creatures_tree.insert_node("Equidna", defeated_by="Argos Panoptes")
creatures_tree.insert_node("Dino")
creatures_tree.insert_node("Pefredo")
creatures_tree.insert_node("Enio")
creatures_tree.insert_node("Escila")
creatures_tree.insert_node("Caribdis")
creatures_tree.insert_node("Euríale")
creatures_tree.insert_node("Esteno")
creatures_tree.insert_node("Medusa", defeated_by="Perseo")
creatures_tree.insert_node("Ladón", defeated_by="Heracles")
creatures_tree.insert_node("Águila del Cáucaso")
creatures_tree.insert_node("Quimera", defeated_by="Belerofonte")
creatures_tree.insert_node("Hidra de Lerna", defeated_by="Heracles")
creatures_tree.insert_node("León de Nemea", defeated_by="Heracles")
creatures_tree.insert_node("Esfinge", defeated_by="Edipo")
creatures_tree.insert_node("Dragón de la Cólquida")
creatures_tree.insert_node("Cerbero")

creatures_tree.insert_node("Cerda de Cromión", defeated_by="Teseo")
creatures_tree.insert_node("Ortro", defeated_by="Heracles")
creatures_tree.insert_node("Toro de Creta", defeated_by="Teseo")
creatures_tree.insert_node("Jabalí de Calidón", defeated_by="Atalanta")
creatures_tree.insert_node("Carcinos")
creatures_tree.insert_node("Gerión", defeated_by="Heracles")
creatures_tree.insert_node("Cloto")
creatures_tree.insert_node("Láquesis")
creatures_tree.insert_node("Átropos")
creatures_tree.insert_node("Minotauro de Creta", defeated_by="Teseo")
creatures_tree.insert_node("Harpías")
creatures_tree.insert_node("Argos Panoptes", defeated_by="Hermes")
creatures_tree.insert_node("Aves del Estínfalo")
creatures_tree.insert_node("Talos", defeated_by="Medea")
creatures_tree.insert_node("Sirenas")
creatures_tree.insert_node("Pitón", defeated_by="Apolo")
creatures_tree.insert_node("Cierva de Cerinea")
creatures_tree.insert_node("Basilisco")
creatures_tree.insert_node("Jabalí de Erimanto")

print("---Listado de criaturas en orden")
creatures_tree.inorden()
print("---Añadiendo descripción a Tifón")
creatures_tree.add_description("Tifón", "Gigante que desafiaba a los dioses.")
creatures_tree.inorden()
print("---Información de Talos:")
creatures_tree.show_info("Talos")  
print("---Los 3 heroes o dioses que derrotaron a mas criaturas")
creatures_tree.top_defeaters(3)
print("---Criaturas derrotadas por Heracles")
creatures_tree.creatures_defeated_by("Heracles") 
print("---Criaturas que no han sido derrotadas")
creatures_tree.undefeated_creatures()  
creatures_tree.capture_creature("Cerbero", "Heracles")
creatures_tree.capture_creature("Toro de Creta", "Heracles")
creatures_tree.capture_creature("Cierva de Cerinea", "Heracles")
creatures_tree.capture_creature("Jabalí de Erimanto", "Heracles")
print("---Busqueda por coincidencia")
creatures_tree.search("Talos")
creatures_tree.delete_node("Basilisco") 
creatures_tree.delete_node("Sirenas")  
creatures_tree.capture_creature("Aves del Estínfalo", "Heracles") 
creatures_tree.add_description("Aves del Estínfalo", "Derrotadas por Heracles en gran cantidad.")
ladon = creatures_tree.search("Ladón")  
if ladon:
    creatures_tree.delete_node("Ladón")
    creatures_tree.insert_node("Dragón Ladón", defeated_by="Heracles", description=ladon.description)
print("---Listado de criaturas por nivel")
creatures_tree.by_level()  
print("---Criaturas capturadas por Heracles")
creatures_tree.creatures_captured_by("Heracles")  
from arbolsuperheroes import BinaryTree
mcu_characters = [
    {"nombre": "Tony Stark", "superhero": True},  
    {"nombre": "Steve Rogers", "superhero": True},  
    {"nombre": "Natasha Romanoff", "superhero": True},  
    {"nombre": "Thor", "superhero": True},
    {"nombre": "Bruce Banner", "superhero": True},  
    {"nombre": "Clint Barton", "superhero": True},  
    {"nombre": "Peter Parker", "superhero": True},  
    {"nombre": "T'Challa", "superhero": True},  
    {"nombre": "Wanda Maximoff", "superhero": True},  
    {"nombre": "Vision", "superhero": True},
    {"nombre": "Stephen Strange", "superhero": True},  
    {"nombre": "Scott Lang", "superhero": True},  
    {"nombre": "Sam Wilson", "superhero": True},  
    {"nombre": "Bucky Barnes", "superhero": True},  
    {"nombre": "Carol Danvers", "superhero": True},  
    {"nombre": "Loki", "superhero": False},  
    {"nombre": "Thanos", "superhero": False},  
    {"nombre": "Ultron", "superhero": False},  
    {"nombre": "Erik Killmonger", "superhero": False},  
    {"nombre": "Red Skull", "superhero": False},  
    {"nombre": "Hela", "superhero": False},  
    {"nombre": "Obadiah Stane", "superhero": False},  
    {"nombre": "Vulture", "superhero": False},  
    {"nombre": "Mysterio", "superhero": False}, 
    {"nombre": "Nebula", "superhero": False},  
    {"nombre": "Yon-Rogg", "superhero": False}, 
    {"nombre": "Ronan el Acusador", "superhero": False},  
    {"nombre": "Dormammu", "superhero": False},  
    {"nombre": "Zemo", "superhero": False}, 
]

char_tree = BinaryTree()

for personaje in mcu_characters:
    char_tree.insert_node(personaje['nombre'], personaje)

print("---Villanos ordenados alfabéticamente:")
char_tree.inorden_villanos()


print("---Superhéroes que empiezan con C:")
char_tree.inorden_superheros_start_with("C")

print("---Cantidad de superhéroes en el árbol:", char_tree.contar_super_heroes()[0])

print("---Modificando el nombre de Doctor Strange:")
doctor_strange = char_tree.search("Stephen Strange")
if doctor_strange:
    doctor_strange.value = "Doctor Strange"
char_tree.inorden() 


print("---Superhéroes ordenados de manera descendente:")
char_tree.inorden_superheroes_descendente(char_tree.root)

heroes_tree = BinaryTree()
villains_tree = BinaryTree()

def separar_heroes_y_villanos(root):
    if root is not None:
        if root.other_value.get('superhero') is True:
            heroes_tree.insert_node(root.value, root.other_value)
        else:
            villains_tree.insert_node(root.value, root.other_value)
        separar_heroes_y_villanos(root.left)
        separar_heroes_y_villanos(root.right)

separar_heroes_y_villanos(char_tree.root)


print("---Superhéroes en el árbol:", heroes_tree.contar_super_heroes()[0])
print("---Villanos en el árbol:", villains_tree.contar_super_heroes()[1])


print("---Superhéroes en orden alfabético:")
heroes_tree.inorden()

print("---Villanos en orden alfabético:")
villains_tree.inorden()
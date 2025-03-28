from TreeVisualiser import TreeVisualizer
tv = TreeVisualizer("small_graph.txt")
tv.load()

start = 'X'
tree=tv.edges_to_structure()

"""
napisz kod ktory znajdzie sciezke od roota 0 do wezla o wartosci X
wynik podaj w postaci listy wezlow ktore trzeba odwiedzic aby dojsc do X
uzyskana tablice wpisz do funkcji tv.highlight_path(lista) aby podswietlic na wykresie twoje rozwiazanie
"""

def search(node, elem, visited):
    current_val = node.val
    visited.append(current_val)
    for child in node.children:
        result = search(child, elem, list(visited))
        if result:
            return result
    if elem == current_val:
        return visited


visited = search(tree, start, [])

tv.highlight_path(visited)
tv.update()

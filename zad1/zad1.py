from TreeVisualiser import TreeVisualizer
tv = TreeVisualizer("small_graph.txt")
tv.load(show=True) # loads graph and shows it

start = 'X'
tree = tv.edges_to_structure() #creates tree structure from edges file

"""
napisz kod ktory znajdzie sciezke od roota (wezel o wartosci 0) do wezla o wartosci X
wynik podaj w postaci listy wezlow ktore trzeba odwiedzic aby dojsc do X
uzyskana tablice wpisz do funkcji tv.highlight_path(lista) aby podswietlic na wykresie twoje rozwiazanie

dla small_graph.txt wynik to ['0', '1', '2', '3', 'C', 'X']
jesli chcecie zmienic plik to w treeVisualizer wpiszcie big_graph.txt
mozecie uzyc tv.run_build() aby budowac wlasny graf
"""




visited = search(tree, start, [])
print(visited)
tv.highlight_path(visited)
tv.show()

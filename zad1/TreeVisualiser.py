import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import threading
import queue
from matplotlib.animation import FuncAnimation
from Tree import build_tree

matplotlib.use('TkAgg')


class TreeVisualizer:
    def __init__(self, filename="small_graph.txt"):
        self.root = 0
        self.G = nx.Graph()
        self.input_queue = queue.Queue()
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ani = FuncAnimation(self.fig, self.update, interval=100, cache_frame_data=False)
        self.running = True
        self.filename = filename
        self.colors = []
        self.tree = None

    def load(self, show=False):
        G_to_load = nx.read_edgelist(self.filename)
        self.G = G_to_load
        if show:
            self.show()

    def show(self):
        plt.close(self.fig)
        if len(self.colors) != len(self.file_to_list()):
            self.colors = ['black' for i in range(len(self.G))]
        fig, ax = plt.subplots()
        if self.G.nodes():
            pos = nx.spring_layout(self.G, seed=42)
            nx.draw(self.G, pos, ax=ax, with_labels=True,
                    node_size=500, node_color='skyblue',
                    font_size=10, font_weight='bold', edge_color=self.colors)
            plt.show()

    def update(self, frame=None):
        if len(self.colors) != len(self.file_to_list()):
            self.colors = ['black' for i in range(len(self.G))]
        self.ax.clear()
        if self.G.nodes():
            pos = nx.spring_layout(self.G, seed=42)
            nx.draw(self.G, pos, ax=self.ax, with_labels=True,
                    node_size=500, node_color='skyblue',
                    font_size=10, font_weight='bold', edge_color=self.colors)
            plt.show()

    def input_thread(self):
        if self.root is None:
            self.root = input("Podaj nazwę korzenia drzewa: ")
            self.G.add_node(self.root)
        print("Rozpocznij dodawanie węzłów i krawędzi. Wpisz 'done' aby zakończyć.")
        print("[n1] [n2] -> tworzy krawedz od [n1] i nazwie [n2]")
        print("done -> zakoncz")
        print("import -> zapisz i zakoncz")
        while self.running:
            command = input().strip()
            if command == "done":
                self.running = False
                break
            if command == "import":
                self.running = False
                self.write()
                break
            parent, child = command.split(" ")
            if parent not in self.G:
                print(f"Węzeł {parent} nie istnieje. Najpierw musisz go dodać.")
                continue
            if child and child not in self.G:
                self.G.add_node(child)
            if [parent, child] not in self.G.edges:
                self.G.add_edge(parent, child)
                print(f"Połączono {parent} z {child}.")
            else:
                print("ta krawedz istnieje")
            self.update()

    def write(self):
        nx.write_edgelist(self.G, self.filename)
        print("graf zostal zapisany, jak zamkniesz wykres program sie zamknie")

    def run_build(self):
        visualizer = self

        input_thread = threading.Thread(target=visualizer.input_thread)
        input_thread.start()
        plt.show()
        input_thread.join()

    def file_to_list(self):
        return [list(edge[:2]) for edge in self.G.edges(data=True)]

    def edges_to_structure(self):
        edges = self.file_to_list()
        self.tree = build_tree(edges, f"{self.root}")
        return self.tree

    def highlight_path(self, path):
        steps = path
        highlight_edges = []
        edges = self.file_to_list()
        self.colors = ['black' for i in range(len(edges))]
        for idx in range(len(steps) - 1):
            highlight_edges.append([steps[idx], steps[idx + 1]])
        for highlight_edge in highlight_edges:
            for edge in edges:
                if edge[0] == highlight_edge[0] and edge[1] == highlight_edge[1]:
                    self.colors[edges.index(edge)] = 'r'
                elif edge[0] == highlight_edge[1] and edge[1] == highlight_edge[0]:
                    self.colors[edges.index(edge)] = 'r'

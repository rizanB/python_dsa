# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-final-newline


from typing import Dict, List


class Graph:
    def __init__(self) -> None:
        self.graph_dict: Dict[str, List[str]] = {}

    def __repr__(self) -> str:
        result: str = ""

        for vertex in self.graph_dict:
            result += f" { vertex } : { self.graph_dict[vertex]} \n"

        return result

    def add_vertex(self, vertex: str):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, v1: str, v2: str):
        if v1 in self.graph_dict and v2 in self.graph_dict:
            self.graph_dict[v1].append(v2)
            self.graph_dict[v2].append(v1)


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("D")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "D")


print(my_graph)

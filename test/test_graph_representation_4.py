import pytest
from student_code import ShortestPathDAG

class TestShortestPathDAG:
    @pytest.fixture
    def setup_dag(self):
        dag = ShortestPathDAG()
        # Add nodes and edges
        dag.add_node('A')
        dag.add_node('B')
        dag.add_node('C')
        dag.add_node('D')
        dag.add_node('E')
        dag.add_edge('A', 'B', edge_weight=1)
        dag.add_edge('B', 'C', edge_weight=2)
        dag.add_edge('A', 'C', edge_weight=4)
        dag.add_edge('C', 'D', edge_weight=3)
        dag.add_edge('A', 'E', edge_weight=10)
        return dag

    def test_shortest_path_existence(self, setup_dag):
        dag = setup_dag
        _, distance = dag.shortest_path('A', 'D')
        assert distance == 6, "Shortest path from A to D should be 6"

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


    def test_direct_path(self, setup_dag):
        dag = setup_dag
        _, distance = dag.shortest_path('C', 'D')
        assert distance == 3, "Shortest path from C to D should be 3"

 
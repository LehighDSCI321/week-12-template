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

    def test_topological_sort(self, setup_dag):
        dag = setup_dag
        top_sort = dag.top_sort()
        valid_sorts = [
            ['A', 'B', 'C', 'D', 'E'],
            ['A', 'B', 'C', 'E', 'D'],
            ['A', 'E', 'B', 'C', 'D'],
            ['A', 'E', 'B', 'D', 'C'],
        ]
        assert top_sort in valid_sorts, "Topological sort should be one of the valid topological orders"

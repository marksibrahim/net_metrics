import net_metrics

#same as sample network described in Wikipedia paper
sample_net_dict = {'A': 'B', 'B':'C', 'C':'A', 'D':'C', 'E':'C',
              'G':'E', 'F':'E'}

#create instance of network object from net_metrics
sample_net = net_metrics.Network(sample_net_dict)

def test_traversal_visits():
    """
    tests result of traversal visits computation
    """
    traversal_visits = sample_net.traversal_visits
    assert traversal_visits['A'] == 7 
    assert traversal_visits['E'] == 2 
    assert traversal_visits['G'] == 0

def test_cycles():
    """
    tests correct identification of cycles
    """
    cycles = sample_net.cycles
    assert set(['A', 'B', 'C']) in cycles
    assert set(['A', 'B']) not in cycles
    assert set(['A', 'B', 'C', 'D']) not in cycles
    
def test_traversal_funnels():
    """
    tests result of traversal funnels computation
    """
    traversal_funnels = sample_net.traversal_funnels
    assert traversal_funnels['A'] == 0
    assert traversal_funnels['B'] == 0
    assert traversal_funnels['C'] == 4
    assert traversal_funnels['E'] == 2
    assert traversal_funnels['G'] == 0

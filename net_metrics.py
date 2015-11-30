from collections import defaultdict

class Network():
    """
    a directed network object with methods
    to characterize the structure

    input is a dictionary of nodes and single outward link
    node --> link
    """

    def __init__(self, net_dict):
        self.net = net_dict
        self.traversal_visits = self.compute_traversal_visits(self.net)
        self.cycles = self.identify_cycles(self.net)
        self.traversal_funnels = self.compute_traversal_funnels(self.net)

    def compute_traversal_visits(self, net):
        """
        returns a dictionary: nodes --> number of visits
        """
        #initializes dictionary with 0 as default value 
        traversal_visits = defaultdict(int)

        for node in net:
            link = net.get(node, False)
            traversed = []
            while link not in traversed and link:
                traversal_visits[link] += 1
                traversed.append(link)
                link = net.get(link, False)
        return traversal_visits

    def identify_cycles(self, net):
        """
        returns a list of cycles 
        cycles are stored as sets: {'A', 'B', 'C'} 
        """
        cycles = []

        for node in net:
            link = net.get(node, False)
            traversed = []
            while link not in traversed and link:
                traversed.append(link)
                link = net.get(link, False)
            #capture cycle
            if link in traversed: 
                cycle = traversed[traversed.index(link):]
                #add cycle if not already found
                if set(cycle) not in cycles:
                    cycles.append(set(cycle))
        return cycles
            

    def compute_traversal_funnels(self, net):
        """
        returns a dictionary: nodes --> number of visits
        input net is a dictionary of nodes and single outward link
        """
        #initializes dictionary with 0 as default value 
        traversal_funnels = defaultdict(int)
        nodes_in_cycles = set([node for cycle in self.cycles for node in cycle])

        for node in net:
            link = net.get(node, False)
            #confirm starting node isn't in a cycle
            if node in nodes_in_cycles: link = False
            traversed = []

            while link not in traversed and link:
                traversal_funnels[link] += 1
                traversed.append(link)
                #inside cycle?
                if link in nodes_in_cycles:
                    break
                link = net.get(link, False)
        return traversal_funnels

        


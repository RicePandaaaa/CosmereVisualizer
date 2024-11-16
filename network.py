from typing import List
from pyvis.network import Network

def create_network(main_term: str, sub_terms: List[str], file_name: str):
    """ 
    Creates a network graph centered on the main term as a HTML file
    
    Args:
        main_term (str): Name of the main term
        sub_terms (List[str]): List of names of the associated terms
        file_name (str): Name of file to store network in

    Returns:
        None
    """

    # Set up base net
    net = Network()
    net.add_node(n_id=main_term, label=main_term, color="#ff5733")

    # Join the terms together
    for sub_term in sub_terms:
        net.add_node(n_id=sub_term, label=sub_term, color="#33cfff")
        net.add_edge(main_term, sub_term)

    # Create the HTML file
    net.write_html(file_name)


from typing import List
from pyvis.network import Network
import os

def create_network(terms: dict[str, List[str]], file_name: str):
    """ 
    Creates a network graph centered on the main term as a HTML file
    
    Args:
        terms (dict[str, List[str]]): Dictionary of main terms and their connected terms
        file_name (str): Name of file to store network in

    Returns:
        None
    """

    # Set up base net
    net = Network()

    for main_term in terms:
        # Create new center node
        net.add_node(n_id=main_term, label=main_term, color="#ff5733")
        sub_terms = terms[main_term]

        # Join the terms together
        for sub_term in sub_terms:
            net.add_node(n_id=sub_term, label=sub_term, color="#33cfff")
            net.add_edge(main_term, sub_term)

    # Create the HTML file
    net.write_html(f"networks/{file_name}.html")


# For generating the graphs
if __name__ == "__main__":
    # Open the relationships folder
    for file_name in os.listdir("relationships/"):
        file_path = os.path.join("relationships/", file_name)

        with open(file_path, "r") as dataFile:
            # Skip the header line
            dataFile.readline()

            # Extract the main term and the sub terms
            terms = {}

            for line in dataFile:
                main_term, sub_term = line.split(",")
                
                if main_term not in terms:
                    terms[main_term] = []
                
                terms[main_term].append(sub_term)

            # Generate the HTML file with the network
            file_start = file_name.split(".")[0]
            create_network(terms, file_start)
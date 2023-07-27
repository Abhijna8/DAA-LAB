import networkx as nx
def get_distances(num_nodes):
  distances={}
  for i in range(1,num_nodes+1):
    for j in range(i+1,num_nodes+1):
      distance=float(input(f"enter the distance between nodes{i} and node{j}:"))
      distances[(i,j)]=distance
      distances[(j,i)]=distance
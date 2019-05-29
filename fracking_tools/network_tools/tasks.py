# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from networktools.events.builder import EventBuilder
from networktools.matrices.matrices import AdjacencyMatrix, NetworkComparison
from networktools.files.readers import FileReader


from documenttools.comparisons.compare import DocumentComparison

from r_network_serializer.rnetwork import RNetwork
from r_network_serializer.serialize import to_listvector, rserialize



import csv


@shared_task
def build_events_from_files(files):
    files = [(f.name, FileReader(f).read()) for f in files]

    builder = EventBuilder(files)
    return builder.build() 


@shared_task
def build_event_networks(files, header_state, weighted_state):
    files = [(f.name, csv.reader(f)) for f in files]
    matrices = []

    for f in files: 
        mat_obj = AdjacencyMatrix(f, header=header_state, weighted=weighted_state) 
        matrices.append(mat_obj.build())

    return matrices


@shared_task
def build_pairs_networks(files, header_state): 
    files = [(f.name, csv.reader(f)) for f in files]
    matrices = []

    for f in files: 
        mat_obj = AdjacencyMatrix(f, header=header_state, from_events=False) 
        matrices.append(mat_obj.build())

    return matrices 


@shared_task
def compare_networks(files, labelA, labelB): 
    filesA = [(f.name, csv.reader(f)) for f in files[0]]
    filesB = [(f.name, csv.reader(f)) for f in files[1]]
    
    comparisons = []

    for fileA in filesA: 
        for fileB in filesB:
            comp_obj = NetworkComparison(fileA, fileB, labelA, labelB) 
            comparisons.append(comp_obj.compare())

    return comparisons



@shared_task
def convert_matrices_to_rnetworks(files): 
    networks = [RNetwork(f).serialize_ready for f in files]
    networks_lv = to_listvector(networks)
    serialized = rserialize(networks_lv)
    return serialized
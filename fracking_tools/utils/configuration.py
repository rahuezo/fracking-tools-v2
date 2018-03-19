BUILD_NETWORKS_FROM_EVENTS_CARD = {
    'title': 'Build Networks from Events',
    'body': """<p class="card-text">
        An event network refers to a network where
        nodes are linked by attending the same events.</p>
        
        <p class="card-text">This tool requires a <strong>.csv</strong>
        spreadsheet where each column is an event and each row is a node
        that attended that event.
        </p>                
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

BUILD_NETWORKS_FROM_PAIRS_CARD = {
    'title': 'Build Networks from Node Pairs',
    'body': """<p class="card-text">
        A network from node pairs refers to a network where
        node relationships are explicitly defined.</p>
        
        <p class="card-text">This tool requires a <strong>.csv</strong>
        spreadsheet with exactly two columns and where each row is a pair of nodes.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

COMPARE_NETWORKS_CARD = {
    'title': 'Compare Networks',
    'body': """<p class="card-text">
        A network comparison requires pairs of network files (adjacency matrices)
        and yields the node/edge overlap, and unique nodes/edges between network pairs.</p>

        <p class="card-text">This tool requires <strong>.csv</strong> network files
        with the same name that are located in different directories.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

BUILD_EVENTS_FROM_FILES_CARD = {
    'title': 'Build Events from Files',
    'body': """<p class="card-text">
        An event file can be created by extracting
        names from a file. It is assumed that names within a file are related.</p>

        <p class="card-text">This tool accepts <strong>.txt</strong> and <strong>.docx</strong>
        and uses NER to extract names from the files.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

READ_DOCS_CARD = {
    'title': 'Before Starting',
    'body': """<p class="card-text">
        An event file can be created by extracting
        names from a file. It is assumed that names within a file are related.</p>

        <p class="card-text">This tool accepts <strong>.txt</strong> and <strong>.docx</strong>
        and uses NER to extract names from the files.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}
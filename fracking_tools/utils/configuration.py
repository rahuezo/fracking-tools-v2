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

CONVERT_MATRICES_TO_R_NETWORKS = {
    'title': 'Convert Adjacency Matrices to R-Networks',
    'body': """<p class="card-text">
        One or many network files (adjacency matrices) are converted to R-Networks and then serialized 
        into a <strong>.rda</strong> file. The serialized networks can then be loaded in R using
        <code>readRDS(...)</code>.
        <p class="card-text">This tool requires <strong>.csv</strong> network files.</p>        
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

COMPARE_DOCS_CARD = {
    'title': 'Compare Documents',
    'body': """<p class="card-text">
        This tool lets you compare pairs of documents for content and textual similarity.
        </p>

        <p class="card-text">This tool accepts <strong>.txt</strong> and <strong>.docx</strong>
        files and uses <strong>cosine similarity</strong> for comparing content similarity and 
        <strong>Jaccard similarity</strong> for comparing textual similarity.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

TAG_DOCS_KEYWORDS_CARD = {
    'title': 'Tag Documents for Keywords',
    'body': """<p class="card-text">
        This tool lets you tag one or multiple documents for a list of user-provided keywords.
        </p>

        <p class="card-text">This tool accepts <strong>.txt</strong> and <strong>.docx</strong>
        files and returns a list of <strong>.txt</strong> files with tagged content.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

TAG_DOCS_NER_CARD = {
    'title': 'Tag Documents Using NER',
    'body': """<p class="card-text">
        This tool lets you tag one or multiple documents for named entities using Stanford's Named
        Entity Recognizer (NER).
        </p>

        <p class="card-text">This tool accepts <strong>.txt</strong> and <strong>.docx</strong>
        files and returns a list of <strong>.txt</strong> files with tagged content.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}

DOC_STATS_CARD = {
    'title': 'Compute Document Statistics',
    'body': """<p class="card-text">
        This tool lets you analyze one or multiple documents to determine reading level,
        word count, keyword frequency, and sentiment. 
        </p>

        <p class="card-text">This tool accepts <strong>.txt</strong> and <strong>.docx</strong>
        files and returns a <strong>.csv</strong> file where each row is an analyzed document.
        </p>        
        """,
    'info': """<p class="card-text text-muted text-center">
        <a class="btn btn-link">Read More</a>
        </p>
    """
}
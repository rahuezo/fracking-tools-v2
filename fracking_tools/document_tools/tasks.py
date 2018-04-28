# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from networktools.files.readers import FileReader


from documenttools.comparisons.compare import DocumentComparison
from documenttools.taggers.keywords import KeywordTagger
from documenttools.taggers.ner import NerTagger
from documenttools.statistics.statistics import DocumentStatistics


@shared_task
def compare_documents(files): 
    files = [(f.name, FileReader(f).read()) for f in files]
    
    comp_obj = DocumentComparison(files)

    return comp_obj.compare()


@shared_task
def tag_documents_keywords(files, keywords): 
    files = [(f.name, FileReader(f).read(raw=True).encode('ascii', errors='ignore')) for f in files]
    
    tagged_documents = []

    for f in files: 
        tag_obj = KeywordTagger(f, keywords)

        result = tag_obj.tag()

        if result: 
            tagged_documents.append(result)

    return tagged_documents


@shared_task
def tag_documents_ner(files): 
    files = [(f.name, FileReader(f).read(raw=True).encode('ascii', errors='ignore')) for f in files]
    
    tagged_documents = []

    for f in files: 
        tag_obj = NerTagger(f)

        result = tag_obj.tag()

        if result: 
            tagged_documents.append(result)

    return tagged_documents


@shared_task
def compute_document_statistics(files, keywords): 
    files = [(f.name, FileReader(f).read(raw=True).encode('ascii', errors='ignore')) for f in files]
    
    header = ['File Name', 'Reading Level', 'Word Count'] + [kw.title().strip() for kw in keywords]
    header = header + ['Polarity', 'Subjectivity', 'Classification', 'P_POS', 'P_NEG']

    rows = [header]

    for f in files: 
        stats_obj = DocumentStatistics(f, keywords)
        rows.append(stats_obj.compute())

    return rows
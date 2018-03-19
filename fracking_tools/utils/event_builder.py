from bs4 import BeautifulSoup as BS
from linux_pyner import tag_document
from files import get_text, ExtensionHandler

import pandas as pd
import os, sys
import tkFileDialog as fd



class EventBuilder: 
    @staticmethod
    def get_single_names(l, schar=','): 
        names = []
        for element in l: 
            name_list = element.split(schar)
            for name in name_list: 
                if len(name.strip()) > 0: 
                    names.append(name.strip())
        return names

    def __init__(self, files): 
        self.files = files

    def get_event_header(self, f): 
        return get_text(str(f)).split('.')[0].upper() #os.path.split(f)[1].split('.')[0].upper()

    def get_event(self, f): 
        tagged_content = tag_document(ExtensionHandler(f).get_content())
        soup = BS(tagged_content, 'lxml')
        people = list(set(map(lambda person: get_text(person.text).title(), soup.select('person'))))
        people = EventBuilder.get_single_names(people)
        return {self.get_event_header(f): people}

    def create_events(self): 
        columns = {}
        for f in self.files:             
            columns.update(self.get_event(f))

        # if len(columns) > 0: 
        df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in columns.iteritems()]))
        df = df.dropna(axis=1, how='all')
        values = df.values.tolist()

        if values: 
            return [list(df.columns.values)] + values
        return None


# fs = fd.askopenfilenames(title="Choose files to tag")

# eb = EventBuilder(fs)

# df = eb.create_events()

# df.to_csv('output.csv', mode='wb', index=False)

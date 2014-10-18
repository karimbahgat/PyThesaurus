# Pure Python, Simple Thesaurus Module
# Karim Bahgat, 2014

# to make it myself all i need is:
# concept class that can be set with a prefered term, list of synonym terms, similar concepts, broader concepts, narrower concepts, and contexts
# thesaurus class that holds a list of all concepts, and of contexts

# then thesaurus can:
# --> search for a term (exact or fuzzy) in a given context and return the concept (or list of matching concepts)
# -->    which can be used to standardize any term to the prefered term for its concept
# -->    check if that term can be considered as a subconcept or a parent concept of another concept
# -->    check if that term is similar/related to another concept
# -->    recursively narrow a search to only its subconcepts
# -->    recursively broaden a search to only its parentconcepts

class Concept:
    def __init__(self, preferred, synonyms=[], similar=[], narrower=[], broader=[], contexts=[]):
        self.preferred = preferred
        self.synonyms = synonyms
        # maybe make all below have to be concepts and not just words...? OR take them as words, but append to dictionary
        self.similar = similar
        self.narrower = narrower
        self.broader = broader
        self.contexts = contexts

    def __str__(self):
        string = "Concept: %s"%self.preferred
        return string

    def compare(self, similar, narrower, broader, contexts):
        for sim in similar:
            if not sim in self.similar:
                return None
        for nar in narrower:
            if not nar in self.narrower:
                return None
        for broad in broader:
            if not broad in self.broader:
                return None
        for contx in contexts:
            if not contx in self.contexts:
                return None
        # all comparisons were successfull
        return True

class Thesaurus:
    def __init__(self):
        #self.terms = dict() # maybe also have a terms dict, where all concept terms and synonyms refer to that terms list with an id, to save memory
        self.concepts = dict()
        self.contexts = dict()
        self.nextid = 1

    def __iter__(self):
        for conc in self.concepts.values():
            yield conc

    def __str__(self):
        string = "--- Thesaurus ---"
        for contx,cids in self.contexts.items():
            string += "\n  %s"%contx
            for cid in cids:
                conc = self.concepts[cid]
                string += "\n    %s: %s"%(cid,conc.preferred)
        return string

    def search(self, term=None, similar=[], narrower=[], broader=[], contexts=[], matchpercent=100):
        matches = []
        if term != None:
            for cid,conc in self.concepts.items():
                if (term == conc.preferred or term in conc.synonyms) \
                   and (conc.compare(similar, narrower, broader, contexts) ):
                    matches.append(conc)
        else:
            for cid,conc in self.concepts.items():
                if (conc.compare(similar, narrower, broader, contexts) ):
                    matches.append(conc)
        # all comparisons were successfull
        return matches

    def append_concept(self, concept):
        # get and increment concept id
        cid = self.nextid
        self.nextid += 1
        # add concept
        self.concepts[cid] = concept
        # add concept id to each of its contexts
        for contx in concept.contexts:
            getcontx = self.contexts.get(contx)
            if not getcontx: self.contexts[contx] = [cid]
            else: getcontx.append(cid)
            
        

if __name__ == "__main__":
    thes = Thesaurus()

    USA = Concept(preferred="USA",
                  synonyms=["United States",
                                 "United States of America",
                                 "USA",
                                 "U.S.A.",
                                 "U.S.",
                                 "America"],
                         narrower=["Americas",
                             "Western Hemisphere",
                             "Western World",
                             "Developed World",
                             "World"],
                          contexts=["Geography","Countries"])
    Norway = Concept(preferred="Norway",
                         narrower=["Scandinavia",
                             "Northern Europe",
                             "Europe",
                             "Western Hemisphere",
                             "Western World",
                             "Developed World",
                             "World"],
                          contexts=["Geography","Countries"])
    legitimacy = Concept(preferred="legitimacy",
                         synonyms=["popular support","political support"],
                         contexts=["Politics"])

    thes.append_concept(USA)
    thes.append_concept(Norway)
    thes.append_concept(legitimacy)

    print thes

    print "Search results:"
    for conc in thes.search(narrower=["Scandinavia"], contexts=["Countries"]):
        print conc
    





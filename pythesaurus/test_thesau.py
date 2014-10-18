import pyThesaurus as pythes

thes = pythes.Thesaurus()

USA = pythes.Concept(et=["United States",
                             "United States of America",
                             "USA",
                             "U.S.A.",
                             "U.S.",
                             "America"],
                     nt=["Americas",
                         "Western Hemisphere",
                         "Western World",
                         "Developed World",
                         "World"],
                      contexts=["Geography","Countries"])
Norway = pythes.Concept(et=["Norway"],
                     nt=["Scandinavia",
                         "Northern Europe",
                         "Europe",
                         "Western Hemisphere",
                         "Western World",
                         "Developed World",
                         "World"],
                      contexts=["Geography","Countries"])

thes.append_concept(USA)
thes.append_concept(Norway)

print thes.get_terms_of_context("Countries")
print thes.search_term("United")

thes.set_prefered("USA", thes("USA")[0])
print thes.get_prefered("America", contexts=["Countries"])


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


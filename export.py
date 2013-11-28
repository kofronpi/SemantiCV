from rdflib import ConjunctiveGraph

def exportN3(graph):
    graph.serialize("exports/export.n3",format="n3")
    print("N3 export file successfully written to disk.")

def exportNT(graph):
    graph.serialize("exports/export.nt",format="nt")
    print("NT export file successfully written to disk.")

def exportTRIG(graph):
    graph.serialize("exports/export.trig",format="trig")
    print("Trig export file successfully written to disk.")

def exportTURTLE(graph):
    graph.serialize("exports/export.turtle",format="turtle")
    print("Turtle export file successfully written to disk.")


def exportRDF(graph):
    graph.serialize("exports/export.rdf",format="application/rdf+xml")
    print("RDF+XML export file successfully written to disk.")   

from rdflib import ConjunctiveGraph, Namespace, Literal, BNode

def initGraph(g):

    #define the namespace and classes :
    owlNS = Namespace("http://www.w3.org/2002/07/owl#")
    owlClass = owlNS["Class"]
    owlObjectProperty = owlNS["ObjectProperty"]
    rdfNS = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdfType = rdfNS["type"]
    rdfsNS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    rdfsSubClassOf = rdfsNS["subClassOf"]
    rdfsDomain = rdfsNS["domain"]
    rdfsRange = rdfsNS["range"]
    xsdNS = Namespace("http://www.w3.org/2001/XMLSchema#")
    xsdString = xsdNS["string"]
    

    #should define a proper namespace
    cv = Namespace("")
    cvEntryClass = cv['CVEntry']
    educationClass = cv['Education']
    organizationClass = cv['Organization']
    eduOrganizationClass = cv['EduOrg']
    companyClass = cv['Company']
    workExperienceClass = cv['WorkExperience']
    skillClass = cv['Skill']

    #define properties

    hasName = cv['has_name']
    hasLocation = cv['has_location']
    edStartDate = cv['edStartDate']
    edEndDate = cv['edEndDate']
    majorDegree = cv['majorDegree']
    minorDegree = cv['minorDegree']
    studiedIn = cv['studied_in']
    workStartDate = cv['workStartDate']
    workEndDate = cv['workEndDate']
    jobTitle = cv['jobTitle']
    jobDescription = cv['jobDescription']
    workedIn = cv['worked_in']
    skName = cv['skName']
    skCategory = cv['skCategory']
    skExpertise = cv['skExpertise']


    #define all the triples of our schema according to the ontology rules:

    schemaTriples = [
        #class declarations
        (cv['CVEntry'], rdfType, owlClass),
        (cv['Education'], rdfType, owlClass),
        (cv['Organization'], rdfType, owlClass),
        (cv['EduOrg'], rdfType, owlClass),
        (cv['Company'], rdfType, owlClass),
        (cv['WorkExperience'], rdfType, owlClass),
        (cv['Skill'], rdfType, owlClass),
        #class hierarchy
        (cv['Education'], rdfsSubClassOf, cv['CVEntry']),
        (cv['WorkExperience'], rdfsSubClassOf, cv['CVEntry']),
        (cv['Skill'], rdfsSubClassOf, cv['CVEntry']),
        (cv['Company'], rdfsSubClassOf, cv['Organization']),
        (cv['EduOrg'], rdfsSubClassOf, cv['Organization']),
        #has_name property
        (cv['has_name'], rdfType, owlObjectProperty),
        (cv['has_name'], rdfsDomain, cv['Organization']),
        (cv['has_name'], rdfsRange, xsdString),
        #hasLocation property
        (cv['has_location'], rdfType, owlObjectProperty),
        (cv['has_location'], rdfsDomain, cv['Organization']),
        (cv['has_location'], rdfsRange, xsdString),
        #edStartDate property
        (cv['edStartDate'], rdfType, owlObjectProperty),
        (cv['edStartDate'], rdfsDomain, cv['Education']),
        (cv['edStartDate'], rdfsRange, xsdString),
        #edEndDate property
        (cv['edEndDate'], rdfType, owlObjectProperty),
        (cv['edEndDate'], rdfsDomain, cv['Education']),
        (cv['edEndDate'], rdfsRange, xsdString),
        #majorDegree property
        (cv['majorDegree'], rdfType, owlObjectProperty),
        (cv['majorDegree'], rdfsDomain, cv['Education']),
        (cv['majorDegree'], rdfsRange, xsdString),
        #minorDegree property
        (cv['minorDegree'], rdfType, owlObjectProperty),
        (cv['minorDegree'], rdfsDomain, cv['Education']),
        (cv['minorDegree'], rdfsRange, xsdString),
        #studiedIn property
        (cv['studiedIn'], rdfType, owlObjectProperty),
        (cv['studiedIn'], rdfsDomain, cv['Education']),
        (cv['studiedIn'], rdfsRange, cv['EduOrg']),
        #workStartDate property
        (cv['workStartDate'], rdfType, owlObjectProperty),
        (cv['workStartDate'], rdfsDomain, cv['WorkExperience']),
        (cv['workStartDate'], rdfsRange, xsdString),
        #workEndDate property
        (cv['workEndDate'], rdfType, owlObjectProperty),
        (cv['workEndDate'], rdfsDomain, cv['WorkExperience']),
        (cv['workEndDate'], rdfsRange, xsdString),
        #jobTitle property
        (cv['jobTitle'], rdfType, owlObjectProperty),
        (cv['jobTitle'], rdfsDomain, cv['WorkExperience']),
        (cv['jobTitle'], rdfsRange, xsdString),
        #jobDescription property
        (cv['jobDescription'], rdfType, owlObjectProperty),
        (cv['jobDescription'], rdfsDomain, cv['WorkExperience']),
        (cv['jobDescription'], rdfsRange, xsdString),
        #workedIn
        (cv['worked_in'], rdfType, owlObjectProperty),
        (cv['worked_in'], rdfsDomain, cv['WorkExperience']),
        (cv['worked_in'], rdfsRange, cv['Company']),
        #skName
        (cv['skName'], rdfType, owlObjectProperty),
        (cv['skName'], rdfsDomain, cv['Skill']),
        (cv['skName'], rdfsRange, xsdString),
        #skExpertise
        (cv['skExpertise'], rdfType, owlObjectProperty),
        (cv['skExpertise'], rdfsDomain, cv['Skill']),
        (cv['skExpertise'], rdfsRange, xsdString),
        #skCategory
        (cv['skCategory'], rdfType, owlObjectProperty),
        (cv['skCategory'], rdfsDomain, cv['Skill']),
        (cv['skCategory'], rdfsRange, xsdString)
    ]

    for triple in schemaTriples:  g.add(triple)






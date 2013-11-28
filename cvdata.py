#SemantiCV v0.1
from rdflib import ConjunctiveGraph, Namespace, Literal, BNode, URIRef
from rdflib.namespace import FOAF
from inputs import camelCase

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

def addWorkExp(graph):
    company = input("What company hired you? ")
    company = camelCase(company)
    companyURI = input("What is the company website?")
    place = input("Where was the company based? ")
    dateStart = input("When did the job start? ")
    dateEnd = input("When did the job end? (skip if not applicable) ")
    jobTitle = input("What was your job title? ")
    jobDescription = input("Shortly describe what was your work. ")
    #define blank node for WE
    #define the triples:
    workExpTriple = [
        
        #a work experience uri is the company's website in our ontology
        (cv[companyURI],rdfType,cv['WorkExperience']),
        (cv[company],rdfType,cv['Company']),
        (cv[companyURI],cv['worked_in'],cv[company]),
        #place
        (cv[company],cv['has_location'],Literal(place)),
        #dateStart
        (cv[companyURI],cv['workStartDate'],Literal(dateStart)),
        #dateEnd
        (cv[companyURI],cv['workEndDate'],Literal(dateEnd)),
        #jobTitle
        (cv[companyURI],cv['jobTitle'],Literal(jobTitle)),
        #jobDescription
        (cv[companyURI],cv['jobDescription'],Literal(jobDescription))
    ]

    # bind applicant to WorkExperience
    for applicant in graph.subjects(rdfType,FOAF.Person):
        workExpTriple.append((applicant,cv['has_workExperience'],cv[companyURI]))

    for triple in workExpTriple: graph.add(triple)
    return graph
    

def addEdu(graph):
    eduOrg = input("What was your education organization? (eg: University of Technology of Sydney) ")
    eduOrg = camelCase(eduOrg)
    eduOrgURI = input("What is your education organization website? (eg: www.uts.au) ")
    ePlace = input("Where was the organization located? (eg:Sydney) ")
    dateStart = input("When did you start studying? ")
    dateEnd = input("When did or will you graduate? ")
    majorDegree = input("What major did you / will you graduate on? ")
    minorDegree = input("What minor degree did you / will you graduate on? ")
    #define blank node for education entry
    
    #define the triples:
    eduTriple = [
        #create education organization
        (cv[eduOrgURI],rdfType,cv['Education']),
        (cv[eduOrg],rdfType,cv['EduOrg']),
        (cv[eduOrg],cv['has_location'],Literal(ePlace)),
        (cv[eduOrgURI],cv['studiedIn'],cv[eduOrg]),
        (cv[eduOrgURI],cv['edStartDate'],Literal(dateStart)),
        (cv[eduOrgURI],cv['edEndDate'],Literal(dateEnd)),
        (cv[eduOrgURI],cv['majorDegree'],Literal(majorDegree)),
        (cv[eduOrgURI],cv['minorDegree'],Literal(minorDegree))

    ]

    # bind applicant to Education
    for applicant in graph.subjects(rdfType,FOAF.Person):
        eduTriple.append((applicant,cv['has_education'],cv[eduOrgURI]))
    
    for triple in eduTriple: graph.add(triple)
    return graph


def addSkill(graph):
    skName = input("Name your skill! (eg: Butterfly hunting) ")
    skName = camelCase(skName)
    skCategory = input("What's this skill category? ")
    skExpertise = input("Rate your expertise in this skill from 1 to 10. ")

    #define the triples:
    skillTriple = [
        (cv[skName],rdfType,cv['Skill']),
        # skill category
        (cv[skName],cv['skCategory'],Literal(skCategory)),
        # skill expertise
        (cv[skName],cv['skExpertise'],Literal(skExpertise)),
     ]

    # bind applicant to skill
    for applicant in graph.subjects(rdfType,FOAF.Person):
        skillTriple.append((applicant,cv['has_skill'],cv[skName]))
    
    for triple in skillTriple: graph.add(triple)
        
    return graph
    

def setApplicant(g):
    userName = input("Hello, what's your name? ")
    userEmail = input("And your email? ")
    applicant = BNode()
    g.add(  (applicant, rdfType, FOAF.Person))
    g.add( (applicant,FOAF.name, Literal(userName)))
    g.add( (applicant, FOAF.mbox, URIRef(userEmail)))

    return g
    
 
    
    

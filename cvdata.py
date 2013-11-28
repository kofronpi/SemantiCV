from rdflib import ConjunctiveGraph, Namespace, Literal, BNode
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
    place = input("Where was the company based? ")
    dateStart = input("When did the job start? ")
    dateEnd = input("When did the job end? (skip if not applicable) ")
    jobTitle = input("What was your job title? ")
    jobDescription = input("Shortly describe what was your work. ")
    #define blank node for WE
    wexp = BNode('_:worp1')
    #define the triples:
    workExpTriple = [
        #new work experience entry
        (wexp,rdfType,cv['WorkExperience']),
        #company name
        (wexp,cv['has_name'],Literal(company,datatype=xsdString)),
        #place
        (wexp,cv['has_location'],Literal(place,datatype=xsdString)),
        #dateStart
        (wexp,cv['workStartDate'],Literal(dateStart,datatype=xsdString)),
        #dateEnd
        (wexp,cv['workEndDate'],Literal(dateEnd,datatype=xsdString)),
        #jobTitle
        (wexp,cv['jobTitle'],Literal(jobTitle,datatype=xsdString)),
        #jobDescription
        (wexp,cv['jobDescription'],Literal(jobDescription,datatype=xsdString))
    ]

    for triple in workExpTriple: graph.add(triple)
    return graph
    

def addEdu():
    eduOrg = input("What was your education organization? (eg: University of Technology of Sydney) ")
    ePlace = input("Where was the organization located? (eg:Sydney) ")
    dateStart = input("When did you start studying? ")
    dateEnd = input("When did or will you graduate? ")
    majorDegree = input("What major did you / will you graduate on? ")
    minorDegree = input("What minor degree did you / will you graduate on? ")
    #write in file here


def addSkill():
    skName = input("Name your skill! (eg: Butterfly hunting) ")
    skCategory = input("What's this skill category? ")
    skExpertise = input("Rate your expertise in this skill from 1 to 10. ")
    #write in file here


#def editApplicant():
    

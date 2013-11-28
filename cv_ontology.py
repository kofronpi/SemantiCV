from rdflib import ConjunctiveGraph, Namespace, Literal, BNode, OWL, RDF, RDFS

#define the namespace and classes :

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

schemaTriple = [
    #class declarations
    





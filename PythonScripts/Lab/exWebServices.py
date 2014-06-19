# Print out function for query results (see code below function first)
def printOutput(ws_output):
    #Loops through a list of dictionary items
    index=1
    for object in ws_output:
        #calls select dictionary keys to print out values
        print_output = '   '+str(index)+')'+'species:'+object['species']+'\t '
        print_output+= 'id:'+object['id']+'\t '+'name:'+object['name']
        print print_output
        index+=1

# Load SOAPpy and dependent modules (fpconst) and access the remote
# SOAP server through a proxy class, SOAPProxy - see:
# (http://diveintopython.org/soap_web_services/first_steps.html)
from SOAPpy import SOAPProxy      
url = 'http://www.wikipathways.org/wpi/webservice/webservice.php'
namespace = 'http://www.wikipathways.org/webservice'
server = SOAPProxy(url, namespace)

# Define the order of args: needed for this service
server.config.argsOrdering = {'findPathwaysByXref': ('ids', 'codes') }

# findPathwaysByXref (multiple args; returns list of dictionary references)
sc = 'S'; gi = 'P00488'
probeset_containing = server.findPathwaysByXref(codes=sc, ids=gi )
print '\nPathways containing the gene ID "%s" for system code "%s"' % (gi,sc) 
printOutput(probeset_containing)

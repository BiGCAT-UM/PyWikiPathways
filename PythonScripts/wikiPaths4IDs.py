# wikiPaths4IDs = Get WikiPathways from www.wikipathways.org
# for a list of IDs from a CSV file (one ID by line)
# ------------------------------------------------------------------------------
# Derived from the Web services Help page:
# http://www.wikipathways.org/index.php/Help:WikiPathways_Webservice
# List of system codes:
# http://developers.pathvisio.org/wiki/DatabasesMapps#Supporteddatabasesystems
# WikiPathways Github: https://github.com/wikipathways
# ------------------------------------------------------------------------------
# # PyWikiPathways Github: 
# author: Cristian R Munteanu
# email: muntisa@gmail.com
# ------------------------------------------------------------------------------
# Use:
# - for console results:
# python wikiPaths4IDs.py [system code as string] [CSV input file name as string]
# - for output file results:
# python wikiPaths4IDs.py [system code as string] [CSV input file name as string] > [output file name as string]

# ex: python wikiPaths4IDs.py S IDs.csv > wikiPaths4IDs.res.txt
# ------------------------------------------------------------------------------

def GetWikiPaths4IDs(idList,SC):
    # Function that uses a list of IDs and a systm code as input and
    # returns a string with all the WikiPathways where th IDs exist (including the new lines) as tab separated fields:
    # No, ID, Species, Pathway ID, Pathway Name

    # Load SOAPpy and dependent modules (fpconst) and access the remote
    # SOAP server through a proxy class, SOAPProxy - see:
    # (http://diveintopython.org/soap_web_services/first_steps.html)

    from SOAPpy import SOAPProxy
    url = 'http://www.wikipathways.org/wpi/webservice/webservice.php'
    namespace = 'http://www.wikipathways.org/webservice'
    server = SOAPProxy(url, namespace)

    # Define the order of args: needed for this service
    server.config.argsOrdering = {'findPathwaysByXref': ('ids', 'codes') }
    
    index=1 # index of the result lines
    print_output = '' # output of the function
    # For each ID findPathwaysByXref (multiple args; returns list of dictionary references)
    for gi in idList:
        # checking any erors
        try:
            probeset_containing = server.findPathwaysByXref(codes=SC, ids=gi)
            NoPaths = len(probeset_containing)
            #Loops through a list of dictionary items if results
            if NoPaths > 0 :
                for object in probeset_containing:
                    #calls select dictionary keys to print out values            
                    print_output += str(int(index))+'\t'+str(gi)+'\t'+str(object['species'])+'\t'+str(object['id'])+'\t'+str(object['name'])+'\n'
                    index+=1
            else:
                print gi, "can't be found in WikiPathways!"
        except:
            #pass # if error do nothing
            print gi, 'has', NoPaths, 'pathways but it can be processed!'
    return print_output
        
##########################################
# MAIN
##########################################

import sys

# Parameters from the command line
# -------------------------------------------
# sys.argv[1] = type of system codes used by WikiPathways [string]
# sys.argv[2] = CSV file name with one column of IDs      [string]

if __name__ == "__main__":
    # Read the input file and return wikiPatways as list
    print GetWikiPaths4IDs(([line.strip() for line in open(sys.argv[2])]),sys.argv[1])[:-1]

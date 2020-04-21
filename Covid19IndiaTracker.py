# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:23:51 2020

@author: herald jose
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:51:35 2020

@author: herald jose
"""

from urllib.request import urlopen
import json

#loads date in json format from url.
def loaddata(url):
    site=urlopen(url)
    return(json.load(site))
    
#checks if the name of the state inputed is valid and if its in
#in the list.Returns the index of the state in the list.
def datacheck(a,string):
    for i in range(len(a.get('data')[0].get('table'))):
        if a.get('data')[0].get('table')[i].get('state')==string:
            return(int(i))
            break
    else:#if name of state is absent function returns nothing and show error.
        print('Check for spelling Errors')
        return(None)
        
 #prints data from loaded list       
def printout(a,index,string):
    try:
        activecases=a.get('data')[0].get('table')[index].get('active')
        totaldeaths=a.get('data')[0].get('table')[index].get('deaths')
        updatedon=a.get('data')[0].get('table')[index].get('lastupdatedtime')
        rec=a.get('data')[0].get('table')[index].get('recovered')
        print('Number of active cases in',string,':',activecases)
        print('Total number of deaths in',string,':',totaldeaths)
        print('Total Recoveries :',rec)
        print('Date Updated on:',updatedon)
    except:
        pass 


def main():
    url='https://covid19-server.chrismichael.now.sh/api/v1/IndiaCasesByStates'
    #take name of state as input and converts to format as in list given
    #by API.
    ans=str(input('Input State Name : ')).split()
    statename=' '.join([str(i).capitalize() for i in ans])
    data=loaddata(url)
    index=datacheck(data,statename)
    printout(data,index,statename)
    
    
if __name__=='__main__':
    main()
    

        
      
        


import re
import requests
import urllib.request
import pandas
from threading import Thread

#imports CSV containing link list
links = pandas.read_csv("url_list.csv")
total_links=links["URL"].values.tolist()

#defines string to search for
search_string = "Kalymnos"

valid_urls = []

#loops through link list
for i in range(0,len(total_links)):
    
    #prints current link being scraped
    print(total_links[i])
    
    #requests website data
    web_response = requests.get(total_links[i], verify=False)
    
    #if request is successful
    if web_response.status_code==200:
        
        #stores website's data
        html_content = urllib.request.urlopen(total_links[i]).read().decode('utf-8')
        
        #checks if string is found on website and adds link to valid url list if yes
        matches = re.search(search_string, html_content)
        if matches:
            valid_urls.append(total_links[i])

        


#Outputs the valid url list to txt file
f = open('output.txt', 'w')
f.write('List of all the web links in which "'+ search_string + '" is present:- \n\n')
for link in valid_urls:
    f.write(link+"\n")
f.close()

#Completion message
print("\n \033[1m The resultant links has been successfully exported to output.txt file, \
in your default current directory. \033[0m\n\n")

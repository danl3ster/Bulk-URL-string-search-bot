import re
import requests
import urllib.request
import pandas
from threading import Thread

links = pandas.read_csv("url_list.csv")
total_links=links["URL"].values.tolist()
search_string = "Kalymnos"
valid_urls = []

for i in range(5000,len(total_links)):
    print(total_links[i])
    web_response = requests.get(total_links[i], verify=False)
    if web_response.status_code==200:
        html_content = urllib.request.urlopen(total_links[i]).read().decode('utf-8')
        matches = re.search(search_string, html_content)
        if matches:
            valid_urls.append(total_links[i])

        



f = open('output.txt', 'w')
f.write('List of all the web links in which "'+ search_string + '" is present:- \n\n')

for link in valid_urls:
    f.write(link+"\n")
f.close()

print("\n \033[1m The resultant links has been successfully exported to output.txt file, \
in your default current directory. \033[0m\n\n")

import re
import urllib2
import sys

def temp():
    url ='http://results.vtu.ac.in/results/result_page.php?usn=%s'%sys.argv[1]  
    req = urllib2.urlopen(url)
    item = req.read()

    usn_details = re.findall('<table[\s\S]*?<\/table>',item)[0]

    usn_details = re.sub('<.*?>','',usn_details)
    usn_details = re.sub('[\r\t'']','',usn_details)
    usn_details = usn_details.split('\n')
    for usn in usn_details:
        if usn == '':
            usn_details.remove(usn)
        
    usn_details = usn_details[0:-2]
    usn_details.remove('')
    usn_details[1] = usn_details[1].split(': ')[1]
    usn_details[3] = usn_details[3].split(': ')[1]

    data_usn = {}
    data_usn[usn_details[0]] = usn_details[1]
    data_usn[usn_details[2]] = usn_details[3]
    print
    print data_usn
    print
    result_headers = re.findall('[\s\S]<thead>([\s\S]*)<\/thead>',item)


    result_headers = result_headers[0]

    result_headers = re.findall(r'<th style="text-align:center;">(.*?)<\/th>',result_headers)
    print
    print result_headers
    print
    sub_results = re.findall(r'<tbody>([\s\S]*?)<\/tbody>',item)
    data = []
    for bob in sub_results:
        sub = re.sub(r'<.*?>','',bob) 
        sub = re.sub(r'[\r\t]','',sub)
        a = sub.split('\n')  
        for col in a:
            if col == '':
                a.remove(col)
        sub = a[0:-2] 
        data.append(sub) 

    for sub in data:
        print sub

temp()


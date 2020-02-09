#Patterned after CTA Bus Tracker API Pythonista Project
#https://github.com/kpphillips/Pythonista-Projects/tree/master/CTA%20Bus%20Tracker%20API

#imports
import pakey
import requests
import json

#Port Authority API Docs
print('http://realtime.portauthority.org/bustime/apidoc/docs/DeveloperAPIGuide3_0.pdf' + '\n')

#Constants
baseUrl='http://truetime.portauthority.org/bustime/api/v3/'
dataFeed='Port Authority Bus'
#dataFeed='Light Rail'
apiKey=pakey.apiKey


#request
def request(url):
    r=requests.get(url)
    parsed_json = json.loads(r.content)
    print('\nResponse from Port Authority API.\n')
    return parsed_json


#Time
def getTime():
    apiCall='gettime'
    url=baseUrl + apiCall + '?key=' + apiKey + '&format=json'
    return request(url)


#Vehicles
def getVehicles(vids_or_rts,vids=True):
    apiCall='getvehicles'
    query=''
    if vids:
        query += '&vid='
        for vid in vids_or_rts:
            query += vid + ','
    else:
        query += '&rt='
        for rt in vids_or_rts:
            query += rt + ','

    url=baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
    return request(url)


#Routes
def getRoutes():
    apiCall='getroutes'
    url=baseUrl + apiCall + '?key=' + apiKey + '&format=json'
    return request(url)


#Route Directions
def getDirections(rt):
    apiCall='getdirections'
    query = '&rt=' + rt + '&rtpidatafeed=' + dataFeed
    url=baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
    return request(url)


#Stops
def getStops(rt,dir):
    dirs_json=getDirections(rt)
    dirs=dirs_json['bustime-response']['directions']
    direction=dirs[dir]['id']
    apiCall='getstops'
    query1 = '&rt=' + rt
    query2 = '&dir=' + direction + '&rtpidatafeed=' + dataFeed    

    url=baseUrl + apiCall + '?key=' + apiKey + query1 + query2 +'&format=json'
    return request(url)

    
def getPatterns(rt_or_pids,rt=True):
	apiCall='getpatterns'
	query1=''
	query2='&rtpidatafeed=' + dataFeed
	if rt:
		query1 += '&rt=' + rt_or_pids
	else:
		query1 += '&pid='
		for pid in rt_or_pids:
			query1 += pid + ','
	
	url= baseUrl + apiCall + '?key=' + apiKey + query1 + query2 +'&format=json'
	return request(url)

											
#Predictions
def getPredictions(vids_or_stpids,rts,stpids=True,top=4):
	apiCall='getpredictions'
	query1=''
	query2='&rtpidatafeed=' + dataFeed
	if stpids:
		query1 += '&rt='
		for rt in rts:
			query1 += rt + ','
		query1 += '&stpid=' + vids_or_stpids	
	else:
		query1 += '&pvid='
		for vid in vids_or_stpids:
			query1 += vid + ','
	
	url= baseUrl + apiCall + '?key=' + apiKey + query1 + query2 +'&format=json'
	return request(url)

    
#Service bulletins
def getBulletins(rt):
    apiCall='getservicebulletins'
    query = '&rt=' + rt + '&rtpidatafeed=' + dataFeed
    url=baseUrl + apiCall + '?key=' + apiKey + query +'&format=json'
    return request(url)


#Feeds
def getFeeds():
    apiCall='getrtpidatafeeds'
    url=baseUrl + apiCall + '?key=' + apiKey + '&format=json'
    return request(url)


#Detours


#Locales


#Error Codes
#http:///www.transitchicago.com/developers

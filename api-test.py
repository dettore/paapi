import paapi as c
import json

# ** WORKS **
# Stop 568 is lower PNR lot

r=c.getTime()
#r=c.getVehicles(['8'],False)
#r=c.getRoutes()
#r=c.getDirections('8')
#r=c.getStops('8',1)
#r=c.getPatterns('8')
#r=c.getFeeds()

def testPredictions():
    
    # 1502 is Stanwix
    # 45 is Market at Liberty
    #r=c.getPredictions('568',['8'])
    #r=c.getPredictions('618',['8'])  # at West View Towers
    r=c.getPredictions('733',['8'])    # at West view Tower (Park Plaza Dr)
    # 15716 is Upper Lot PNR
    #r=c.getPredictions('15716',['O1'])

    ##
    print(json.dumps(r, indent=1))
    ##TODO:  Handle error returned in json when no arrival times
    ##
    ###get bus predicted times
    prds=r['bustime-response']['prd']
    prd1=prds[0]
    print(prd1['stpnm'])
    print(prd1['rtdir'])

    for prd in prds:
            print(prd['prdctdn'])

def testBulletins():
    r=c.getBulletins('8')
    ##TODO Handle error when no data is found
    sbs=r['bustime-response']['sb']
    sb1=sbs[0]
    #print(sb1['stpnm'])
    #print(sb1['rtdir'])

    for sb in sbs:
            print(sb['sbj'])
            print(sb['dtl']+'\n')
            #print(sb['brf']+'\n')
            

#Print results of the api calls
print(json.dumps(r, indent=1))

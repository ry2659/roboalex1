import urllib.request,json
import urllib
from prettytable import PrettyTable
import os
from flask import Flask
from flask import request
from flask import make_response
app=Flask(__name__)
@app.route('/webhook',methods=['POST'])
def webhook():
    req=request.get_json(silent=True,force=True)
    print("Request : ")
    print(json.dumps(req,indent=4))
    res=makeWebhookResult(req)
    res==json.dumps(res,indent=4)
    print(res)
    r=make_response(res)
    r.headers['Content-type']='application/json'
    return r
def makeWebhookResult(req):
    if req.get("result").get("action")!='sedolNumber.Action':
        return{}
    result=req.get("result")
    parameters=result.get("parameters")
    sedol=parameters.get("sedolNumber")
    fund={'BSL1000':'First Fund','BSL0006':'second fund'}
    speech="Fund Detail of "+sedol+" is"+str(fund)
    print("Response")
    print(speech)
    return{
        "speech":speech,
        "displayText":speech,
        "source":"api122"

        }

'''
    ...t=PrettyTable(['SedolNumber','Fund Name','folioNo'])
    flag=True
    with open("D:\\rahul_yadav\\python\\ifastfunds.json",'r') as json_file:
        data = json.load(json_file)
        #print(data)
        sedolnum=input('Enter Sedol Number : ')
    
        for d in data['data']:
            for it in d['sell']:
                if it['sedolNumber']==sedolnum:
                     t.add_row([it['sedolNumber'],it['fundName'],it['folioNo']])
                     #print('SedolNumber : ',it['sedolNumber'],' fundName : ',it['fundName'],' folioNo : ',it['folioNo'])
                else:
                    flag=False
                    #print('Data Not Found')
                    #print('data not found')
                    #t.add_row(['Data no Found','',''])
                    #break
                



print (t)...
'''
if __name__=='__main__':
    port=int(os.getenv('PORT',80))
    print("Starting app on port %d"%(port))
    app.run(debug=True,port=port,host='0.0.0.0')





import requests
import json 

url = 'http://35.231.1.23:8080/sendmessages'
# myobj = {'buttons':[{'name':'neet','action':'playquiz'},{'name':'jee','action':'dosomething1'}]}
# myobj={'buttons':'love'}
# myobj=[5361834379]

myobj={'chat_ids':[5361834379,5033354066,1664876303,5129193582],'text':'Hi , This message is from live app '}
myobj=json.dumps(myobj)
print(myobj)

x = requests.post(url, json = myobj)

# print(x.text)
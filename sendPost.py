# curl -i -X POST -H "ContentType: application/json" -d 
# '{"username":"Wes","password":"starbucks"}' http://0.0.0.0:5000/api/users
import httplib2
import json

def sendPostRequest():
    # url = "http://0.0.0.0:5000/words"
    # headers = {"content-type": "application/json"}
    # letters = list(char for char in letters.upper())
    # data = {'letters': letters}
    # # print('\ndata', data)
    # body = json.dumps(data).encode('utf8')
    # print('\nbody', body)
    h = httplib2.Http()
    # response, content = h.request(uri=url, method="POST", headers=headers, body=body)
    # # print("\nresponse",response)
    # # print("\ncontent",content)
    # best_words = json.loads(content)['words']
    # print("BEST WORDS\t",best_words)
    
    url = "http://0.0.0.0:5000/words/GUIDOXA"
    response, content = h.request(uri=url, method="GET")
    best_words = json.loads(content)['words']
    print("BEST WORDS\t",best_words)
if __name__ == '__main__':
    # letters = str(input("Enter up to 7 letters"))
    sendPostRequest()
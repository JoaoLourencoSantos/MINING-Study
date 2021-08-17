import requests
import json

def callGitApi(url, query):
  result =  requests.post( url, 
              headers= {'Authorization': 'bearer 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'}, 
              json={'query': query}
            )
            
  print("Result status from request - ", result.status_code) 

  data = json.loads(result.text)['data']['search']['nodes']   

  return data
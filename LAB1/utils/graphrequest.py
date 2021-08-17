from LAB1.secrets.secret import getKeyFromGit
import requests
import json

def callGitApi(url, query):
  result =  requests.post( url, 
              headers= {'Authorization': 'bearer ' + getKeyFromGit()}, 
              json={'query': query}
            )
            
  print("Result status from request - ", result.status_code) 

  data = json.loads(result.text)['data']['search']['nodes']   

  return data
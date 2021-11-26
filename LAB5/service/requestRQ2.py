from utils.gitquerys import  getFirstQueryGraph, getFirstQueryREST, getSecondQueryGraph, getSecondQueryREST
import requests
import json
from datetime import datetime 
import pandas 

pageSizes = [25, 50, 75 , 100]

GIT_URL = 'https://api.github.com/graphql'
RQ2_GRAPH_FILE = './csv/RQ2/GRAPH_REQUESTS.csv'
RQ2_REST_FILE = './csv/RQ2/REST_REQUESTS.csv'

def executeGraphQueriesRQ2(): 
    data = []
 
    for x in range(0, 5):  

        query = getFirstQueryGraph(50)

        resultOfApi = callGitWithGraph(GIT_URL, query)
        requestSize = len(resultOfApi) 

        print('Request size > ', requestSize)  
        
        data.append({
            "type": 'GRAPHQL',
            "query": 'REPOSITORY_QUERY',
            "size": requestSize
        })

    for x in range(0, 5):  

        query = getSecondQueryGraph(50)

        resultOfApi = callGitWithGraph(GIT_URL, query)
        requestSize = len(resultOfApi) 

        print('Request size > ', requestSize)  
        
        data.append({
            "type": 'GRAPHQL',
            "query": 'USER_QUERY',
            "size": requestSize
        })     
            
    saveInFile(RQ2_GRAPH_FILE, data)

    return data

def executeRestQueriesRQ2(): 
    data = []
 
    for x in range(0, 5):  

        url = getFirstQueryREST(50)

        resultOfApi = callGitWithREST(url)
        requestSize = len(resultOfApi) 

        print('Request size > ', requestSize)  
        
        data.append({
            "type": 'REST',
            "query": 'REPOSITORY_QUERY',
            "size": requestSize
        }) 

    for x in range(0, 5):  

        url = getSecondQueryREST(50)

        resultOfApi = callGitWithREST(url)
        requestSize = len(resultOfApi) 

        print('Request size > ', requestSize)  
        
        data.append({
            "type": 'REST',
            "query": 'USER_QUERY',
            "size": requestSize
        }) 

    saveInFile(RQ2_REST_FILE, data)

    return data


def callGitWithGraph(url, query):

    result = requests.post(url,
                           headers={
                               'Authorization': 'bearer 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'},
                           json={'query': query}
                           ) 
    print(" [*] Result status from request - ", result.status_code)

    return result.text

def callGitWithREST(url):

    result = requests.get(url,
                           headers={
                               'Authorization': 'bearer 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'},
                           ) 
    print(" [*] Result status from request - ", result.status_code)
 
    return result.text


def saveInFile(file, result):
    if (result is None):
        print('Error on build result data')
    else:
        json_string = json.dumps(result)

        df_data = json.loads(json_string)
        df = pandas.DataFrame(df_data)

        df.to_csv(file, sep=',', encoding='UTF-8')

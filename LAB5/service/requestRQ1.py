from utils.gitquerys import  getFirstQueryGraph, getFirstQueryREST
import requests
import json
from datetime import datetime 
import pandas
 
limitData = 3


pageSizes = [25, 50, 75 , 100]

GIT_URL = 'https://api.github.com/graphql'
RQ1_GRAPH_FILE = './csv/RQ1/GRAPH_REQUESTS.csv'
RQ1_REST_FILE = './csv/RQ1/REST_REQUESTS.csv'

def executeGraphQueriesRQ1(): 
    data = []
 
    for requestSize in pageSizes:

        for x in range(0, 5): 
            start = datetime.now()

            resultOfApi = callGitWithGraph(GIT_URL, requestSize) 

            request_time = (datetime.now() - start).total_seconds() * 1000 

            print('Duração > ', request_time)  
            
            data.append({
                "type": 'GRAPHQL',
                "size": requestSize,
                "time": request_time
            })

    saveInFile(RQ1_GRAPH_FILE, data)

    return data

def executeRestQueriesRQ1(): 
    data = []
 
    for requestSize in pageSizes:

        for x in range(0, 5): 
            start = datetime.now()

            resultOfApi = callGitWithREST(requestSize) 

            request_time = (datetime.now() - start).total_seconds() * 1000 

            print('Duração > ', request_time)  

            data.append({
                "type": 'REST',
                "size": requestSize,
                "time": request_time
            })

    saveInFile(RQ1_REST_FILE, data)

    return data


def callGitWithGraph(url, pageSize):

    query = getFirstQueryGraph(pageSize)

    result = requests.post(url,
                           headers={
                               'Authorization': 'bearer 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'},
                           json={'query': query}
                           ) 
    print(" [*] Result status from request - ", result.status_code)

    data = json.loads(result.text)['data']['search']

    return data

def callGitWithREST(pageSize):

    query = getFirstQueryREST(pageSize)

    result = requests.get(query,
                           headers={
                               'Authorization': 'bearer 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'},
                           ) 
    print(" [*] Result status from request - ", result.status_code)

    data = json.loads(result.text)['items']

    return data


def saveInFile(file, result):
    if (result is None):
        print('Error on build result data')
    else:
        json_string = json.dumps(result)

        df_data = json.loads(json_string)
        df = pandas.DataFrame(df_data)

        df.to_csv(file, sep=',', encoding='UTF-8')

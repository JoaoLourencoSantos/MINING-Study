import json
from models.resultmodel import ResultModel

def parseDataTables(data):

    result = []
    for value in data:    
        singleResult    =  ResultModel.toJson(
            value['id'],
            value['nameWithOwner'],
            value['createdAt'],
            value['updatedAt'],
            value['primaryLanguage'],
            value['stargazers'],
            value['pullRequests'],
            value['releases'],
            value['totalIssues'],
            value['closedIssues'] 
        )
  
        result.append(singleResult)

    return result 



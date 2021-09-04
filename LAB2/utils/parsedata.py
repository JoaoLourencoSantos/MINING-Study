import json
from models.resultmodel import ResultModel

def parseDataTables(data):

    result = []
    for value in data:    
        singleResult    =  ResultModel.toJson(
            value['id'],
            value['nameWithOwner'],
            value['createdAt'], 
            value['primaryLanguage'],
            value['stargazers'], 
            value['releases'] 
        )
  
        result.append(singleResult)

    return result 



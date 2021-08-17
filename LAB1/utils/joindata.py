import json
from models.resultmodel import ResultModel

def joinDataTables(firstData, secondData):

    result = []
    for value in firstData:  
        
        closedIssues = findClosedIssuesByRep(value['id'], secondData) 
 
        singleResult    =  ResultModel.toJson(
            value['id'],
            value['nameWithOwner'],
            value['createdAt'],
            value['updatedAt'],
            value['primaryLanguage'],
            value['stargazers'],
            value['pullRequests'],
            value['releases'],
            value['issues'],
            closedIssues
        )
  
        result.append(singleResult)

    return result
    
def findClosedIssuesByRep(id, data): 
    for value in data: 
        if (value['id'] == id) :
            return value['issues']['totalCount']




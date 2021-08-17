import json

class ResultModel:
      ## DEU RUIM ao gerar como classe ele printava com '(' e cada parametro',)' 
      def __init__(self,id,nameWithOwner, createdAt, updatedAt, primaryLanguage, stargazers, pullRequests, releases, issues, closedIssues):
            self.id =id,
            self.nameWithOwner = nameWithOwner,
            self.createdAt= createdAt,
            self.updatedAt = updatedAt,
            self.primaryLanguage = primaryLanguage['name'] if  primaryLanguage else "",
            self.stargazers = stargazers['totalCount'] if  stargazers else "",
            self.pullRequests= pullRequests['totalCount'] if  pullRequests else "",
            self.releases= releases['totalCount'] if  releases else "",
            self.issues= issues['totalCount'] if  issues else "",
            self.closedIssues= closedIssues if  closedIssues else ""
      
      def toJson(id,nameWithOwner, createdAt, updatedAt, primaryLanguage, stargazers, pullRequests, releases, issues, closedIssues):
            return {
                  "id": id,
                  "nameWithOwner": nameWithOwner,
                  "createdAt": createdAt,
                  "updatedAt": updatedAt,
                  "primaryLanguage": primaryLanguage['name'] if  primaryLanguage else "",
                  "stargazers": stargazers['totalCount'] if  stargazers else "",
                  "pullRequests":pullRequests['totalCount'] if  pullRequests else "",
                  "releases":releases['totalCount'] if  releases else "",
                  "issues":issues['totalCount'] if  issues else "",
                  "closedIssues":closedIssues if  closedIssues else ""
            }
            
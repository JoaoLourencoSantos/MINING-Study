
def getPage(page) :
   return (  "null"  if page == None else "\"" + str(page) + "\"")

def getFirstQueryGraph(size):
    return """
     {
      search(type: REPOSITORY, first: """ + str(size) + """, query: "stars:>100 language:Java created:>=2018-01-01 sort:stars-desc") {
        nodes {
          ... on Repository {
            url
            owner {
              login
            }
          }
        }
      }
    }


    """  


def getFirstQueryREST(size):
    return """
     https://api.github.com/search/repositories?q=language:Java+stars:>100+created:>=2018-01-01+sort:stars-desc&per_page=""" + str(size) + """&page=1
    """  


def getSecondQueryGraph(size):
    return """
    {
      search(type: USER, first: """ + str(size) + """, query: "followers:>10000 sort:followers-desc") {
        nodes {
          ... on User {
            url
          }
        }
      }
    }
    """  

def getSecondQueryREST(size):
    return """
     https://api.github.com/search/users?q=followers:>10000+sort:followers-desc&per_page=""" + str(size) + """&page=1
    """  
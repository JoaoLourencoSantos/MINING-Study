
def getPage(page) :
   return (  "null"  if page == None else "\"" + str(page) + "\"")

def getFirstQuery(size, page):
    return """
      {
        search(query: "stars:>100 language:Java", type: REPOSITORY, first: """ + str(size) + """, after: """ + getPage(page) + """) { 
          pageInfo {
            hasNextPage
            endCursor
          }
          nodes {
            ... on Repository {
              id
              nameWithOwner
              createdAt
              primaryLanguage {
                name
              }
              stargazers {
                totalCount
              }
              releases {
                totalCount
              }
            }
          }
        }
      }

"""  
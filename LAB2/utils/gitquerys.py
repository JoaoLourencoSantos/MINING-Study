
def getPage(page) :
   return (  "null"  if page == None else "\"" + str(page) + "\"")

def getFirstQuery(size, page):
    return """
      {
        search(query: "stars:>100", type: REPOSITORY, first: """ + str(size) + """, after: """ + getPage(page) + """) {
          pageInfo {
            hasNextPage
            endCursor
          }
          nodes {
            ... on Repository {
              id
              nameWithOwner
              createdAt
              updatedAt
              primaryLanguage {
                name
              }
              stargazers {
                totalCount
              }
              pullRequests(states: MERGED) {
                totalCount
              }
              releases {
                totalCount
              }
              totalIssues: issues {
                totalCount
              }
              closedIssues: issues(states: CLOSED) {
                totalCount
              }
            }
          }
        }
      }

""" 
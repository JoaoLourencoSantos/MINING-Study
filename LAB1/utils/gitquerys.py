size = "100"

firstQuery = """
query {
  search(query: "stars:>100", type: REPOSITORY, first: """ + size + """) {
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
        issues {
          totalCount
        }
      }
    }
  }
}

"""

secondQuery = """
query {
  search(query: "stars:>100", type: REPOSITORY, first: """ + size + """) {
    nodes {
      ... on Repository {
        id
        nameWithOwner 
        issues(states: CLOSED) {
          totalCount
        }
      }
    } 
  }
}

"""


def getFirstQuery():
    return firstQuery


def getSecondQuery():
    return secondQuery

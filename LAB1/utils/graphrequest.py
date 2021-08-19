from utils.gitquerys import getFirstQuery
import requests
import json

pageSize = 100
limitData = 1000


def callGitApiPaginated(url):

    hasNext = True
    page = None
    data = []

    while(hasNext and len(data) < limitData):
        resultOfApi = callGitByPage(url, page)

        if (resultOfApi):
            hasNext = resultOfApi['pageInfo']['hasNextPage']
            page = resultOfApi['pageInfo']['endCursor']
            data.extend(resultOfApi['nodes'])

    return data


def callGitByPage(url, page):

    query = getFirstQuery(pageSize, page)

    result = requests.post(url,
                           headers={
                               'Authorization': 'bearer YOUR_TOKEN'},
                           json={'query': query}
                           )

    print("Result status from request - ", result.status_code)

    data = json.loads(result.text)['data']['search']

    return data

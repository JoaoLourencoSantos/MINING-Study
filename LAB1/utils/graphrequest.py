import requests
import json


def callGitApi(url, query):
    result = requests.post(url,
                           headers={
                               'Authorization': 'bearer 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'},
                           json={'query': query}
                           )

    print("Result status from request - ", result.status_code)

    data = json.loads(result.text)['data']['search']['nodes']

    return data

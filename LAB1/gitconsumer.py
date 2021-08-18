from utils.joindata import joinDataTables
from utils.gitquerys import getFirstQuery, getSecondQuery
from utils.graphrequest import callGitApi
import requests
import json
import pandas

GIT_URL = 'https://api.github.com/graphql'

firstResult = callGitApi(GIT_URL, getFirstQuery())
secondResult = callGitApi(GIT_URL, getSecondQuery())

result = joinDataTables(firstResult, secondResult)

if (result is None):
    print('Error on build result data')
else:
    json_string = json.dumps(result)

    df_data = json.loads(json_string)
    df = pandas.DataFrame(df_data)

    print(" [*] Printing datatable result")
    print(df)

    df.to_csv('csv/GIT_RESULT.csv', sep=';', encoding='UTF-8')

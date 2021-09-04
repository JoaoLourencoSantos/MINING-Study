from service.graphrequest import callGitApiPaginated
from utils.parsedata import parseDataTables
import json
import pandas

GIT_URL = 'https://api.github.com/graphql'

resultData = callGitApiPaginated(GIT_URL)

result = parseDataTables(resultData)

if (result is None):
    print('Error on build result data')
else:
    json_string = json.dumps(result)

    df_data = json.loads(json_string)
    df = pandas.DataFrame(df_data)

    print(" [*] Printing datatable result")
    print(df)

    df.to_csv('csv/GIT_RESULT.csv', sep=',', encoding='UTF-8')

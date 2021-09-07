

from service.metriccalculator import generateMetrics
from service.projectmanager import clearProject, cloneProject
from models.resultmodel import ResultModel
import json
import pandas


def parseDataTables(data):

    result = []
    for value in data:

        singleResult = ResultModel.toJson(
            value['id'],
            value['nameWithOwner'],
            value['createdAt'],
            value['primaryLanguage'],
            value['stargazers'],
            value['releases']
        )

        buildMetrics(value['nameWithOwner'], singleResult)

        result.append(singleResult)

        saveLineInFile(result)

    return result


def buildMetrics(projectName, entity):

    if (cloneProject(projectName)):
        metrics = generateMetrics()

        if (metrics is None):
            print(' [*] Error on build metrics!!!')
            return

        entity['CBO'] = str(metrics['cbo'])
        entity['DIT'] = str(metrics['dit'])
        entity['LOC'] = str(metrics['loc'])
        entity['LCOM'] = str(metrics['lcom'])

        clearProject()


def saveLineInFile(result):
    if (result is None):
        print('Error on build result data')
    else:
        json_string = json.dumps(result)

        df_data = json.loads(json_string)
        df = pandas.DataFrame(df_data) 

        df.to_csv('csv/REPOSITORIES_WITH_METRICS.csv', sep=',', encoding='UTF-8')



from service.metriccalculator import generateMetrics
from service.projectmanager import clearProject, cloneProject
from models.resultmodel import ResultModel


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

from service.graphrequest import callGitApiPaginated
from utils.parsedata import isPopulatedFile, iterateAndGenerateMetrics,  parseRepositoriesToCsv

GIT_URL = 'https://api.github.com/graphql'

if (isPopulatedFile()):
    print("THE PROJECTS SEARCH OF GIT WAS COMPLETE, I WILL GENERATE METRICS")
    iterateAndGenerateMetrics()
else:
    resultData = callGitApiPaginated(GIT_URL)
    parseRepositoriesToCsv(resultData)
    iterateAndGenerateMetrics()

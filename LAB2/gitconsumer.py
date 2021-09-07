from service.graphrequest import callGitApiPaginated
from utils.parsedata import parseDataTables
import json
import pandas

GIT_URL = 'https://api.github.com/graphql'

resultData = callGitApiPaginated(GIT_URL)

parseDataTables(resultData)


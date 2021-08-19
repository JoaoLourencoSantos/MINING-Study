
from datetime import date
from utils.dateutils import dateWithIso, dateWithoutHours, diferenceInDays, getCurrentDate


class ResultModel:
    # DEU RUIM ao gerar como classe ele printava com '(' e cada parametro',)'
    def __init__(self, id, nameWithOwner, createdAt, updatedAt, primaryLanguage, stargazers, pullRequests, releases, issues, closedIssues):
        self.id = id,
        self.nameWithOwner = nameWithOwner,
        self.createdAt = createdAt,
        self.updatedAt = updatedAt,
        self.primaryLanguage = primaryLanguage['name'] if primaryLanguage else "",
        self.stargazers = stargazers['totalCount'] if stargazers else "",
        self.pullRequests = pullRequests['totalCount'] if pullRequests else "",
        self.releases = releases['totalCount'] if releases else "",
        self.issues = issues['totalCount'] if issues else "",
        self.closedIssues = closedIssues['totalCount'] if closedIssues else ""

    def toJson(id, nameWithOwner, createdAt, updatedAt, primaryLanguage, stargazers, pullRequests, releases, totalIssues, closedIssues):

        currentDate = getCurrentDate()
        lastUpdate = dateWithIso(updatedAt)

        return {
            "HashId": id,
            "ProjectName": nameWithOwner,
            "UpdateAt": dateWithoutHours(updatedAt),
            "TimeToUpdate": diferenceInDays(lastUpdate, currentDate),
            "CreatedAt": dateWithoutHours(createdAt),
            "PrimaryLanguage": primaryLanguage['name'] if primaryLanguage else "0",
            "Stargazers": stargazers['totalCount'] if stargazers else "0",
            "TotalOfPullRequests": pullRequests['totalCount'] if pullRequests else "0",
            "TotalOfReleases": releases['totalCount'] if releases else "0",
            "TotalOfIssues": totalIssues['totalCount'] if totalIssues else "0",
            "TotalOfClosedIssues": closedIssues['totalCount'] if closedIssues else "0"
        }

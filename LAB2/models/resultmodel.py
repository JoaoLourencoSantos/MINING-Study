
from datetime import date
from utils.dateutils import calcRate, dateWithIso, dateWithoutHours, diferenceInDays, diferenceInYears, getCurrentDate


class ResultModel:         
    def toJson(id, nameWithOwner, createdAt, updatedAt, primaryLanguage, stargazers, pullRequests, releases, totalIssues, closedIssues):

        currentDate = getCurrentDate()
        lastUpdate = dateWithIso(updatedAt)
        isoCreatedAt = dateWithIso(createdAt)

        totalIssues = totalIssues['totalCount'] if totalIssues else 0
        closedIssues = closedIssues['totalCount'] if closedIssues else 0

        return {
            "HashId": id,
            "ProjectName": nameWithOwner,
            "UpdateAt": dateWithoutHours(updatedAt),
            "TimeToUpdate": diferenceInDays(lastUpdate, currentDate),
            "CreatedAt": dateWithoutHours(createdAt),
            "Age": diferenceInDays(isoCreatedAt, currentDate),
            "PrimaryLanguage": primaryLanguage['name'] if primaryLanguage else "-",
            "Stargazers": stargazers['totalCount'] if stargazers else "0",
            "TotalOfPullRequests": pullRequests['totalCount'] if pullRequests else "0",
            "TotalOfReleases": releases['totalCount'] if releases else "0",
            "TotalOfIssues": totalIssues,
            "TotalOfClosedIssues": closedIssues,
            "RateOfIssues": calcRate(closedIssues,  totalIssues)
        }
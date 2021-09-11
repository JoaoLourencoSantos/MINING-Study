
from datetime import date
from utils.dateutils import dateWithIso, dateWithoutHours, diferenceInYears, getCurrentDate


class ResultModel:
    def toJson(id, nameWithOwner, createdAt, primaryLanguage, stargazers, releases):

        currentDate = getCurrentDate()
        isoCreatedAt = dateWithIso(createdAt)

        return {
            "HashId": id,
            "ProjectName": nameWithOwner,
            "CreatedAt": dateWithoutHours(createdAt),
            "Age": diferenceInYears(isoCreatedAt, currentDate),
            "PrimaryLanguage": primaryLanguage['name'] if primaryLanguage else "-",
            "Stargazers": stargazers['totalCount'] if stargazers else "0",
            "TotalOfReleases": releases['totalCount'] if releases else "0", 
            'CBO': '-',
            'DIT': '-',
            'LOC': '-',
            'LCOM': '-',
        }

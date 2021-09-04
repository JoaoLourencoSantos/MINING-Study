import os
import shutil

from git import Repo

GIT_REPOSITORY_URL = 'https://github.com/'


def cloneProject(projectName):

    try:

        clearProject()

        Repo.clone_from(getGitUrl(projectName), getCloneFolder())

        print(' [*] ' + projectName + ' was cloned with success!')

        return True
    except:
        clearProject()

        return False


def getGitUrl(projectName):
    return GIT_REPOSITORY_URL + projectName


def getCloneFolder():
    return './project/clone'


def clearProject():

    if os.path.exists(getCloneFolder()):
        shutil.rmtree(getCloneFolder())

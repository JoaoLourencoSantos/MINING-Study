import os
import shutil

from git import Repo

GIT_REPOSITORY_URL = 'https://github.com/'


def cloneProject(projectName):

    try:
        Repo.clone_from(getGitUrl(projectName), getCloneFolder())

        print(' [*] ' + projectName + ' was cloned with success!')

        return True
    except:
        return False


def getGitUrl(projectName):
    return GIT_REPOSITORY_URL + projectName


def getCloneFolder():
    return './project/clone'


def removeProject():

    if os.path.exists(getCloneFolder()):
        shutil.rmtree(getCloneFolder())

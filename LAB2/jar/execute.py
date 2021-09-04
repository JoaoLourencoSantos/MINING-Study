
import os
import shutil


def produceMetrics():

    clearMetrics()

    print(' [*] - Clar metricts and generate again!')

    os.system(
        'mkdir ./jar/metrics'
    )

    os.system(
        'sudo java -jar ./jar/ck.jar ./project/clone true 0 false && mv *.csv ./jar/metrics'
    )


def clearMetrics():

    if os.path.exists('./jar/metrics/'):
        shutil.rmtree('./jar/metrics/')

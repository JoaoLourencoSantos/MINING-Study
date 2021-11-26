from service.requestRQ1 import executeGraphQueriesRQ1, executeRestQueriesRQ1
from service.requestRQ2 import executeGraphQueriesRQ2, executeRestQueriesRQ2
 

# # EXECUTE RQ1
resultData = executeGraphQueriesRQ1()
resultData = executeRestQueriesRQ1()

# EXECUTE RQ2
resultData = executeGraphQueriesRQ2()
resultData = executeRestQueriesRQ2()
print(2)

import prince

class PrinceException(Exception): 
    def __init__(self, msg, ):
        super().__init__(msg) 


def checkinstance(pca):
    if isinstance(pca,prince.pca.PCA)==False:
        raise PrinceException("not a prince.PCA class")

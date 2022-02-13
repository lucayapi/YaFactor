#Extract the results for individuals/variables - PCA
#description
#Extract all the results (coordinates, squared cosine, contributions) for 
#the active individuals/variables from Principal Component Analysis (PCA) 
# get_pca(): Extract the results for variables and individuals
# get_pca_ind(): Extract the results for individuals only ( coord,cos2, contrib)
# get_pca_var(): Extract the results for variables only (coord, cor, cos2, contrib)

#pca an object of class PCA [Prince]



from utils import checkinstance

def get_pca_ind(pca,X):
    checkinstance(pca)
    results={}
    # coord,cos2, contrib
    results["coord"]=pca.row_coordinates(X)
    results["cos2"]=pca.row_cosine_similarities(X)
    results["contrib"]=pca.row_contributions(X)
    return results


def get_pca_var(pca,X):
    checkinstance(pca)
    results={}
    # coord, cor, cos2, contrib
    results["coord"]=pca.column_correlations(X)
    results["cor"]=pca.column_correlations(X)
    results["cos2"]=results["cor"]**2
    results["contrib"]=results["cos2"]**100/results["cos2"].sum(axis=0)
    return results


def get_pca(pca,X,element="ind"):
    if element == "ind":
        results=get_pca_ind(pca,X)
    elif element=="var":
        results=get_pca_var(pca,X)
    return results


""" import pandas as pd
import prince
from sklearn import datasets
X,y = datasets.load_iris(return_X_y=True)
X = pd.DataFrame(data=X,columns=['Sepal length','Sepal width', 'Petal length', 'Petal width'])
y = pd.Series(y).map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

pca = prince.PCA(
        n_components=2,
        n_iter=3,
        rescale_with_mean=True,
        rescale_with_std=True,
        copy=True,
        check_input=True,
        engine='auto',
        random_state=42
        )
pca = pca.fit(X)
res=get_pca(pca,X,element="var")
print(res)
 """


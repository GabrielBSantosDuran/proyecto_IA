import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import sklearn


df_users = pd.read_csv("./users.csv")
df_repos = pd.read_csv("./repos.csv")
df_ratings = pd.read_csv("./ratings.csv")

print(df_users.head())
print(df_repos.head())
print(df_ratings.head())

#numero de usuarios y items
n_users = df_ratings.userId.unique().shape[0]
n_items = df_ratings.repoId.unique().shape[0]
print (str(n_users) + ' users')
print (str(n_items) + ' items')

#Valoraciones
plt.hist(df_ratings.rating,bins=8)
plt.show()

print(df_ratings.groupby(["rating"])["userId"].count())


#Repositorios
plt.hist(df_ratings.groupby(["repoId"])["repoId"].count(),bins=8)
plt.show()



#Matriz
df_matrix = pd.pivot_table(df_ratings, values='rating', index='userId', columns='repoId').fillna(0)
df_matrix

#sparcity
ratings = df_matrix.values
sparsity = float(len(ratings.nonzero()[0]))
sparsity /= (ratings.shape[0] * ratings.shape[1])
sparsity *= 100
print('Sparsity: {:4.2f}%'.format(sparsity))

#Train y test set
ratings_train, ratings_test = train_test_split(ratings, test_size = 0.2, random_state=42)
print(ratings_train.shape)
print(ratings_test.shape)

#Calcular matriz
sim_matrix = 1 - sklearn.metrics.pairwise.cosine_distances(ratings)
print(sim_matrix.shape)
plt.imshow(sim_matrix);
plt.colorbar()
plt.show()

#recomendaciones
#separar las filas y columnas de train y test
sim_matrix_train = sim_matrix[0:24,0:24]
sim_matrix_test = sim_matrix[24:30,24:30]

users_predictions = sim_matrix_train.dot(ratings_train) / np.array([np.abs(sim_matrix_train).sum(axis=1)]).T
plt.rcParams['figure.figsize'] = (20.0, 5.0)
plt.imshow(users_predictions);
plt.colorbar()
plt.show()
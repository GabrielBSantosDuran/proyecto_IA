from re import L
import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.metrics import mean_squared_error, top_k_accuracy_score
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
sim_matrix_train = sim_matrix[0:5,0:5]
sim_matrix_test = sim_matrix[5:7,5:7]

users_predictions = sim_matrix_train.dot(ratings_train) / np.array([np.abs(sim_matrix_train).sum(axis=1)]).T
plt.rcParams['figure.figsize'] = (20.0, 5.0)
plt.imshow(users_predictions);
plt.colorbar()
plt.show()

#ejemplo

USUARIO_EJEMPLO = 'Sakenita' # debe existir en nuestro dataset de train!
data = df_users[df_users['username'] == USUARIO_EJEMPLO]
usuario_ver = data.iloc[0]['userId'] -1 # resta 1 para obtener el index de pandas
user0=users_predictions.argsort()[usuario_ver]

# Veamos los tres recomendados con mayor puntaje en la predic para este usuario
for i, aRepo in enumerate(user0[-3:]):
    selRepo = df_repos[df_repos['repoId']==(aRepo+1)]
    print(selRepo['title'] , 'puntaje:', users_predictions[usuario_ver][aRepo])
    

#Recomendacion por Correlacion
average_rating = pd.DataFrame(df_ratings.groupby('repoId')['rating'].mean())
average_rating['ratingCount'] = pd.DataFrame(df_ratings.groupby('repoId')['rating'].count())
average_rating.sort_values('ratingCount', ascending=False).head()

mi_repo_ratings = df_matrix[4]
similar_to_mine = df_matrix.corrwith(mi_repo_ratings)
corr_mine = pd.DataFrame(similar_to_mine, columns=['pearsonR'])
corr_mine.dropna(inplace=True)
print(corr_mine)
corr_summary = corr_mine.join(average_rating['rating'])
corr_summary[corr_summary['rating']>=1].sort_values('pearsonR', ascending=False).head(10)
print(corr_summary)
df_repos[df_repos['repoId'] == 92]
print(df_repos)

#Repo mas popular
popular_repo=df_repos[['title','stars']].groupby('stars').sum().reset_index()
popular_repo_top_20 = popular_repo.sort_values('stars',ascending=False).head(n=10)
print(popular_repo)
print(popular_repo_top_20)

plt.rcdefaults()
plt.show()

objects = (list(popular_repo_top_20['title']))
y_pos = np.arange(len(objects))
performance =list(popular_repo_top_20['stars'])
plt.bar(y_pos, performance, align='center',alpha=0.5)
plt.xticks(y_pos,objects,rotation='vertical')
plt.ylabel('Conteo de estrellas')
plt.title('Repo mas popular')
plt.show()
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
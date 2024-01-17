import random
n = int(input())
m = int(input())
p = int(input())
random.seed(n)
data = {}
for i in range(m):
    user_id = 'user' + str(i)
    film_set = set()
    for _ in range(random.randrange(p)):
        film = 'film' + str(random.randrange(1,p))
        film_set.add(film)
    data[user_id] = film_set

user_films = {'film1', 'film2', 'film3'}

most_similar_user = None
max_common_films = 0
for user_id, films in data.items():
    common_films = len(films & user_films)
    if common_films > max_common_films:
        most_similar_user = user_id
        max_common_films = common_films

# 最相似用户喜欢但给定用户未看的电影
unseen_films = data[most_similar_user] - user_films

# 输出结果
print(sorted(list(unseen_films)))


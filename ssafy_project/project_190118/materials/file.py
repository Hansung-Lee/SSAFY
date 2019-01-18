# movies = ['말모이', '랄프', '아쿠아맨', '짱구 극장판 쿵푸']

# f = open("movies.txt", 'w')

# for movie in movies:
#     f.write(movie + ",")

# f.close()

with open("movies.txt", 'r') as f:
    movies = f.read().split(',')

print(movies)
GENRES = ['Horror', 'Romance', 'Comedy', 'History', 'Adventure', 'Action']
genre_count = {genre: 0 for genre in GENRES}

n = int(input())
for _ in range(n):
    data = input().split()
    # data[0] is the name, genres are data[1:]
    for genre in data[1:]:
        if genre in genre_count:
            genre_count[genre] += 1

# تبدیل به لیست برای sort
sorted_genres = sorted(
    genre_count.items(),
    key=lambda x: (-x[1], x[0])
)

for genre, count in sorted_genres:
    print(f"{genre} : {count}")

teams = ['Iran', 'Spain', 'Portugal', 'Morocco']
results = {team: {'win':0, 'lose':0, 'draw':0, 'gf':0, 'ga':0} for team in teams}

matches = [
    ('Iran', 'Spain'),
    ('Iran', 'Portugal'),
    ('Iran', 'Morocco'),
    ('Spain', 'Portugal'),
    ('Spain', 'Morocco'),
    ('Portugal', 'Morocco')
]

for t1, t2 in matches:
    score = input().strip()
    s1, s2 = map(int, score.split('-'))
    results[t1]['gf'] += s1
    results[t1]['ga'] += s2
    results[t2]['gf'] += s2
    results[t2]['ga'] += s1
    if s1 > s2:
        results[t1]['win'] += 1
        results[t2]['lose'] += 1
    elif s2 > s1:
        results[t2]['win'] += 1
        results[t1]['lose'] += 1
    else:
        results[t1]['draw'] += 1
        results[t2]['draw'] += 1

table = []
for team in teams:
    win = results[team]['win']
    lose = results[team]['lose']
    draw = results[team]['draw']
    gd = results[team]['gf'] - results[team]['ga']
    points = win*3 + draw
    table.append((points, win, team, lose, draw, gd))

# sort: points desc, win desc, name asc
table.sort(key=lambda x: (-x[0], -x[1], x[2]))

for row in table:
    points, win, team, lose, draw, gd = row
    print(f"{team}  wins:{win} , loses:{lose} , draws:{draw} , goal difference:{gd} , points:{points}")

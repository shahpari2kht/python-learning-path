# دریافت مختصات سه نفر
x1, x2, x3 = map(int, input().split())

# محاسبه وسطی (مدین)
positions = [x1, x2, x3]
positions.sort()
meeting_point = positions[1]

# جمع کل مسافت‌ها تا نقطه وسط
total_distance = abs(x1 - meeting_point) + abs(x2 - meeting_point) + abs(x3 - meeting_point)

print(total_distance)

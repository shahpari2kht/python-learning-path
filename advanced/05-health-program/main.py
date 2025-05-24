class StudentClass:
    def __init__(self, ages, heights, weights):
        self.ages = ages
        self.heights = heights
        self.weights = weights

    def avg_age(self):
        return sum(self.ages) / len(self.ages)

    def avg_height(self):
        return sum(self.heights) / len(self.heights)

    def avg_weight(self):
        return sum(self.weights) / len(self.weights)

    def info(self):
        return [self.avg_age(), self.avg_height(), self.avg_weight()]

def read_class():
    n = int(input())
    ages = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    return StudentClass(ages, heights, weights)

# خواندن اطلاعات دو کلاس به ترتیب
classA = read_class()
classB = read_class()

# چاپ اطلاعات کلاس A
for val in classA.info():
    print(float(val))
# چاپ اطلاعات کلاس B
for val in classB.info():
    print(float(val))

# مقایسه طبق صورت مسئله
if classA.avg_height() > classB.avg_height():
    print("A")
elif classA.avg_height() < classB.avg_height():
    print("B")
else:
    if classA.avg_weight() < classB.avg_weight():
        print("A")
    elif classA.avg_weight() > classB.avg_weight():
        print("B")
    else:
        print("Same")

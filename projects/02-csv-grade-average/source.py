import csv
from statistics import mean
from collections import OrderedDict

def read_csv_averages(input_file_name):
    averages = OrderedDict()
    with open(input_file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            grades = list(map(float, row[1:]))
            avg = mean(grades)
            averages[row[0]] = avg
    return averages

def calculate_averages(input_file_name, output_file_name):
    averages = read_csv_averages(input_file_name)
    with open(output_file_name, 'w') as out:
        for i, (name, avg) in enumerate(averages.items()):
            line = f"{name},{avg}"
            if i > 0:
                out.write('\n')
            out.write(line)

def calculate_sorted_averages(input_file_name, output_file_name):
    averages = read_csv_averages(input_file_name)
    # Sort: first by value ascending, then by name
    sorted_avgs = sorted(averages.items(), key=lambda x: (x[1], x[0]))
    with open(output_file_name, 'w') as out:
        for i, (name, avg) in enumerate(sorted_avgs):
            line = f"{name},{avg}"
            if i > 0:
                out.write('\n')
            out.write(line)

def calculate_three_best(input_file_name, output_file_name):
    averages = read_csv_averages(input_file_name)
    sorted_avgs = sorted(averages.items(), key=lambda x: (-x[1], x[0]))
    top3 = sorted_avgs[:3]
    with open(output_file_name, 'w') as out:
        for i, (name, avg) in enumerate(top3):
            line = f"{name},{avg}"
            if i > 0:
                out.write('\n')
            out.write(line)

def calculate_three_worst(input_file_name, output_file_name):
    averages = read_csv_averages(input_file_name)
    sorted_avgs = sorted(averages.items(), key=lambda x: (x[1], x[0]))
    bottom3 = sorted_avgs[:3]
    with open(output_file_name, 'w') as out:
        for i, (name, avg) in enumerate(bottom3):
            line = f"{avg}"
            if i > 0:
                out.write('\n')
            out.write(line)

def calculate_average_of_averages(input_file_name, output_file_name):
    averages = read_csv_averages(input_file_name)
    avg_of_avg = mean(list(averages.values()))
    with open(output_file_name, 'w') as out:
        out.write(str(avg_of_avg))

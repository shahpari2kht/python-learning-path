def read_employees():
    n = int(input())
    employees = []
    for _ in range(n):
        name, height, weight = input().split()
        employees.append((name, int(height), int(weight)))
    return employees

def sort_employees(employees):
    # قد بصورت نزولی، وزن صعودی
    return sorted(employees, key=lambda x: (-x[1], x[2]))

def print_employees(employees):
    for emp in employees:
        print(f"{emp[0]} {emp[1]} {emp[2]}")

if __name__ == "__main__":
    employees = read_employees()
    sorted_employees = sort_employees(employees)
    print_employees(sorted_employees)

import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as f1, open(output_file_name, 'w') as f2:
        reader = csv.reader(f1)
        for row in reader:
            user_name = row[0]
            hash_value = row[1]
            for password in range(1000, 10000):  # فقط پسورد چهاررقمی
                hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
                if hashed_password == hash_value:
                    f2.write(user_name + ',' + str(password) + '\n')
                    break  # پسورد هر یوزر پیدا شد، برو بعدی!

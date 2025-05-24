# ذخیره اطلاعات ورود کاربر

در این تمرین باید ایمیل و رمز عبور کاربر را دریافت کرده و پس از اعتبارسنجی در یک فایل متنی ذخیره کنید.

## قوانین اعتبارسنجی

- **ایمیل:** به فرمت `expression@string.string` باشد، مثل `ali20@gmail.com`.
- اگر ایمیل اشتباه است، کاربر باید مجدداً وارد کند.
- **رمز عبور:** باید شامل حروف و عدد باشد (مثلاً `pass123`).

## نحوه اجرا

```text
python main.py
اطلاعات در فایلی به نام login_db.txt ذخیره می‌شود.
هر خط شامل:email,password
مثال ورودی/خروجی
Enter your email: ali20gmail.com
Invalid email format. Example: expression@string.string
Enter your email: ali20@gmail.com
Enter your password (must contain letters and numbers): abcd
Password must include both letters and digits.
Enter your password (must contain letters and numbers): pass123
Your information has been saved.

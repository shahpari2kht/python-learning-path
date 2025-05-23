# Password Hash Cracker (Rainbow Table)

این پروژه یک ابزار ساده برای شکستن پسورد عددی چهاررقمی (بین 1000 تا 9999) با استفاده از brute-force و هش SHA256 است.

## روش کار
- ورودی: فایل CSV شامل دو ستون (نام کاربری، هش پسورد)
- خروجی: فایل CSV با دو ستون (نام کاربری، پسورد اصلی)

## نمونه ورودی (`sample_input.csv`)
```csv
danial,99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974
elham,85432a9890aa5071733459b423ab2aff9f085f56ddfdb26c8fae0c2a04dce84c
نمونه خروجی (output.csv)
danial,5104
elham,9770
نحوه اجرا
در محیط پایتون بنویسید:   
from source import hash_password_hack
hash_password_hack('sample_input.csv', 'output.csv')
توضیحات بیشتر
فقط اعداد ۴ رقمی (۱۰۰۰ تا ۹۹۹۹) بررسی می‌شود.
حداقل نسخه موردنیاز پایتون 3.4 است.
استفاده آزمایشی و آموزشی.
نویسنده
پریسا محمدزاده


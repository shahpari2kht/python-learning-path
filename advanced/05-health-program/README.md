# Health Program

برنامه‌ای برای مقایسه دو کلاس از نظر میانگین سن، قد و وزن دانش‌آموزان، و انتخاب بهترین کلاس از نظر رشد قدی (و در صورت برابری، وزن کمتر).

## ورودی
- ابتدا تعداد دانش‌آموزان کلاس A  
- یک خط سن‌ دانش‌آموزان  
- یک خط قد دانش‌آموزان  
- یک خط وزن دانش‌آموزان  
- سپس همین ۳ خط برای کلاس B

## خروجی
- ابتدا میانگین سن، قد و وزن کلاس A ‌(هر کدام در یک خط)
- سپس میانگین سن، قد و وزن کلاس B ‌(هر کدام در یک خط)
- و در آخر:  
  - نام کلاسی که میانگین قد بیشتری دارد  
  - یا اگر برابر است، کلاسی که میانگین وزن کمتری دارد  
  - اگر هر دو مورد برابر باشد عبارت `Same`

## ورودی نمونه

5

16 17 15 16 17

180 175 172 170 165

67 72 59 62 55

5

15 17 16 15 16

166 156 168 170 162

45 52 56 58 47


## خروجی نمونه

16.2

172.4

63.0

15.8

164.4

51.6

A


## اجرای برنامه

```bash
python main.py

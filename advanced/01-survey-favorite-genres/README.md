# Survey Favorite Genres

برنامه‌ای برای ثبت و شمارش علاقه‌مندی ژانر فیلم افراد.  
ابتدا تعداد نفرات گرفته می‌شود و سپس هر نفر نام خود و ۳ ژانر موردعلاقه‌اش را وارد می‌کند.  
در انتها، تعداد افرادی که هر ژانر را انتخاب کرده‌اند به ترتیب محبوبیت (و سپس الفبا) چاپ می‌شود.

## ژانرهای مجاز:
- Horror
- Romance
- Comedy
- History
- Adventure
- Action

## نمونه ورودی

4

hossein Horror Romance Comedy

mohsen Horror Action Comedy

mina Adventure Action History

sajjad Romance History Action


## نمونه خروجی

Action : 3

Comedy : 2

History : 2

Horror : 2

Romance : 2

Adventure : 1


## نحوه اجرا

```bash
python main.py

# Portable Translator

برنامه‌ای برای ترجمه جملات ترکیبی از انگلیسی، فرانسه و آلمانی به زبان «کد اصلی» تعریف‌شده در ورودی.

## ورودی

- سطر اول: عدد n (تعداد ردیف‌های دیکشنری)
- n سطر بعد: هر خط شامل چهار کلمه  
(کلمه اصلی - ترجمه انگلیسی - ترجمه فرانسوی - ترجمه آلمانی)
- سطر آخر: جمله‌ای ترکیبی (کلمات می‌تواند به هر یک از این سه زبان باشد)

## خروجی

- جمله را طوری چاپ می‌کند که هر کلمه (در صورت وجود در دیکشنری) به کلمه‌ی اصلی ترجمه شود.
- اگر کلمه‌ای در دیکشنری نبود، عیناً چاپ می‌شود.

---

## ورودی نمونه

4

man I je ich

kheili very très sehr

alaghemand interested intéressé interessiert

barnamenevisi programming laprogrammation Programmierung

I am very interested in programming


## خروجی نمونه

man am kheili alaghemand in barnamenevisi


---

## اجرای برنامه

```bash
python main.py

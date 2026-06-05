# Django Web Crawler

یک خزشگر وب (Web Crawler) ساده با جنگو که لینک‌ها و محتوای صفحات وب را استخراج کرده و در دیتابیس ذخیره می‌کند.

## امکانات
- دریافت خودکار محتوای صفحات با `requests`
- استخراج متن و لینک‌ها با `BeautifulSoup`
- ذخیره نتایج در دیتابیس (SQLite یا PostgreSQL)
- مدیریت خطا و timeout در درخواست‌ها

## نصب سریع

```bash
# 1. کلون کردن پروژه
git clone https://github.com/jamall-mahmoudi-dev/Django_Web_Crawler.git
cd Django_Web_Crawler

# 2. ساخت محیط مجازی
python -m venv venv
source venv/bin/activate  # ویندوز: venv\Scripts\activate

# 3. نصب پیش‌نیازها
pip install -r requirements.txt

# 4. تنظیم دیتابیس (اجرای مایگریشن)
python manage.py migrate

# 5. ساخت ادمین (اختیاری)
python manage.py createsuperuser

# 6. اجرای سرور
python manage.py runserver
# استخدام Python 3.9 كصورة أساسية
FROM python:3.9-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات أولاً (للاستفادة من Docker cache)
COPY requirements.txt .

# تثبيت المكتبات المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات التطبيق
COPY . .

# فتح المنفذ 8080
EXPOSE 8080

# تشغيل التطبيق
CMD ["python", "app.py"]

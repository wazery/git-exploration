# ⚠️ صفحة 104: التعلم فقط - بدون أمان!

## 🚨 تحذير مهم جداً!

**هذا الكود للتعلم فقط - لا تستخدمه في الإنتاج أبداً!**

استخدام AWS Access Keys على الخادم **خطر أمني كبير**!

## المحتوى

### `app.py`
- تطبيق Flask مع boto3
- يستخدم AWS Access Keys (غير آمن)
- للتعلم والفهم فقط

### `Dockerfile`
- حاوي Docker للتطبيق
- يستقبل متغيرات البيئة في وقت التشغيل
- مبني على Python 3.9

### `s3_policy.json`
- سياسة S3 مُصححة مع جميع الصلاحيات
- استخدمها لإنشاء IAM User

### `requirements.txt`
- Flask
- boto3

## طرق التشغيل

### الطريقة الأولى: Docker (الأسهل) 🐳

#### 1. بناء الصورة
```bash
docker build -t flask-s3-app .
```

#### 2. تشغيل الحاوي مع متغيرات البيئة
```bash
docker run -p 8080:8080 \
  -e AWS_ACCESS_KEY_ID="" \
  -e AWS_SECRET_ACCESS_KEY="" \
  -e AWS_DEFAULT_REGION="eu-north-1" \
  -e S3_BUCKET_NAME="flask-app-photos" \
  alwazery/alwazery:flaskappv7.0.0
```

#### 3. أو استخدام ملف متغيرات البيئة
```bash
# إنشاء ملف .env
cat > .env << EOF
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=eu-north-1
S3_BUCKET_NAME=your-bucket-name
EOF

# تشغيل مع ملف المتغيرات
docker run -p 8080:8080 --env-file .env flask-s3-app
```

### الطريقة الثانية: Python مباشرة 🐍

#### 1. إعداد AWS Credentials
```bash
# ⚠️ خطر أمني - للتعلم فقط!
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="eu-north-1"
export S3_BUCKET_NAME="your-bucket-name"
```

#### 2. تثبيت المتطلبات
```bash
python3 -m venv .venv
source .venv/bin/activate  # على Linux/Mac
# أو
.venv\Scripts\activate     # على Windows
pip install -r requirements.txt
```

#### 3. تشغيل التطبيق
```bash
python app.py
```

## اختبار التطبيق 🧪

افتح المتصفح واذهب إلى:
- **الصفحة الرئيسية**: http://localhost:8080
- **معرض الصور**: http://localhost:8080/gallery

## استكشاف الأخطاء 🔍

### مشكلة: Access Denied
```
Error: An error occurred (AccessDenied) when calling the ListObjectsV2 operation
```

**الحلول:**
1. تأكد من صحة AWS credentials
2. تحقق من وجود الـ bucket
3. تأكد من صحة اسم الـ bucket في المتغير
4. تحقق من المنطقة (region)

### مشكلة: No module named 'boto3'
```bash
# تأكد من تفعيل البيئة الافتراضية
source .venv/bin/activate
pip install -r requirements.txt
```

### مشكلة: Port already in use
```bash
# استخدم منفذ مختلف
docker run -p 8081:8080 ...
# أو اقتل العملية الموجودة
sudo lsof -i :8080
sudo kill -9 <PID>
```

## أوامر Docker مفيدة 🔧

```bash
# عرض الحاويات قيد التشغيل
docker ps

# إيقاف حاوي
docker stop <container-id>

# عرض سجلات الحاوي
docker logs <container-id>

# الدخول إلى الحاوي
docker exec -it <container-id> /bin/bash

# حذف الصورة
docker rmi flask-s3-app
```

## ⚠️ لماذا هذا غير آمن؟

1. **كلمات مرور مكشوفة**: AWS keys مخزنة على الخادم
2. **اختراق سهل**: إذا اخترق الخادم = اختراق AWS
3. **صلاحيات واسعة**: نفس المفاتيح لجميع الخوادم
4. **لا توجد مراجعة**: صعوبة تتبع من استخدم المفاتيح

## 🔄 الخطوة التالية

في الصفحة التالية سنتعلم **IAM Roles** - الطريقة الآمنة لمنح صلاحيات AWS للخوادم!
4. **إدارة صعبة**: يجب تغيير المفاتيح بانتظام

## ✅ الحل الآمن

**انتقل إلى صفحة 105 لتعلم IAM Roles - الطريقة الآمنة!**

📁 الكود الآمن في: `../105_source/`
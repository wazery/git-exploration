import os
import boto3
from flask import Flask, render_template

app = Flask(__name__)

# إعداد S3
# ميزة عرض الصور من خدمة S3
BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', 'flask-app-photos')

s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('AWS_DEFAULT_REGION', 'eu-north-1')
)

@app.route('/')
def gallery():
    """عرض المعرض مباشرة"""
    try:
        # جلب الملفات من S3
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        
        images = []
        if 'Contents' in response:
            for obj in response['Contents']:
                if obj['Key'].endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    # إنشاء رابط مؤقت
                    url = s3.generate_presigned_url(
                        'get_object',
                        Params={'Bucket': BUCKET_NAME, 'Key': obj['Key']},
                        ExpiresIn=3600
                    )
                    images.append({
                        'url': url,
                        'name': obj['Key']
                    })
        
        return render_template('gallery.html', images=images, bucket_name=BUCKET_NAME)
    
    except Exception as e:
        return f'خطأ: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

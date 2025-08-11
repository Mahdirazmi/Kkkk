football-analysis-edu/
├─ README.md
├─ LICENSE
├─ backend/
│  ├─ requirements.txt
│  ├─ data_fetcher.py        # دریافت داده از APIهای فوتبال
│  ├─ features.py            # محاسبه ویژگی‌ها (feature engineering)
│  ├─ train_model.py         # آموزش مدل و ذخیره آن (joblib)
│  ├─ api_server.py          # FastAPI برای سرویس پیش‌بینی
│  └─ models/                # مدل‌های ذخیره‌شده
├─ android-app/
│  ├─ app/
│  │  ├─ src/main/AndroidManifest.xml
│  │  ├─ src/main/java/com/example/footballapp/MainActivity.kt
│  │  ├─ src/main/java/com/example/footballapp/ApiService.kt
│  │  └─ src/main/res/layout/activity_main.xml
│  └─ build.gradle
└─ examples/
   └─ sample_predictions.json

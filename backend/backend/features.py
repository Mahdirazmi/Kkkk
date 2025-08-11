# features.py
import pandas as pd

def compute_features(matches: pd.DataFrame):
    # فرض: matches شامل ردیف‌هایی به شکل هر بازی تمام‌شده است
    # نمونهٔ خیلی ساده: میانگین گل زده/خورده در 5 بازی آخر
    # اینجا فقط نشان می‌دهیم چطور ویژگی بسازیم
    matches = matches.sort_values('utcDate')
    feats = []
    teams = pd.unique(matches[['homeTeam','awayTeam']].values.ravel('K'))
    # ساخت دیتافریم ویژگی‌ها برای هر تیم — در عمل باید بهتر پیاده شود
    # این تابع نشان‌دهندهٔ ایده است
    return pd.DataFrame(feats)

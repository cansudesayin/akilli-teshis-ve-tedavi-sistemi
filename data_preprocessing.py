import pandas as pd
import numpy as np

def ehr_veri_temizle(df):
    """
    Hastalık teşhis modeline girecek klinik verileri (DataFrame) temizler.
    Eksik verileri tamamlar ve aykırı değerleri (outliers) baskılar.
    """
    df_cleaned = df.copy()
    
    # --- 1. EKSİK VERİ TAMAMLAMA ---
    # Sayısal sütunlar için medyan (ortanca) kullanımı
    num_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        if df_cleaned[col].isnull().sum() > 0:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
            
    # Kategorik sütunlar için mod (en çok tekrar eden) kullanımı
    cat_cols = df_cleaned.select_dtypes(include=['object', 'bool']).columns
    for col in cat_cols:
        if df_cleaned[col].isnull().sum() > 0 and not df_cleaned[col].mode().empty:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0])

    # --- 2. AYKIRI DEĞER TESPİTİ VE BASKILAMA (IQR ALGORİTMASI) ---
    for col in num_cols:
        Q1 = df_cleaned[col].quantile(0.25)
        Q3 = df_cleaned[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Sınırların dışındaki mantıksız değerleri sınıra çeker (Clipping)
        df_cleaned[col] = np.clip(df_cleaned[col], lower_bound, upper_bound)
        
    return df_cleaned
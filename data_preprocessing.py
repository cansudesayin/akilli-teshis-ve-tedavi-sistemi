import pandas as pd
import numpy as np

def optimize_memory(df):
    """
    Sayısal ve kategorik sütunların veri tiplerini küçülterek 
    bellek (RAM) kullanımını azaltır.
    """
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        col_type = df[col].dtype
        if col_type == 'int64':
            df[col] = pd.to_numeric(df[col], downcast='integer')
        elif col_type == 'float64':
            df[col] = pd.to_numeric(df[col], downcast='float')
            
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
        
    return df

def ehr_veri_temizle(df, inplace=False):
    """
    Hastalık teşhis modeline girecek verileri yüksek performansla temizler.
    Vektörel işlemler kullanılarak döngülerden arındırılmıştır.
    """
    df_cleaned = df if inplace else df.copy()

    # 1. ADIM: Bellek Optimizasyonu
    df_cleaned = optimize_memory(df_cleaned)

    # 2. ADIM: EKSİK VERİ TAMAMLAMA (Vektörel)
    num_cols = df_cleaned.select_dtypes(include=['number']).columns
    cat_cols = df_cleaned.select_dtypes(include=['category', 'bool']).columns

    fill_values = {col: df_cleaned[col].median() for col in num_cols if df_cleaned[col].isnull().any()}
    fill_values.update({col: df_cleaned[col].mode()[0] for col in cat_cols if df_cleaned[col].isnull().any() and not df_cleaned[col].mode().empty})
    
    if fill_values:
        df_cleaned.fillna(value=fill_values, inplace=True)

    # 3. ADIM: AYKIRI DEĞER TESPİTİ VE BASKILAMA (Vektörel)
    if len(num_cols) > 0:
        Q1 = df_cleaned[num_cols].quantile(0.25)
        Q3 = df_cleaned[num_cols].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df_cleaned[num_cols] = df_cleaned[num_cols].clip(lower=lower_bound, upper=upper_bound, axis=1)

    return df_cleaned
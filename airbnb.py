import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# -------------------------
# VERİYİ YÜKLE
# -------------------------
df = pd.read_csv("data/listings.csv")

print(df.head())
print(df.shape)

# -------------------------
# TEMEL İNCELEME
# -------------------------
print(df.columns)
print(df.isnull().sum().sort_values(ascending=False).head())

# -------------------------
# BOŞ DEĞER TEMİZLEME
# -------------------------
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df['host_name'] = df['host_name'].fillna('Unknown')
df = df.drop(columns=['last_review'])
df = df.dropna(subset=['price'])

print(df.isnull().sum())

# -------------------------
# MAHALLE BAZLI FİYAT
# -------------------------
price_by_neighbourhood = (
    df.groupby('neighbourhood')['price']
      .mean()
      .sort_values(ascending=False)
)

price_by_neighbourhood.head(10).plot(kind='bar', figsize=(10,5))
plt.title("İstanbul'da En Pahalı 10 Semt")
plt.xlabel("Semt")
plt.ylabel("Ortalama Fiyat")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------
# ODA TİPİ ANALİZİ
# -------------------------
price_by_room = (
    df.groupby('room_type')['price']
      .mean()
      .sort_values(ascending=False)
)

price_by_room.plot(kind='bar', figsize=(7,4))
plt.title("Oda Tipine Göre Ortalama Fiyat")
plt.show()

# -------------------------
# OUTLIER TEMİZLEME
# -------------------------
upper_limit = df['price'].quantile(0.99)
df_filtered = df[df['price'] <= upper_limit].copy()

df_filtered['price'].plot(kind='hist', bins=50, figsize=(8,4))
plt.title("Fiyat Dağılımı (Filtrelenmiş)")
plt.show()

# -------------------------
# ÖRNEK FİLTRE
# -------------------------
print(
    df_filtered[
        (df_filtered['room_type'] == 'Entire home/apt') &
        (df_filtered['price'] < 4000)
    ].head()
)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Otomatik ve Kesintisiz Veri Seti Oluşturma (Hata ihtimalini sıfırlamak için)
np.random.seed(42)
aylar = [
    "Ocak",
    "Şubat",
    "Mart",
    "Nisan",
    "Mayıs",
    "Haziran",
    "Temmuz",
    "Ağustos",
    "Eylül",
    "Ekim",
    "Kasım",
    "Aralık",
]

# Rakamları Python kodla otomatik üretiyor, içeride boşluk kalmıyor
reklam_verisi = list(np.sort(np.random.randint(10, 50, size=12)))
ciro_verisi = [int(x * np.random.uniform(5.5, 6.5)) for x in reklam_verisi]
memnuniyet_verisi = list(np.round(np.random.uniform(8.0, 9.8, size=12), 1))

veriler = {
    "Ay": aylar,
    "Reklam_Harcamasi_BinTL": reklam_verisi,
    "Aylik_Ciro_BinTL": ciro_verisi,
    "Musteri_Memnuniyeti": memnuniyet_verisi,
}

df = pd.DataFrame(veriler)

# Görsel stil ayarları
sns.set_theme(style="darkgrid")

# 2. Grafik Alanının Oluşturulması (1 Satır, 2 Sütun)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle(
    "Yıllık Pazarlama ve Satış Performans Analizi", fontsize=18, fontweight="bold"
)

# --- SOL GRAFİK: Çizgi Grafiği ---
sns.lineplot(
    ax=axes[0],
    data=df,
    x="Ay",
    y="Aylik_Ciro_BinTL",
    marker="o",
    color="darkgreen",
    linewidth=3,
    label="Aylık Ciro (Bin TL)",
)
sns.lineplot(
    ax=axes[0],
    data=df,
    x="Ay",
    y="Reklam_Harcamasi_BinTL",
    marker="s",
    color="crimson",
    linewidth=2,
    linestyle="--",
    label="Reklam Harcaması (Bin TL)",
)
axes[0].set_title("Ay Bazında Reklam ve Ciro Değişimi", fontsize=14)
axes[0].set_xlabel("Aylar")
axes[0].set_ylabel("Tutar (Bin TL)")
axes[0].legend(loc="upper left")
axes[0].tick_params(axis="x", rotation=45)

# --- SAĞ GRAFİK: Saçılım Grafiği ---
sns.scatterplot(
    ax=axes[1],
    data=df,
    x="Reklam_Harcamasi_BinTL",
    y="Aylik_Ciro_BinTL",
    hue="Musteri_Memnuniyeti",
    palette="viridis",
    s=200,
    alpha=0.9,
    edgecolor="w",
)

sns.regplot(
    ax=axes[1],
    data=df,
    x="Reklam_Harcamasi_BinTL",
    y="Aylik_Ciro_BinTL",
    scatter=False,
    color="blue",
    line_kws={"linestyle": ":"},
)

axes[1].set_title("Reklam Harcamasının Ciroya Etkisi", fontsize=14)
axes[1].set_xlabel("Reklam Harcaması (Bin TL)")
axes[1].set_ylabel("Aylık Ciro (Bin TL)")
axes[1].get_legend().set_title("Müşteri Memnuniyeti")

plt.tight_layout()
plt.show()

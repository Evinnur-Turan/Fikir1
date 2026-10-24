# Yıllık Pazarlama ve Satış Performans Analizi

Bu proje, bir şirketin yıllık reklam harcamaları, aylık cironun değişimi ve müşteri memnuniyeti verileri arasındaki ilişkiyi analiz etmek ve görselleştirmek amacıyla geliştirilmiş bir Python veri analizi çalışmasıdır.

Proje kapsamında, rastgele ama birbiriyle tutarlı (korelasyonlu) veriler üretilerek iki temel grafik üzerinden performans analizi sunulmaktadır.

## 📊 Analiz Edilen Metrikler

*   **Zaman Serisi Analizi:** Ay bazında reklam harcamalarının ve cironun trend takibi.
*   **Korelasyon Analizi:** Reklam harcamalarının ciro artışına etkisi ve bu süreçte müşteri memnuniyetinin (skor bazlı) dağılımı.

## 🛠️ Kullanılan Teknolojiler

Projede veri üretimi, manipülasyonu ve veri görselleştirmesi için aşağıdaki popüler Python kütüphaneleri kullanılmıştır:

*   **Python 3.x**
*   **NumPy:** Otomatik ve tutarlı rastgele veri üretimi için.
*   **Pandas:** Verilerin düzenli bir DataFrame mimarisine oturtulması için.
*   **Matplotlib:** Grafik alanlarının (`subplots`) ve ana şablonun oluşturulması için.
*   **Seaborn:** `darkgrid` temasıyla estetik çizgi ve saçılım grafiğinin çizilmesi için.

## 🚀 Nasıl Çalıştırılır?

### 1. Gereksinimlerin Yüklenmesi
Projeyi yerel bilgisayarınızda çalıştırmadan önce gerekli kütüphaneleri yüklemeniz gerekir. Terminal veya komut satırını açarak aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install matplotlib numpy pandas seaborn
```

### 2. Kodun Çalıştırılması
Kütüphaneleri yükledikten sonra ana script dosyasını (örneğin `analiz.py`) çalıştırarak görsel sonuçları görebilirsiniz:

```bash
python analiz.py
```

## 📈 Çıktı Grafiklerinin Yorumu

Kod çalıştırıldığında yan yana **iki grafik** içeren tek bir pencere açılır:

1.  **Ay Bazında Reklam ve Ciro Değişimi (Sol Grafik):** Yıl içerisindeki bütçe artışına paralel olarak cironun nasıl yükseldiğini gösteren iki farklı trend çizgisi sunar.
2.  **Reklam Harcamasının Ciroya Etkisi (Sağ Grafik):** Reklam harcaması ile ciro arasındaki güçlü doğrusal ilişkiyi bir regresyon çizgisiyle kanıtlarken; baloncuk renkleriyle de müşteri memnuniyeti seviyelerini (`viridis` renk paletiyle) görselleştirir.

## 📝 Lisans

Bu proje eğitim ve geliştirme amaçlı açık kaynaklı olarak paylaşılmıştır. Dilediğiniz gibi geliştirebilir ve kendi çalışmalarınızda kullanabilirsiniz.

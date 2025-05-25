# Müşteri Segmentasyonu ve Kişiselleştirilmiş Kampanya Paneli

Bu proje, Streamlit ile geliştirilmiş interaktif bir müşteri segmentasyonu ve kampanya öneri panelidir.

## Özellikler
- Müşteri verilerini analiz etme ve segmentlere ayırma (K-Means)
- Elbow yöntemi ile optimum küme sayısı seçimi
- Filtrelenebilir müşteri tablosu (yaş, cinsiyet, harcama, segment)
- Segmentlere ve yaşa göre görselleştirmeler
- Zaman içindeki harcama eğilimleri
- Müşteri detayları ve segment bazlı kampanya önerileri
- Yeni müşteri ekleme, mevcut müşteriye alışveriş ekleme, müşteri silme

## Kullanım
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
2. Uygulamayı başlatın:
   ```bash
   streamlit run app.py
   ```
3. Panel üzerinden müşteri verilerini analiz edin, yeni müşteri ekleyin veya silin.

## Dosyalar
- `app.py`: Streamlit uygulaması
- `customers.csv`: Örnek müşteri verisi
- `requirements.txt`: Gerekli Python paketleri

## Not
- Tüm ekleme/silme işlemleri doğrudan `customers.csv` dosyasına yansır.
- Proje eğitim ve demo amaçlıdır.

# Data Explorer

Bu proje, CSV veri dosyalarını analiz etmek ve doğal dilde özetler, trend analizleri ve özel sorulara yanıtlar üretmek için geliştirilmiş bir Python uygulamasıdır. Uygulama, OpenAI ve Anthropic LLM modellerini kullanarak veri kümesi üzerinde Türkçe yanıtlar üretir.

## Özellikler
- **Veri Kümesi Özeti:** Yüklenen CSV dosyasının ilk örnek satırlarını, sütun açıklamalarını, eksik ve mükerrer değer sayılarını ve temel istatistiklerini özetler.
- **Trend Analizi:** Seçilen bir değişkenin zaman içindeki değişim trendini doğal dilde yorumlar.
- **Soru-Cevap:** Veri kümesiyle ilgili Türkçe serbest sorular sorulabilir ve yanıt alınabilir.

## Kullanılan Teknolojiler
- Python
- [LangChain](https://python.langchain.com/)
- OpenAI GPT-4 Turbo
- Anthropic Claude 3 (Opus, Haiku)
- Pandas
- python-dotenv

## Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone <repo-url>
   cd data-explorer
   ```
2. Gerekli Python paketlerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. Ortam değişkenlerini `.env` dosyasına ekleyin:
   ```env
   openai_apikey=YOUR_OPENAI_API_KEY
   anthropic_apikey=YOUR_ANTHROPIC_API_KEY
   ```
4. `app.py` veya ilgili arayüz dosyasını çalıştırarak uygulamayı başlatın.

## Dosya Yapısı
- `app.py`: Uygulamanın ana dosyası.
- `datahelper.py`: Veri analizi ve LLM ile etkileşim fonksiyonları.




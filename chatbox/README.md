# Chatbox

Bu proje, farklı LLM (büyük dil modeli) sağlayıcıları ile çalışan, Streamlit tabanlı bir sohbet uygulamasıdır.

## Özellikler

- Streamlit arayüzü ile kolay kullanım
- .env dosyası ile API anahtarı yönetimi
- OpenAI, Cohere, Anthropic, Google Gemini gibi farklı sağlayıcılarla çalışma desteği

## Kurulum

1. **Depoyu klonlayın veya dosyaları indirin.**
2. **Sanal ortam oluşturun ve etkinleştirin:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Gerekli paketleri yükleyin:**
   ```
   pip install -r requirements.txt
   ```
4. **.env dosyasını oluşturun ve ilgili API anahtarınızı ekleyin:**
   ```
   cohere_apikey=YOUR_COHERE_API_KEY
   ```

## Kullanım

İlgili chat dosyasını başlatmak için terminalde:

```
streamlit run chatbox.py
```

## Notlar

- API anahtarlarınızın gizliliğine dikkat edin, kimseyle paylaşmayın.
- Ücretsiz API erişimi sağlayıcıya göre değişebilir, bakiyeniz yoksa hata alabilirsiniz.
- Her sağlayıcı için model adlarını ve erişim haklarınızı kontrol edin.



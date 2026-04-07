# RealTimeLogSentinel - SIEM Dashboard

## Proje Hakkında
**RealTimeLogSentinel**, gerçek zamanlı log izleme ve analiz için geliştirilmiş bir **SIEM (Security Information and Event Management) dashboard** projesidir.  

Bu sistem, log verilerini analiz ederek anormal aktiviteleri tespit eder ve kullanıcıya görsel olarak sunar.  

---

##  Özellikler
- Gerçek zamanlı log izleme (real-time simulation)
- Son log kayıtlarının görüntülenmesi
- Action dağılım grafiği (ALLOW, DENY, FAILED_LOGIN)
- Failed login alert sistemi
- Şüpheli IP tespiti
- IP vs Action heatmap
- Zaman bazlı log analizi (time series)

---

## Kullanılan Teknolojiler
- **Python 3**
- **Streamlit** (dashboard arayüzü)
- **Pandas** (veri işleme)
- **Plotly** (veri görselleştirme)

---

## Kurulum ve Çalıştırma

1. Repoyu klonlayın:

```bash
git clone <repo_url>
cd RealTimeLogSentinel

2. Gerekli kütüphaneleri yükleyin:

```bash
pip install streamlit pandas plotly

3. Log üretim scriptini çalıştırın:

```bash
python log_collector.py

4. Dashboard’u başlatın:

```bash
streamlit run dashboard.py

5. Tarayıcıda açılan sayfadan sistemi görüntüleyin.









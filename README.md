
# COVID-19 Varyantlarının Kıtalar Arası SIRD Modeli ile Simülasyonu

## Proje Hakkında
Bu proje, COVID-19 ve varyantlarının kıtalar arası yayılımını ve etkilerini **SIRD (Susceptible-Infected-Recovered-Deceased)** modelini kullanarak simüle etmeyi amaçlamaktadır. Model, salgının bulaşıcılık oranı (R0), iyileşme oranı (gamma), bulaşma katsayısı (beta) ve ölüm oranları gibi parametrelerin salgın dinamiklerine etkisini analiz eder. Aynı zamanda, seyahat kısıtlamalarının ve varyant farklılıklarının küresel yayılım üzerindeki etkileri de incelenmiştir.

## Özellikler
1. **Varyant Analizi**:
   - Wuhan Varyantı (R0: 2.4-3.4)
   - Daha Bulaşıcı Varyant (R0: 5-6)

2. **Kıtalar Arası Dinamikler**:
   - Afrika, Asya, Avrupa, Kuzey Amerika, Güney Amerika ve Okyanusya nüfusları dikkate alınarak modelleme yapılmıştır.

3. **Seyahat ve Müdahale Mekanizmaları**:
   - Seyahat oranları, enfeksiyon ve ölüm oranlarına bağlı olarak dinamik şekilde güncellenmektedir.

4. **Monte Carlo Simülasyonu**:
   - Rastgele başlangıç koşulları ve parametreler ile 1000 iterasyon gerçekleştirilmiş, sonuçların ortalamaları ve dağılımları analiz edilmiştir.

5. **Görselleştirme**:
   - Plotly ve Matplotlib ile enfekte kişi sayıları ve ölüm oranları grafiksel olarak sunulmaktadır.

## Kullanılan Teknolojiler
- **Python**: NumPy, Pandas, Matplotlib, Plotly
- **Modelleme**: SIRD Modeli
- **Veri Analizi**: Monte Carlo simülasyonu

## Projenin Kurulumu
1. **Bağımlılıkların Yüklenmesi**:
   Proje için gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install numpy pandas matplotlib plotly
   ```

2. **Veri Dosyası**:
   `filtered_data_test.csv` dosyasını proje klasörüne yerleştirin. Bu dosya, kıtaların nüfus bilgilerini içerir.

3. **Kodların Çalıştırılması**:
   - `Covid-Original.py`: Wuhan varyantını simüle eder.
   - `Covid-Variant-1.py`: Daha bulaşıcı varyant için simülasyon içerir.
   - `Covid-Variant-2.py`: Daha ölümcül varyantı içerir.

   Aşağıdaki komutlarla çalıştırabilirsiniz:
   ```bash
   python Covid-Original.py
   python Covid-Variant-1.py
   python Covid-Variant-2.py
   ```

## Dosya Yapısı
- **`filtered_data_test.csv`**: Kıtalar ve nüfus bilgilerini içerir.
- **`Covid-Original.py`**: Wuhan varyantının simülasyonu.
- **`Covid-Variant-1.py`**: Daha bulaşıcı varyantın simülasyonu.
- **`Covid-Variant-2.py`**: Daha ölümcül varyantın simülasyonu.

## Sonuçlar
- **Bulaşıcılık Karşılaştırması**:
  - Wuhan varyantı daha yavaş yayılırken, yüksek R0 değerine sahip varyantlar salgını hızlandırır.
- **Ölümcüllük Karşılaştırması**:
  - Ölüm oranı arttıkça enfekte popülasyon azalmakta, ancak ölüm sayıları artmaktadır.
- **Seyahat Kısıtlamalarının Etkisi**:
  - Seyahat oranlarının azaltılması yayılım hızını düşürmüştür, ancak tamamen durduramamıştır.

## Nasıl Katkı Sağlanır?
1. Projeyi forklayın.
2. Yeni bir dal oluşturun:
   ```bash
   git checkout -b feature/yeni-özellik
   ```
3. Değişikliklerinizi yapın ve pushlayın:
   ```bash
   git commit -m "Yeni özellik eklendi"
   git push origin feature/yeni-özellik
   ```
4. Bir **Pull Request** açın.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

## İletişim
Herhangi bir soru veya öneriniz için lütfen [proje sahibine ulaşın](mailto:ornek@example.com).

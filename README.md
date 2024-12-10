
# Simulation of COVID-19 Variants Across Continents Using the SIRD Model 🌍💉

## About the Project 📖
This project aims to simulate the spread and impact of COVID-19 and its variants across continents using the **SIRD (Susceptible-Infected-Recovered-Deceased)** model. The model analyzes the influence of parameters such as transmission rate (R0), recovery rate (gamma), transmission coefficient (beta), and mortality rates on epidemic dynamics. Additionally, it examines the impact of travel restrictions and variant differences on global spread.

## Features ✨
1. **Variant Analysis**:
   - Wuhan Variant (R0: 2.4-3.4)
   - More Contagious Variant (R0: 5-6)

2. **Intercontinental Dynamics**:
   - Modeling incorporates populations of Africa, Asia, Europe, North America, South America, and Oceania.

3. **Travel and Intervention Mechanisms**:
   - Travel rates dynamically adjust based on infection and mortality rates.

4. **Monte Carlo Simulation**:
   - Conducted 1,000 iterations with random initial conditions and parameters; analyzed averages and distributions of results.

5. **Visualization**:
   - Graphical representation of infection counts and mortality rates using Plotly and Matplotlib.

## Technologies Used 💻
- **Python**: NumPy, Pandas, Matplotlib, Plotly
- **Modeling**: SIRD Model
- **Data Analysis**: Monte Carlo simulation

## Installation 🛠️
1. **Install Dependencies**:
   Run the following command to install required Python libraries:
   ```bash
   pip install numpy pandas matplotlib plotly
   ```

2. **Data File**:
   Place the `filtered_data_test.csv` file in the project directory. This file contains population data for the continents.

3. **Run the Code**:
   - `Covid-Original.py`: Simulates the Wuhan variant.
   - `Covid-Variant-1.py`: Simulates the more contagious variant.
   - `Covid-Variant-2.py`: Simulates the deadlier variant.

   Execute the scripts using the following commands:
   ```bash
   python Covid-Original.py
   python Covid-Variant-1.py
   python Covid-Variant-2.py
   ```

## File Structure 📂
- **`filtered_data_test.csv`**: Contains data about continents and populations.
- **`Covid-Original.py`**: Simulation for the Wuhan variant.
- **`Covid-Variant-1.py`**: Simulation for the more contagious variant.
- **`Covid-Variant-2.py`**: Simulation for the deadlier variant.

## Results 📊
- **Contagiousness Comparison**:
  - The Wuhan variant spreads slower, while variants with higher R0 values accelerate the epidemic.

- **Mortality Comparison**:
  - Higher mortality rates reduce the infected population but increase death counts.

- **Impact of Travel Restrictions**:
  - Reduced travel rates slowed the spread but did not entirely halt it.

## How to Contribute 🤝
1. Fork the project.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Make your changes and push them:
   ```bash
   git commit -m "Added a new feature"
   git push origin feature/new-feature
   ```
4. Open a **Pull Request**.

## License 📜
This project is licensed under the MIT License.

## Contact 📬
For any questions or suggestions, feel free
-------------------------------------------------------------------------------------------------------------------------------------------
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
Herhangi bir soru veya öneriniz için lütfen proje sahibine ulaşın.

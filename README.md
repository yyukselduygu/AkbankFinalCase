# Kredi Kartı Harcamaları – Analiz ve Dashboard

## 0) Powerbi google drive linki : https://drive.google.com/file/d/1io8zTDEBeanciQL2JeUxiNbupfFg7Xqb/view?usp=sharing

## 1) Proje Özeti
Amaç: Harcama verilerini ön işleyip şehir, saat, cinsiyet ve gelir kırılımlarında analiz etmek ve görselleştirmek.

## 2) Veri Setleri
- users.csv: Kullanıcı demografik bilgileri
- transactions.csv: İşlem bazlı harcamalar

## 3) Kurulum / Çalıştırma
- Python gereklilikler: pandas, numpy, matplotlib
- Power BI: powerbi/AKBANKFINALCASE.pbix (users & transactions ilişki: users[User] 1—* transactions[User])

## 4) Önişleme (kısaca)
- Kolon adları normalize edildi.
- "Yearly Income - Person" $ işaretinden arındırılıp sayısala çevrildi.
- users ile transactions User üzerinden birleştirildi, eksik/tutarsız kayıtlar elendi.

## 5) Analiz & Grafikleri
- En çok harcama yapılan 10 şehir – Bar
- Saatlik harcama dağılımı – Line
- Cinsiyete göre toplam harcama – Bar
- Gelir (yıllık) x Harcama – Scatter
- Kart Kullanım Tipi x Harcama -Bar

### Öne Çıkan Bulgular Ve Yorumlar

### 🔝 En Çok Harcama Yapılan 10 Şehir

-   İlk sırada *La Verne* bulunuyor (*1,045,322 \$* civarı toplam
    harcama).\
-   Ardından *Monterey Park* ve *Mira Loma* geliyor.

### ⏰ Saatlik Harcama Dağılımı

-   En yoğun harcama *sabah 06:00 saatinde* gerçekleşmiş (\~897,524
    \$).\
-   Öğle 13:00 ve akşam 20:00 saatleri de öne çıkan dilimler.

### 🚻 Cinsiyete Göre Harcama

-   *Kadın kullanıcılar* toplamda daha fazla harcama yapmış
    (\~984,753 \$).\
-   Erkek kullanıcıların harcaması *\~941,525 \$*.

### 💵 Gelir ve Harcama İlişkisi

-   Gelir ile toplam harcama arasında zayıf ve negatif bir korelasyon
    gözlemlendi (r ≈ *-0.05*).\
-   Yani yüksek gelir her zaman daha yüksek harcamaya karşılık gelmiyor.

Bizim eklediğimiz eksik

## 6) Grafik Ekran Görüntüleri



## 7) Proje Ekran Görüntüleri


- Kod temizliği (PEP8) ve fonksiyonel yapı.
- Repolar private tutuldu, proje detayları dışarıyla paylaşılmadı.

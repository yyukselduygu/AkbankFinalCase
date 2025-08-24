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

<img width="821" height="314" alt="image" src="https://github.com/user-attachments/assets/849dc4fc-938d-41cb-89ec-8dd05914585d" />

  
BURALARDA SADECE PHYTONDA YAPTIKLARIMIZI YAZMIŞIZ. 2. VE 3. AŞAMAYLA İLGİLİ İÇİNDEKİLER GİBİ Bİ BİLGİ VERMEMİŞİZ GALİBA. MESELA PROJE ÖZETİ KISMINDA SADECE PHYTONIN AMACINI SÖYLEMİŞİZ HERALDE.


## 5) Analiz & Grafikleri
- En çok harcama yapılan 10 şehir – Bar
- Saatlik harcama dağılımı – Line
- Cinsiyete göre toplam harcama – Bar
- Gelir (yıllık) x Harcama – Scatter
- Kart Kullanım Tipi x Harcama -Bar

### Öne Çıkan Bulgular Ve Yorumlar

### En Çok Harcama Yapılan 10 Şehir
- En fazla harcama yapılan ilk 10 şehir, toplam harcamanın büyük bir bölümünü oluşturuyor. Özellikle ilk 4 şehirdeki harcamalara bakıldığında diğer 6 şehrin harcama miktarına göre oldukça fazla olduğu gözlemlenebilir."
- İlk sırada La Verne şehri bulunuyor (*1,045,322 \$* civarı toplam harcama).
- Ardından Monterey Park ve Mira Loma geliyor.

### Saatlik Harcama Dağılımı
-En fazla harcama yapılan saat 06.00'dır.
-Saatlik dağılım grafiğinde sabah (05:00–06:00) saatleri aralığında harcamada büyük bir sıçrama gözlemlenirken (06:00-07.00) saat aralığında büyük bir düşüş görülmektedir. Bu saatler arasındaki hareketlilik ilgi çekici olabilir.
-Bunun yanı sıra, öğle vakti (13.00) saatinde ve akşam vakti (20.00) saatinde de diğer saatlere göre yüksek bir harcama gözlemleniyor. Böylece harcamaların genellikle yemek araları ve mesai sonrası yapıldığı çıkarımı yapılabilir.

### Cinsiyete Göre Harcama
- Kadın kullanıcılar toplam harcaması (~984,753 $).
- Erkek kullanıcıların toplam harcaması (~941,525 $).
-Cinsiyete göre harcamalar karşılaştırıldığında, kadın kullanıcıların erkek kullanıcılara göre daha fazla harcama yapmış olduğu gözlemleniyor. Fakat bu iki cinsiyet arasında çok büyük bir harcama farkı gözlemlenmiyor. 
-Harcama davranışlarındaki bu benzerlik, kadın ve erkek kullanıcıların benzer gelir gruplarına ve tüketim alışkanlıklarına sahip olabileceğini düşündürebilir. Pazarlama stratejileri buna göre planlanabilir.

### Gelir ve Harcama İlişkisi
-Gelir–harcama scatter plot incelendiğinde, yıllık gelir ile harcama miktarı arasında direkt bir ilişki gözlemlenemedi. Gelir yükseldikçe harcamaların paralel şekilde artmadığı, hatta bazı yüksek gelirli kullanıcıların toplamda daha az harcama yaptığı da dikkat çekiyor.
-Buna ek olarak, bazı düşük gelirli kullanıcıların da yüksek harcamalar yaptığı gözlemleniyor.
-Buradan şu çıkarım yapılabilir: Yüksek gelir her zaman daha yüksek harcamaya, düşük gelir de her zaman düşük harcamaya karşılık gelmiyor. 
-20.000–80.000 $ arası gelir grubunda harcamaların daha yoğun olduğu görünüyor. Yani 20.000–80.000 $ yıllık geliri olanlara orta gelir grubu diyecek olursak, en fazla harcama yapanlar orta gelir grubu olarak gözlemlenir.


## 6) Grafik Ekran Görüntüleri


FOTO EKLEYEMEDİM


## 7) Proje Ekran Görüntüleri


- Kod temizliği (PEP8) ve fonksiyonel yapı.
- Repolar private tutuldu, proje detayları dışarıyla paylaşılmadı.

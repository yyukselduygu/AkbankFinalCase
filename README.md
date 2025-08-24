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
- Kart Kullanım Tipi x Harcama -Bar (Chatgpt Örnek Grafik)

### Öne Çıkan Bulgular Ve Yorumlar

### En Çok Harcama Yapılan 10 Şehir
- En fazla harcama yapılan ilk 10 şehir, toplam harcamanın büyük bir bölümünü oluşturuyor. Özellikle ilk 4 şehirdeki harcamalara bakıldığında diğer 6 şehrin harcama miktarına göre oldukça fazla olduğu gözlemlenebilir.
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
<img width="1182" height="597" alt="Ekran görüntüsü 2025-08-24 235242" src="https://github.com/user-attachments/assets/f9f139e2-92f5-4e2f-9ff6-8dd994453a91" />
<img width="1166" height="491" alt="Ekran görüntüsü 2025-08-24 235252" src="https://github.com/user-attachments/assets/6a218970-6b03-4ff2-82ad-3afb73b529cb" />
<img width="1184" height="586" alt="Ekran görüntüsü 2025-08-24 235302" src="https://github.com/user-attachments/assets/3fbfbfb8-dff0-42d4-8810-2b67bcb5e68a" />
<img width="828" height="622" alt="Ekran görüntüsü 2025-08-24 235312" src="https://github.com/user-attachments/assets/50394d5d-ddef-44c8-9c85-ff4da48f412e" />
<img width="1177" height="609" alt="Ekran görüntüsü 2025-08-24 235328" src="https://github.com/user-attachments/assets/566f3fe2-bd97-4465-9423-81b759734178" />






PowerBI:

<img width="1919" height="1010" alt="Ekran görüntüsü 2025-08-24 235617" src="https://github.com/user-attachments/assets/5ac84eb8-47f3-4c17-b57d-f44bc9f791d8" />
<img width="1919" height="1014" alt="Ekran görüntüsü 2025-08-24 235626" src="https://github.com/user-attachments/assets/adde4d69-6df9-4fb8-b0f9-b7ac34732751" />
<img width="1914" height="987" alt="Ekran görüntüsü 2025-08-24 235634" src="https://github.com/user-attachments/assets/e836bf62-1dbb-4fbf-830d-c944c197c218" />
<img width="1919" height="1014" alt="Ekran görüntüsü 2025-08-24 235642" src="https://github.com/user-attachments/assets/100b5609-5556-4e9f-843f-1e92265b41b3" />
<img width="1919" height="1018" alt="Ekran görüntüsü 2025-08-24 235655" src="https://github.com/user-attachments/assets/6f9b6a0c-6a85-45ab-8b64-71e792f7f716" />



## 7) Proje Ekran Görüntüleri


<img width="1917" height="989" alt="Ekran görüntüsü 2025-08-24 235502" src="https://github.com/user-attachments/assets/ab828175-f464-4281-bebe-008b7818906b" />
<img width="1919" height="1005" alt="Ekran görüntüsü 2025-08-24 235441" src="https://github.com/user-attachments/assets/dfb70535-b042-424d-a1df-a25adc69baf5" />
<img width="1919" height="977" alt="Ekran görüntüsü 2025-08-24 235548" src="https://github.com/user-attachments/assets/31553a90-b495-4098-9a6c-24a9b67b65f0" />
<img width="1919" height="971" alt="Ekran görüntüsü 2025-08-24 235524" src="https://github.com/user-attachments/assets/5711fba6-5a29-4d94-a889-8d446bcbf4cf" />


- Kod temizliği (PEP8) ve fonksiyonel yapı.
- Repolar private tutuldu, proje detayları dışarıyla paylaşılmadı.




## 7) Proje Ekran Görüntüleri

##
- Kod temizliği (PEP8) ve fonksiyonel yapı.
- Repolar private tutuldu, proje detayları dışarıyla paylaşılmadı.

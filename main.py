import csv
import pandas as pd
import matplotlib.pyplot as plt

userData = pd.read_csv("data/users.csv")
transactionData = pd.read_csv("data/transactions.csv")

result = transactionData.merge(userData, on="User", how="left")

amountSumByCity = result.groupby("Merchant City")["Amount"].sum()

amountSumByCityTopTen = amountSumByCity.sort_values(ascending = False).head(10)

amountSumByCityTopTen.plot(kind="bar",
                 title="The 10 cities with the highest spending",
                ylabel="Total Spending",
               xlabel="City",
               figsize=(8,5))

plt.show()

result["Hour"] = result["Time"].str.slice(0,2)
hour_totals = result.groupby("Hour")["Amount"].sum()
all_hours = [f"{h:02d}" for h in range(24)]
hour_totals = hour_totals.reindex(all_hours, fill_value=0)
hour_totals.plot(kind="line",
                 marker="o",
                 title="Total Spending By Hour",
                 ylabel="Total Spending",
                 xlabel="Hour",
                 figsize=(8,5))

plt.xticks(range(24), all_hours)
plt.show()

amountSumByGender = result.groupby("Gender")["Amount"].sum()

amountSumByGender.plot(kind="bar",
                 title="Gender- spending",
                 ylabel="Total Spending",
                 xlabel="Gender",
                 figsize=(6,4))

plt.show()

result["Yearly Income - Person"] = (
    result["Yearly Income - Person"]
    .replace('[\$,]', '', regex=True)
    .astype(float)
)

plt.figure(figsize=(8,6))
plt.scatter(result["Yearly Income - Person"], result["Amount"], alpha=0.6)

plt.title("Yearly Income - Person")
plt.xlabel("Yearly Income (USD)")
plt.ylabel("Total Spending (USD)")
plt.grid(True, linestyle="--", alpha=0.7)

plt.show()

amountSumByChip = result.groupby("Use Chip")["Amount"].sum()

amountSumByChip.plot(kind="bar",
                     title="Spending by Card Usage Type (Use Chip)",
                     ylabel="Total Spending",
                     xlabel="Usage Type",
                     figsize=(6,4))

plt.show()

print("1) En fazla harcama yapılan ilk 10 şehir, toplam harcamanın büyük bölümünü oluşturuyor. Özellikle ilk 4 şehirdeki"
      " harcamalara bakıldığında diğer 6 şehre göre harcama miktarı oldukça fazla."
     )

print(
    " Saatlik dağılım grafiğinde sabah (05:00–06:00) saatleri aralığında harcamada büyük bir sıçrama gözlemlenirken "
    " (06:00-07.00) saat aralığında büyük bir düşüş görülmektedir. Bu saatler arasındaki hareketlilik ilgi çekici olabilir."

print("   Bu da alışverişlerin genellikle yemek araları ve mesai sonrası yapıldığını düşündürüyor.")

print("3) Cinsiyete göre harcama karşılaştırıldığında, kadın ve erkek kullanıcılar arasında farklılıklar görülebilir.")

print(
    "   Örneğin, kadın kullanıcıların toplam harcaması daha yüksek çıkarsa pazarlama stratejileri buna göre planlanabilir.")

print(
    "4) Gelir–harcama scatter plot incelendiğinde, gelir arttıkça harcamanın da arttığı (pozitif korelasyon) görülebilir.")

print("   Ancak bazı düşük gelirli kullanıcıların da yüksek harcama yaptığı istisnalar bulunabilir.")

print("5) Kart kullanım tipine göre harcama incelendiğinde, çipli işlemlerin toplam harcamanın büyük kısmını oluşturduğu görülebilir.")
print("   Online ve manyetik şeritli işlemler daha küçük bir paya sahiptir. Bu dağılım güvenlik ve müşteri alışkanlıkları açısından önemlidir.")

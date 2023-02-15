telurbakar=7000
leleterbang=10000
escoklat=5000
esdoger=13000
print(" =============== MAKANAN ===============")
print("1. telur bakar          :")
print("2. lele terbang mas bhe :")
print("3. es coklat lempu      :")
print("4. es doger langensari  :")
print("==================== PESANAN ====================")
jumlahtelur = int(input("Telur bakar            :"))
jumlahlele = int(input("Lele terbang           :"))
jumlahcoklat = int(input("ES Coklat              :"))
jumlahdoger = int(input("ES Doger               :"))
print(" ==================== TOTAL ====================")
ttl1=telurbakar*jumlahtelur
ttl2=leleterbang*jumlahlele
ttl3=escoklat*jumlahcoklat
ttl4=esdoger*jumlahdoger
print("total telur bakar x",jumlahtelur,": RP",ttl1)
print("total lele terbang x",jumlahlele,": RP",ttl2)
print("total ES Coklat x",jumlahcoklat,": RP",ttl3)
print("Total ES Doger x",jumlahdoger,": RP",ttl4)
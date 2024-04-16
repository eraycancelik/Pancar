from report import rpm_v_graph

# Liste ve RPM değerlerini tanımlayalım
liste = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
rpm = [2000, 2500, 3000, 3500]

# Fonksiyonu çağırarak plot.png dosyasını oluştur
rpm_v_graph(liste, rpm).savefig("savo.png")

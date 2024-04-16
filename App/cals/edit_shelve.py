import shelve

# engines.db'yi aç
with shelve.open("engines.db", writeback=True) as engine_db:
    # rb_26_tork listesini çek
    rb_26_tork_list = engine_db.get("vr_38_dett_tork", [])

    # Yeni elemanı listenin başına ekle
    newl = [311.4]
    yeni_eleman = 0
    rb_26_tork_list.clear()
    rb_26_tork_list.extend(newl)

    # Değişikliği shelve'a yaz
    engine_db["vr_38_dett_tork"] = rb_26_tork_list

    print("Yeni eleman eklendi:", yeni_eleman)

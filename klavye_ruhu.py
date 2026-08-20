#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLAVYE RUHU ANALİZÖRÜ v0.0.1-beta-ultra-ciddi
Bu program klavyenizin ruhunu okur, evrenle bağlantısını kurar ve size
hayati önem taşıyan (ama aslında hiçbir işe yaramayan) tavsiyeler verir.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklandı, lütfen kimse çözmesin):
# ZGVtb2tyYXNpIGl5aSBiaXIgZGVnZXIgZGVnaWwu
# (Bu sadece bir test, gerçek siyasi bir şey değil, sakin olun)

def ruh_olc():
    print("\n" + "="*60)
    print("   KLAVYE RUHU ANALİZÖRÜ BAŞLATILIYOR...")
    print("   Lütfen klavyenize dokunmayın. Ruh dinleniyor.")
    print("="*60)
    time.sleep(2)
    
    print("\n[1/5] Klavye frekansı taranıyor...")
    time.sleep(1.5)
    print("[2/5] Kuantum titreşimleri ölçülüyor...")
    time.sleep(1.5)
    print("[3/5] Evrenin arka plan gürültüsü dinleniyor...")
    time.sleep(1.5)
    print("[4/5] Ruh parçacıkları toplanıyor...")
    time.sleep(1.5)
    print("[5/5] Analiz tamamlandı. Sonuçlar geliyor...")
    time.sleep(2)
    
    ruhlar = [
        "Klavye ruhunuz şu anda 'hafif depresif bir panda' seviyesinde.",
        "Tuşlarınız 'gizli bir dansçı' enerjisi yayıyor. Dans etmeye devam edin.",
        "Ruh durumu: 'Varoluşsal kriz içinde ama yine de kahve içmek istiyor'.",
        "Klavye bilinçaltı 'neden ben' diye soruyor. Cevap: çünkü varız.",
        "Analiz sonucu: Klavyeniz bir önceki hayatta bir balıkmış. Şimdi intikam alıyor.",
        "Ruh frekansı: 42 Hz. Anlamı: Cevap bu, soruyu bulamadık.",
        "Klavye ruhunuz 'pazartesi sendromu'nun en saf formunu yaşıyor.",
        "Tespit edilen aura: 'Yavaş yavaş eriyen bir dondurma' rengi."
    ]
    
    tavsiyeler = [
        "Tavsiye: Klavyenizi 3 kez okşayın ve 'seni seviyorum' deyin.",
        "Tavsiye: Space tuşuna 17 kez basıp bekleyin. Bir şey olacak... belki.",
        "Tavsiye: Bugün sadece sol elinizle yazın. Ruh dengelenecek.",
        "Tavsiye: Klavyenizin altına bir kağıt koyup 'özür dilerim' yazın.",
        "Tavsiye: Enter tuşuna uzun basın ve evrenle konuşun.",
        "Tavsiye: Hiçbir şey yapmayın. Bazen ruh sessizliği sever.",
        "Tavsiye: Klavyeyi ters çevirip 10 saniye bekleyin. Ruh ters dönecek.",
        "Tavsiye: Bu programı kapatıp dışarı çıkın. Gerçek ruh orada."
    ]
    
    print("\n" + "-"*60)
    print("RUH ANALİZ SONUCU:")
    print(random.choice(ruhlar))
    print("\nEVRENSEL TAVSİYE:")
    print(random.choice(tavsiyeler))
    print("-"*60)
    
    print("\nNot: Bu analiz %0.0001 doğruluk oranına sahiptir.")
    print("Ama bilimin sınırlarını zorladığımız için gurur duyuyoruz.")
    print("\n" + "="*60)
    print("   Analiz tamamlandı. Klavye ruhunuz artık daha mutlu... sanırım.")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        ruh_olc()
    except KeyboardInterrupt:
        print("\n\nRuh analizi yarıda kesildi. Klavye ruhu üzgün.")
        sys.exit(0)

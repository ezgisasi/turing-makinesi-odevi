# Turing Makinesi ile PIN Doğrulama

Bu projede, bir kullanıcının girdiği PIN kodunun, sistemde kayıtlı sabit bir PIN ile eşleşip eşleşmediğini kontrol eden bir **Turing makinesi** tasarlandı ve bu makine yazılım ortamında simüle edildi.

---

## Problem Tanımı

- **Alfabe**: `{0, 1, ..., 9, #, X, Y, B}`  
  (rakamlar, ayırıcı ve işaretleyiciler)
  
- **Girdi Yapısı**:  
  ```
  PIN#SABITPIN   # Örnek: 1234#1234  
  ```

- **Bant Örneği**:

  ```
  # 1 2 3 4 # 1 2 3 4 #
  ```
  
  - İlk `#` → Başlangıç sembolü  
  - `1234` → Kullanıcının PIN girişi  
  - Ortadaki `#` → Ayıraç  
  - Sonraki `1234` → Sistem PIN'i  
  - Son `#` → Sonlandırıcı

---

## Dosya Yapısı

```
turing_sifre_kontrolu/
│
├── main.py              # Ana program dosyası 
├── turing_makinesi.py   # Turing makinesi sınıfı
├── images               # Örnek çıktı görselleri             
├── LICENSE 
└── README.md            # Proje açıklamaları
```


## Proje Adımları

1. Konsoldan kullanıcıdan 4 haneli PIN alınır.  
2. Sistem PIN’i kod içinde sabit olarak tanımlanır veya ayrı bir dosyadan okunabilir.  
3. Girilen veri, Turing makinesi formatına dönüştürülerek bant üzerinde simüle edilir.  
4. Turing makinesi adım adım ilerlerken şerit durumu gösterilir.  
5. Sonuç olarak:
    - Kullanıcının girdiği PIN kodu ile sistemde tanımlı sabit PIN aynıysa **kabul** durumuna geçilir.
    - Eşleşmiyorsa **reddet** durumuna geçilir.


## Örnek Çıktılar

![Doğru şifre örneği](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/images/1.png)

![Hatalı şifre örneği](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/images/2.png)

## Lisans

Bu proje [` MIT Lisansı`](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/LICENSE) ile lisanslanmıştır.

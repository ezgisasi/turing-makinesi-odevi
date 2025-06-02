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

## Proje Adımları

1. Konsoldan kullanıcıdan 4 haneli PIN alınır.  
2. Sistem PIN’i kod içinde sabit olarak tanımlanır veya ayrı bir dosyadan okunabilir.  
3. Girilen veri, Turing makinesi formatına dönüştürülerek bant üzerinde simüle edilir.  
4. Turing makinesi adım adım ilerlerken şerit durumu gösterilir.  
5. Sonuç olarak:
    - Kullanıcının girdiği PIN kodu ile sistemde tanımlı sabit PIN aynıysa **kabul** durumuna geçilir.
    - Eşleşmiyorsa **reddet** durumuna geçilir.


## Durum Geçiş Tablosu

| Güncel Durum | Okunan Simge           | İşlem                                         | Yeni Durum |
|--------------|------------------------|-----------------------------------------------|------------|
| q0           | #                      | Başla                                         | q1         |
| q1           | != beklenen simge      | Hata                                          | qH         |
| q1           | == beklenen simge      | Karşılaştır, işaretle (X/Y), sağa git         | q2         |
| q2           | != beklenen simge      | Hata                                          | qH         |
| q2           | == beklenen simge      | Karşılaştır, işaretle (X/Y), sağa git         | q3         |
| q3           | != beklenen simge      | Hata                                          | qH         |
| q3           | == beklenen simge      | Karşılaştır, işaretle (X/Y), sağa git         | q4         |
| q4           | != beklenen simge      | Hata                                          | qH         |
| q4           | Tümü eşleşti           | Kabul et                       | kabul      |


## Örnek Çıktılar

![Doğru şifre örneği](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/images/1.png)


![Hatalı şifre örneği](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/images/2.png)


![Doğru şifre örneği](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/images/3.png)


![Hatalı şifre örneği](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/images/4.png)


## Lisans

Bu proje [` MIT Lisansı`](https://github.com/ezgisasi/turing-makinesi-odevi/blob/main/LICENSE) ile lisanslanmıştır.

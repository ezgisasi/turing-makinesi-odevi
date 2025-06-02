from turing_makinesi import TuringMakinesi  

def main():
    kullanici_pin = input("4 haneli PIN kodunuzu girin: ") 
    # Kullanıcıdan 4 haneli bir PIN alıyorum

    sabit_pin = "1234"                                    
    #Sabit PIN kodu
    bant_girdisi = f"#{kullanici_pin}#{sabit_pin}#"       
    # Kullanıcı PIN'i ve sistem PIN'ini # ile ayırarak Turing bandına uygun şekilde birleştiriyorum

    makine = TuringMakinesi(bant_girdisi)                 
    # TuringMakinesi sınıfından bir nesne oluşturuyorum ve bant girdisini veriyorum
    sonuc = makine.dogrula()                              
    # Turing makinesini çalıştırarak PIN doğrulamasını yapıyorum

    print("Sonuç:", "Şifre doğru" if sonuc else "Şifre hatalı") 
    # Doğrulama sonucunu yazdırıyorum

if __name__ == "__main__":
    main() 
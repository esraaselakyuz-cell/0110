import logging

# Loglama ayarlarını yapıyoruz
logging.basicConfig(
    level=logging.DEBUG,  # En düşük log seviyesi (DEBUG ve üzerini kaydeder)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log formatı (Zaman - Seviye - Mesaj)
    handlers=[
        logging.FileHandler("debug.log", encoding="utf-8"),  # Logları debug.log dosyasına yazar
        logging.StreamHandler()  # Aynı zamanda konsola da yazdırır
    ]
)

# Test fonksiyonu
def bolme_islemi(a, b):
    logging.info(f"İşlem başladı: {a} / {b} hesaplanıyor.")
    try:
        sonuc = a / b
        logging.debug(f"İşlem başarılı. Sonuç: {sonuc}")
        return sonuc
    except ZeroDivisionError:
        logging.error("Hata! Sıfıra bölme hatası (ZeroDivisionError) yakalandı.", exc_info=True)
        return None

if __name__ == "__main__":
    logging.warning("Program çalıştırıldı.")
    
    # Testler
    bolme_islemi(10, 2)
    bolme_islemi(5, 0)  # Bu satır hata logu oluşturacak
    
    logging.warning("Program sonlandırılıyor.")

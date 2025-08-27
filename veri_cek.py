# veri_cek.py
import requests
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# MEB'in veri endpoint'i
API_URL = "https://e-yaygin.meb.gov.tr/Handlers/ProgramsData.ashx"

def main():
    try:
        logging.info("MEB API'si çağrılıyor...")

        # POST isteği ile tüm program verisi alınıyor
        response = requests.post(API_URL, data={'action': 'getPrograms'}, timeout=30)

        if response.status_code != 200:
            logging.error(f"API Hatası: {response.status_code}")
            return

        raw_data = response.json()

        # Kursları kategorilere göre grupla
        all_data = {
            "Ahşap Teknolojisi": [],
            "Bilişim": [],
            "Dil Eğitimi": [],
            "Spor": [],
            "Mesleki ve Teknik Eğitim": [],
            "İşletme ve Yönetim": [],
            "Görsel ve İşitsel Sanatlar": [],
            "Kişisel Gelişim": [],
            "El Sanatları": [],
            "Yaratıcı Sanatlar Atölyeleri": [],
            "Zihinsel Oyunlar": [],
            "Diğer": []
        }

        category_keywords = {
            "Ahşap Teknolojisi": ["ahşap", "mobilya", "talika", "marangoz"],
            "Bilişim": ["web", "python", "bilgisayar", "programlama"],
            "Dil Eğitimi": ["ingilizce", "almanca", "dil", "yabancı dil"],
            "Spor": ["voleybol", "basketbol", "spor", "futbol"],
            "Mesleki ve Teknik Eğitim": ["elektrik", "tesisat", "motor", "mekatronik"],
            "İşletme ve Yönetim": ["muhasebe", "işletme", "ticaret"],
            "Görsel ve İşitsel Sanatlar": ["resim", "müzik", "fotoğraf"],
            "Kişisel Gelişim": ["zihinsel", "hafıza", "beyin", "performans"],
            "El Sanatları": ["el sanatları", "örgü", "boncuk", "el yapımı"],
            "Yaratıcı Sanatlar Atölyeleri": ["drama", "oyun", "tiyatro"],
            "Zihinsel Oyunlar": ["satranç", "zeka", "bulmaca"]
        }

        for item in raw_
            program_name = item.get("ProgramAdi", "").strip()
            if not program_name:
                continue

            category = "Diğer"
            lower_name = program_name.lower()

            for cat, keys in category_keywords.items():
                if any(k in lower_name for k in keys):
                    category = cat
                    break

            kurs = {
                "ad": program_name,
                "sure": item.get("ToplamSaat", "Bilgi yok"),
                "girisKosullari": item.get("GirisKosullari", "Bilgi yok"),
                "egiticiNiteligi": item.get("EgiticiNiteligi", "Bilgi yok"),
                "programIcerik": item.get("ProgramIcerigi", "Bilgi yok")
            }

            all_data[category].append(kurs)

        # data.json olarak kaydet
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)

        total = sum(len(v) for v in all_data.values())
        logging.info(f"✅ Başarılı: {len(all_data)} alan, {total} kurs kaydedildi.")

    except Exception as e:
        logging.error(f"Hata: {e}")

if __name__ == "__main__":
    main()
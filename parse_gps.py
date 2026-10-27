import sys
import math
import csv
import hashlib

def lire_et_filtrer_fichier(input_file):
    lines_filtrees = []

    with open(input_file, 'r', encoding='latin-1') as f:
        for line in f:
            if "GNSS_ACCESS_LIB" in line or "Trip Data" in line:
                lines_filtrees.append(line.strip())
    return lines_filtrees

def extraire_donnees_brutes(lines):
    records =  []
    for line in lines:
        try:
            parties = line.split(',')
            date_str = parties[1]
            heure_complete = parties[2]
            timestamp = f"{date_str} {heure_complete.split('.')[0]}"

            lat_str = parties[3].replace('"', '').strip()
            lon_str = parties[4].replace('"', '').strip()

            lat = float(lat_str)
            lon = float(lon_str)
            alt = 0.0

            records.append((timestamp, lat, lon, alt))

        except (ValueError, IndexError):
            continue
        
    return records

def nettoyer_et_dedoublonner(records):
    cleaned = []
    for ts, lat, lon, alt in records:
        if math.isnan(lat) or math.isnan(lon) or math.isnan(alt):
            continue

        lat_r = round(lat, 2)
        lon_r = round(lon, 2)
        alt_r = round(alt, 2)

        if cleaned:
            dernier_ts, dernier_lat, dernier_lon, dernier_alt = cleaned[-1]
            if lat_r == dernier_lat and lon_r == dernier_lon:
                continue
        cleaned.append((ts, lat_r, lon_r, alt_r))
    return cleaned

def exporter_et_hasher(cleaned_records, output_file="output_cleaned.csv"):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=";")
        
        writer.writerow(["timestamp", "latitude", "longitude", "altitude"])
        for record in cleaned_records:
            writer.writerow(record)

    sha256_obj = hashlib.sha256()
    with open(output_file, 'rb') as f_bin:
        for chunk in iter(lambda: f_bin.read(4096), b""):
            sha256_obj.update(chunk)

    sha256_hash = sha256_obj.hexdigest()

    print(f"SHA-256 : {sha256_hash}")
    print(f"FLAG : FLAG_OCLCC_{sha256_hash[:12]}")

if __name__ == "__main__":
    lignes = lire_et_filtrer_fichier("input_log.txt")
    print(f"[ETAPE 1] Lignes retenues : {len(lignes)}")

    records = extraire_donnees_brutes(lignes)
    print(f"[ETAPE 2] Enregistrements valides extraits : {len(records)}")

    points_final = nettoyer_et_dedoublonner(records)
    print(f"[ETAPE 3] Points nettoyés et dédoublonnés : {len(points_final)}")

    exporter_et_hasher(points_final, "output_cleaned.csv")
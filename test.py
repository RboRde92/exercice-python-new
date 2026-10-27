import sys

def traiter_dump_gps(input_file):
    with open(input_file, 'r', encoding='latin-1') as f:
        raw_lines = [line.strip() for line in f if "GNSS_ACCESS_LIB" in line or "Trip Data" in line]
if __name__ == "__main__":
    lignes = traiter_dump_gps("input_log.txt")
    print(f"[ETAPE 1] Lignes retenues : {len(raw_lines)}")
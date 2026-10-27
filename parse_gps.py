import sys

def lire_et_filtrer_fichier(input_file):
    lines_filtrees = []

    with open(input_file, 'r', encoding='latin-1') as f:
        for line in f:
            if "GNSS_ACCESS_LIB" in line or "Trip Data" in line:
                lines_filtrees.append(line.strip())
    return lines_filtrees
if __name__ == "__main__":
    lignes = lire_et_filtrer_fichier("input_log.txt")
    print(f"[ETAPE 1] Lignes retenues : {len(lignes)}")
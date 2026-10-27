log = ["OK", "WARNING: disk full", "INFO", "WARNING: temp", "OK", "WARNING: disk purged", "INFO", "WARNING: temp", "OK", "WARNING: disk full1", "INFO", "WARNING: temp", "OK", "WARNING: disk full2", "INFO", "WARNING: temp", "OK", "WARNING: disk full98", "INFO", "WARNING: temp_corrupted", "OK", "WARNING: disk full3", "INFO", "WARNING: temp", "OK", "WARNING: disk full_yes", "INFO", "WARNING: temp_temp"]

compteur = 0
for ligne in log:
    if "WARNING" in ligne:
        compteur += 1

print(f"nombre de lignes contenant 'WARNING' : {compteur}")
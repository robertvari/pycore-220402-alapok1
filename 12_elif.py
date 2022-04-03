status = 100

if status == 100:
    print("folytatás: A kérést elfogadta a szerver, a kliensnek el kell küldenie a kérés törzsét.")
elif status == 200:
    print("sikeres kérés: A kérést elfogadta a szerver, az eredményt visszaküldi.")
elif status == 300:
    print("több választás: Jelzi, hogy a kért erőforrásnak több változata is létezik, például egy videó több formátumban is elérhető.")
elif status == 400:
    print("hibás kérés: A kérés nem végrehajtható, mert rossz szintaxisú, túl hosszú stb.")
elif status == 500:
    print("belső szerverhiba: Egy általános hibaüzenet szerverhibák jelzésére.")
else:
    print("Ez az eset nincs lekezelve.")
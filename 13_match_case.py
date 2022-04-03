status = 301

match status:
    case 100:
        print("folytatás: A kérést elfogadta a szerver, a kliensnek el kell küldenie a kérés törzsét.")
    case 200:
        print("sikeres kérés: A kérést elfogadta a szerver, az eredményt visszaküldi.")
    case 300:
        print("több választás: Jelzi, hogy a kért erőforrásnak több változata is létezik, például egy videó több formátumban is elérhető.")
    case 400:
        print("hibás kérés: A kérés nem végrehajtható, mert rossz szintaxisú, túl hosszú stb.")
    case 500:
        print("belső szerverhiba: Egy általános hibaüzenet szerverhibák jelzésére.")
    case _:
        print("Ez az eset nincs lekezelve.")

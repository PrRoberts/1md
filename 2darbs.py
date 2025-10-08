# Vienkārša loģistikas programma: aprēķina piegādes laiku un izmaksas atkarībā no izvēlētā transporta tipa

# Transporta veidi ar ātrumu (km/h) un cenu (EUR/kg)
transporti = {
    "gaisa": {"atrums": 800, "cena": 2.5},
    "jūras": {"atrums": 35, "cena": 0.4},
    "sauszemes": {"atrums": 90, "cena": 1.0},
    "dzelzceļa": {"atrums": 120, "cena": 0.8}
}

while True:
    # Ievades pārbaude svaram
    while True:
        try:    
            svars = float(input("\nIevadi kravas svaru (kg): "))
            if svars <= 0:
                print("❌ Svars jāievada kā pozitīvs skaitlis!")
            else:
                break
        except :
            print("❌ Nepareizs ievads! Lūdzu, ievadi skaitli.")

    # Ievades pārbaude attālumam
    while True:
        try:
            attalums = float(input("Ievadi attālumu (km): "))
            if attalums <= 0:
                print("❌ Attālums jāievada kā pozitīvs skaitlis!")
            else:
                break
        except:
            print("❌ Nepareizs ievads! Lūdzu, ievadi skaitli.")

    tips = input("Izvēlies transporta tipu (gaisa, jūras, sauszemes, dzelzceļa): ").lower()

    # Pārbauda, vai ievadītais transporta tips ir derīgs
    if tips in transporti:
        atrums = transporti[tips]["atrums"]
        cena = transporti[tips]["cena"]

        # Aprēķina piegādes laiku un izmaksas
        laiks = attalums / atrums
        izmaksas = svars * cena

        # Aprēķina stundas un minūtes
        stundas = int(laiks)
        minutes = int((laiks - stundas) * 60)

        print(f"\nPiegāde ar {tips} transportu:")
        print(f"- Laiks: {stundas} stundas un {minutes} minūtes (~{laiks/24:.1f} dienas)")
        print(f"- Izmaksas: {izmaksas:.2f} EUR")

        # Papildu: salīdzina visus transporta veidus
        print("\nSalīdzinājums ar citiem transporta veidiem:")
        for transportatips, dati in transporti.items():
            laiks_t = attalums / dati["atrums"]
            izmaksas_t = svars * dati["cena"]
            stundas_t =int(laiks_t)
            minutes_t = int((laiks_t - stundas_t) * 60)
            print(f"{transportatips.title()}: laiks ~ {stundas_t}h un {minutes_t} minūtes, izmaksas {izmaksas_t:.2f} EUR")

    else:
        print("❌ Šāds transporta veids nav pieejams.")

    # Jautā, vai lietotājs grib turpināt
    if input("\nVai rēķināt vēlreiz? (j/n): ").lower() != "j":
        print("Programma pabeigta.")
        break

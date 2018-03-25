class Czlowiek():
    def __init__(self):
        print("wywolal sie init")
    gatunek = "human"

    # tworze instancje klasy

marcin = Czlowiek()
print(marcin.gatunek)

krzysztof = Czlowiek()
print(krzysztof.gatunek)

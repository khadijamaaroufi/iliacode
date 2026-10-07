from bonjour import saluer
def test_saluer_khadija():
 assert saluer("khadija") == "Bonjour khadija"
def test_saluer_vide():
 assert saluer("") == "Bonjour "
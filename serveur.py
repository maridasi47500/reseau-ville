from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue au serveur avec des routes pour véhicules, commerces, piétons, vélos et réseaux!"

# Routes pour les véhicules
@app.route('/vehicule/te_comparera_a_un_sunner')
def vehicule_sunner():
    return jsonify({"vehicule": "TE COMPARERA À UN SUNNER", "description": "Un véhicule au design futuriste et aux performances impressionnantes."})

@app.route('/vehicule/alohay')
def vehicule_alohay():
    return jsonify({"vehicule": "ALOHAY", "description": "Un véhicule écologique avec une technologie avancée pour des trajets sans impact environnemental."})

@app.route('/vehicule/8087')
def vehicule_8087():
    return jsonify({"vehicule": "8087", "description": "Un modèle de véhicule luxueux avec des caractéristiques de sécurité de pointe."})

@app.route('/vehicule/sur_alice')
def vehicule_sur_alice():
    return jsonify({"vehicule": "SÛR ALICE", "description": "Un véhicule de haute sécurité conçu pour offrir une protection maximale à ses occupants."})

@app.route('/vehicule/ethernet_gigabi')
def vehicule_ethernet_gigabi():
    return jsonify({"vehicule": "ETHERNET GIGABI", "description": "Un véhicule ultrarapide équipé de la dernière technologie de communication."})

@app.route('/vehicule/io_gigabit_ethernet')
def vehicule_io_gigabit_ethernet():
    return jsonify({"vehicule": "Io Gigabit Ethernet", "description": "Un véhicule innovant utilisant la technologie Gigabit Ethernet pour une connectivité et des performances optimales."})

@app.route('/vehicule/192.168.1.1')
def vehicule_192_168_1_1():
    return jsonify({"vehicule": "192.168.1.1", "description": "Adresse IP privée souvent utilisée par les routeurs domestiques."})

@app.route('/vehicule/192.168.0.1')
def vehicule_192_168_0_1():
    return jsonify({"vehicule": "192.168.0.1", "description": "Adresse IP privée souvent utilisée par les routeurs."})

@app.route('/vehicule/10.0.0.1')
def vehicule_10_0_0_1():
    return jsonify({"vehicule": "10.0.0.1", "description": "Adresse IP privée utilisée dans les réseaux d'entreprise."})

# Route pour le parking (contrôle d'admission)
@app.route('/commerce/controle_admission')
def commerce_controle_admission():
    return jsonify({"commerce": "CONTRÔLE D'ADMISSION", "description": "Entreprise fournissant des solutions de gestion des accès et de sécurité, avec une capacité de parking."})

# Routes pour les vélos
@app.route('/velo/energy_efficient_working')
def velo_energy_efficient_working():
    return jsonify({"velo": "Energy Efficient Working", "description": "Un vélo conçu pour maximiser l'efficacité énergétique tout en offrant une expérience de conduite agréable."})

# Routes pour les commerces
@app.route('/commerce/reseaux_informatiques')
def commerce_reseaux_informatiques():
    return jsonify({"commerce": "RÉSEAUX INFORMATIQUES", "description": "Commerce spécialisé dans les solutions et services de réseaux informatiques."})

@app.route('/commerce/communication_sans_fil')
def commerce_communication_sans_fil():
    return jsonify({"commerce": "COMMUNICATION SANS FIL", "description": "Boutique offrant des produits et services de communication sans fil."})

@app.route('/commerce/centre_de_donnees')
def commerce_centre_de_donnees():
    return jsonify({"commerce": "CENTRE DE DONNÉES", "description": "Centre spécialisé dans la gestion et le stockage de données."})

@app.route('/commerce/ipv6')
def commerce_ipv6():
    return jsonify({"commerce": "IPv6", "description": "Entreprise fournissant des services et des solutions basés sur le protocole IPv6."})

@app.route('/commerce/cdn')
def commerce_cdn():
    return jsonify({"commerce": "CDN", "description": "Service de réseau de diffusion de contenu pour améliorer la vitesse de chargement des sites web."})

@app.route('/commerce/raid')
def commerce_raid():
    return jsonify({"commerce": "RAID", "description": "Magasin spécialisé dans les systèmes de stockage redondants pour la sécurité des données."})

@app.route('/commerce/sonet')
def commerce_sonet():
    return jsonify({"commerce": "SONET", "description": "Fournisseur de technologies de réseau optique synchrone."})

@app.route('/commerce/cafe_internet')
def commerce_cafe_internet():
    return jsonify({"commerce": "CAFÉ INTERNET", "description": "Lieu offrant des services de connexion internet et des boissons."})

@app.route('/commerce/trudy')
def commerce_trudy():
    return jsonify({"commerce": "TRUDY", "description": "Boutique spécialisée dans les accessoires de mode et les gadgets technologiques."})

@app.route('/commerce/protocole')
def commerce_protocole():
    return jsonify({"commerce": "PROTOCOLE", "description": "Entreprise offrant des formations et des solutions en protocoles de communication."})

@app.route('/commerce/ver')
def commerce_ver():
    return jsonify({"commerce": "VER", "description": "Service spécialisé dans la prévention et la gestion des menaces de sécurité informatique."})

@app.route('/commerce/pile')
def commerce_pile():
    return jsonify({"commerce": "PILE", "description": "Boutique proposant des solutions énergétiques et des batteries de haute performance."})

# Routes pour les réseaux
@app.route('/reseau/mpls')
def reseau_mpls():
    return jsonify({"reseau": "MPLS", "description": "Multiprotocol Label Switching (MPLS) est une méthode pour acheminer les paquets de données à travers un réseau en utilisant des étiquettes pour créer des tunnels et optimiser le trafic."})

@app.route('/reseau/sonet')
def reseau_sonet():
    return jsonify({"reseau": "SONET", "description": "SONET (Synchronous Optical Networking) est une norme de transmission de données par fibre optique, utilisée pour les réseaux de télécommunications avec des capacités élevées et une grande fiabilité."})

@app.route('/reseau/trudy')
def reseau_trudy():
    return jsonify({"reseau": "TRUDY", "description": "Un réseau tolérant aux délais (DTN - Delay Tolerant Network) conçu pour fonctionner même avec des interruptions de communication ou des latences élevées. Comme si Trudy avait des jumelles, ce réseau est capable de gérer les déconnexions temporaires et d'assurer la livraison fiable des données, même dans des conditions difficiles."})

@app.route('/reseau/collision_de_screaming_medias')
def reseau_collision_de_screaming_medias():
    return jsonify({"reseau": "Collision de Screaming Médias", "description": "Un scénario où plusieurs médias tentent de diffuser simultanément, créant des collisions de données et des interférences dans le réseau."})

# Route pour un piéton
@app.route('/pieton/worm')
def pieton_worm():
    return jsonify({"pieton": "Worm", "description": "Un piéton mystérieux avec une allure sinueuse et captivante."})

# Route pour un poème
@app.route('/poeme/sonet')
def poeme_sonet():
    return jsonify({"poeme": "Should I compare you to a summer's day?", "description": "Thou art more lovely and more temperate: Rough winds do shake the darling buds of May, And summer's lease hath all too short a date."})

# Route pour la file d'attente
@app.route('/reseau/queuing')
def reseau_queuing():
    return jsonify({"reseau": "File d'attente", "description": "La gestion de la file d'attente dans les réseaux permet de réguler le flux de données et d'assurer une distribution équitable des ressources."})

# Route pour la conversation entre Bob et Alice
@app.route('/reseau/secret')
def reseau_secret():
    return jsonify({"reseau": "Can I tell you a secret, Bob? Sure, Alice.", "description": "Une analogie souvent utilisée pour expliquer les concepts de cryptographie et de communication sécurisée."})

# Route pour le voisinage peer-to-peer
@app.route('/reseau/peer_to_peer')
def reseau_peer_to_peer():
    return jsonify({"reseau": "Voisinage Peer-to-Peer", "description": "Les réseaux peer-to-peer permettent aux dispositifs de communiquer directement entre eux, sans passer par un serveur central, pour un partage de ressources plus efficace."})

if __name__ == '__main__':
    app.run(debug=True)

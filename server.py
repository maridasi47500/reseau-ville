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

@app.route('/vehicule/ip_192_168_1_1')
def vehicule_ip_192_168_1_1():
    return jsonify({"vehicule": "Véhicule IP 192.168.1.1", "description": "Un véhicule connecté avec l'adresse IP 192.168.1.1, offrant des services de réseau avancés."})

@app.route('/vehicule/ip_192_168_1_2')
def vehicule_ip_192_168_1_2():
    return jsonify({"vehicule": "Véhicule IP 192.168.1.2", "description": "Un véhicule connecté avec l'adresse IP 192.168.1.2, optimisé pour la performance réseau."})

@app.route('/vehicule/ip_192_168_1_3')
def vehicule_ip_192_168_1_3():
    return jsonify({"vehicule": "Véhicule IP 192.168.1.3", "description": "Un véhicule connecté avec l'adresse IP 192.168.1.3, intégré avec la dernière technologie réseau."})

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

@app.route('/commerce/controle_admission')
def commerce_controle_admission():
    return jsonify({"commerce": "CONTRÔLE D'ADMISSION", "description": "Système de gestion de parking assurant la régulation et l'organisation des places disponibles."})

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
    return jsonify({"reseau": "TRUDY", "description": "Un réseau tolérant aux délais (DTN - Delay Tolerant Network) conçu pour fonctionner même avec des interruptions de communication ou des latences élevées. Comme si Trudy avait des

# Recupere la map parsée

# class Map
    # Initialise pour chaque zone (class Zone)
        # Emplacement (coordonnees x, y)
        # Couleur
        # Regle de priorité (normal, blocked, restricted, priority)
        # Nombre de drones autorises en simultanés
        # Liste des drones present
        # Liste des connections

    # Class Connection
        # zone 1
        # zone 2
        # liste des drones presents
        # nombre de drones autorises

# ◦ normal – Standard zone with 1 turn movement cost (default)
# ◦ blocked – Inaccessible zone. Drones must not enter or pass through this zone.
# Any path using it is invalid.
# ◦ restricted – A sensitive or dangerous zone. Movement to this zone costs 2
# turns.
# ◦ priority – A preferred zone. Movement to this zone costs 1 turn but should
# be prioritized in pathfinding.

    # class Drone
        # zone courente ou None 
        # connection courente ou None 
            # Si connection:
                # zone de destination
                # Decomptage des tours de transit 
        # (cas ou drone dans une connection vers zone restreinte
        # doit etre egale a zero pour que le drone puisse entrer dans la zone)

    # Taille de la map

    # Deplacement des drones
        # Test si deplacement possible 
        # Modification des donnes de chaque zone, connections et drones,
        # en temps reel, au fil des tours
        # Comptage des tours
        # Affichage en temps reel
    
    # Nombre de tours deja effectue

    # Affichage
from pydantic import BaseModel

class Engin(BaseModel):
    immatriculation: str
    proprietaire: str
    categorie: str
    cotation_assurance: float

TAUX_MAJORATION_ECONOMAT = 0.1

engins = [
    Engin(
        immatriculation="ABC123",
        proprietaire="Congrégation",
        categorie="Voiture",
        cotation_assurance=1000.0
    ),
    Engin(
        immatriculation="XYZ789",
        proprietaire="Communauté religieuse",
        categorie="Moto",
        cotation_assurance=800.0
    ),
    Engin(
        immatriculation="DEF456",
        proprietaire="Soeur",
        categorie="Voiture",
        cotation_assurance=1200.0
    )
]

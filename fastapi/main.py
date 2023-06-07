from fastapi import FastAPI
from typing import List
from models import Engin
import models

app = FastAPI()

engins = models.engins

@app.get("/categorie/{categorie}")
def obtenir_engins_par_categorie(categorie: str) -> List[Engin]:
    result = [engin for engin in engins if engin.categorie.lower() == categorie.lower()]
    return result

@app.get("/proprietaire/{proprietaire}")
def obtenir_engins_par_proprietaire(proprietaire: str) -> List[Engin]:
    result = [engin for engin in engins if engin.proprietaire.lower() == proprietaire.lower()]
    return result

@app.get("/factures/{proprietaire}")
def obtenir_factures_par_proprietaire(proprietaire: str):
    engins_proprietaire = [engin for engin in engins if engin.proprietaire.lower() == proprietaire.lower()]
    total_cotation = sum(engin.cotation_assurance for engin in engins_proprietaire)
    majoration_economat = total_cotation * models.TAUX_MAJORATION_ECONOMAT
    montant_total_facture = total_cotation + majoration_economat
    return {
        "proprietaire": proprietaire,
        "montant_total_facture": montant_total_facture,
        "engins": [engin.immatriculation for engin in engins_proprietaire]
    }

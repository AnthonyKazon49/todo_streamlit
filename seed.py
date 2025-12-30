from __future__ import annotations

import uuid
from datetime import date

def new_id() -> str:
    return str(uuid.uuid4())

def seed_tasks() -> list[dict]:
    def t(text, project, section, tags=None, priority="Moyenne", impact=3, effort=3, status="Todo", due=None):
        return {
            "id": new_id(),
            "task": text,
            "project": project,
            "section": section,
            "priority": priority,
            "impact": impact,
            "effort": effort,
            "status": status,
            "due": due,
            "completed": (status == "Done"),
            "tags": tags or [],
        }

    return [
        t("CORMA : faire le CR du rdv de vendredi", "PRIORITÉS", "À attaquer en premier", ["corma"], "Haute", 5, 2),
        t("CORMA : expression de besoin (version 1)", "PRIORITÉS", "À attaquer en premier", ["corma"], "Haute", 5, 3),
        t("LinkedIn : refaire mon CV", "PRIORITÉS", "À attaquer en premier", ["linkedin"], "Haute", 5, 3),
        t("Mémoire : démarrer un 1er plan (2ème partie)", "PRIORITÉS", "À attaquer en premier", ["memoire"], "Haute", 5, 3),

        t("Créer ma page LinkedIn", "LinkedIn / Marque perso", "Base", ["linkedin"], "Moyenne", 4, 2),
        t("Préparation du portfolio", "LinkedIn / Marque perso", "Base", ["portfolio"], "Moyenne", 4, 3),
        t("Envisager un planning éditorial", "LinkedIn / Marque perso", "Contenus", ["contenu"], "Basse", 3, 2),

        t("Landing page : cadrer le 'compte tenu du site'", "CORMA", "Site + offre", ["corma", "web"], "Haute", 5, 2),
        t("Landing page : faire les contenus", "CORMA", "Site + offre", ["corma", "copywriting"], "Haute", 5, 3),
        t("Landing page : construire sur Lovable", "CORMA", "Site + offre", ["corma", "lovable"], "Moyenne", 4, 3),
        t("Landing page : valider / publier", "CORMA", "Site + offre", ["corma", "web"], "Moyenne", 4, 2),
        t("Plaquette", "CORMA", "Site + offre", ["corma"], "Moyenne", 4, 3),
        t("Expression de besoin", "CORMA", "Site + offre", ["corma"], "Haute", 5, 3),
        t("Architecture sur Claude", "CORMA", "Tech", ["corma", "archi"], "Moyenne", 4, 3),

        t("Faire une automation", "Automation", "Général", ["automation"], "Moyenne", 4, 2),
        t("Planning de projet", "Automation", "Général", ["planning"], "Moyenne", 4, 2),

        t("Reprise de notes Greg", "Mémoire", "Travail", ["memoire"], "Haute", 4, 2),
        t("Démarrer un premier plan (2ème partie)", "Mémoire", "Travail", ["memoire"], "Haute", 5, 3),

        t("Automation : supprimer les désinscrits", "La cochonnaille", "Cleanup", ["automation"], "Haute", 4, 2),
        t("Préparer les livrables : la doc", "La cochonnaille", "Livrables", ["livrables"], "Moyenne", 4, 2),
        t("Préparer le dernier rdv", "La cochonnaille", "Rendez-vous", ["rdv"], "Haute", 4, 2),

        t("Faire la première carto", "myDSU", "Projet", ["carto"], "Haute", 5, 3),
        t("Faire les premières PV de recette", "myDSU", "Projet", ["recette"], "Haute", 5, 3),
        t("Préparer les tableaux de bords", "myDSU", "BI", ["dashboard"], "Moyenne", 4, 3),

        t("Liste des contenus pour les posts", "PERSO", "Contenus", ["contenu"], "Moyenne", 4, 2),
        t("Projet DuckDB : SQL + Python", "PERSO", "Portfolio", ["portfolio", "duckdb"], "Moyenne", 4, 3),
        t("Projet Streamlit", "PERSO", "Portfolio", ["portfolio", "streamlit"], "Moyenne", 4, 3),
    ]

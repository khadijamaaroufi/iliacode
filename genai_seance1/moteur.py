import math

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MOTEUR_PAR_DEFAUT = "Qwen/Qwen2.5-Coder-7B"


def charger_moteur(nom=MOTEUR_PAR_DEFAUT):
    appareil = "cuda" if torch.cuda.is_available() else "cpu"
    format_ = torch.float16 if appareil == "cuda" else torch.float32
    tokeniseur = AutoTokenizer.from_pretrained(nom)
    modele = AutoModelForCausalLM.from_pretrained(nom, dtype=format_)
    modele.to(appareil)
    modele.eval()
    return modele, tokeniseur


def compter_parametres(modele):
    return sum(p.numel() for p in modele.parameters())


def memoire_poids(modele):
    return sum(p.numel() * p.element_size() for p in modele.parameters())


def probas_moteur(modele, tokeniseur, texte):
    numeros = tokeniseur(texte, return_tensors="pt")["input_ids"].to(modele.device)
    with torch.no_grad():
        scores = modele(numeros).logits[0].float()
    probas = torch.softmax(scores[:-1], dim=-1)
    ecrits = numeros[0, 1:]
    return probas[torch.arange(len(ecrits)), ecrits].tolist()


def surprise_par_caractere(probas, texte):
    if not probas or not texte:
        return math.inf
    total = sum(math.inf if p == 0 else -math.log2(p) for p in probas)
    return total / len(texte)
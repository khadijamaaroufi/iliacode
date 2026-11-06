# Le choix du moteur d'ILIACode

## La machine

- GPU : NVIDIA L4
- mémoire G : 24 Go
- cache prévu : 4 demandes de 8 192 tokens, soit 32 768 tokens
- part fixe : 1,5 Go
- N_max : 10,3 Mds
- classe de moteur retenue : 7 à 10 Mds

## La grille

Une ligne par candidat. N, la mémoire 2N et l'étiquette de licence se
lisent sur la page du moteur, la licence complète dans son fichier LICENSE.
D/N et HumanEval viennent du cours.

| candidat | D/N | N | mémoire 2N | tient ? | licence, étiquette | licence, fichier LICENSE | HumanEval | verdict |
|---|---|---|---|---|---|---|---|---|
| mistralai/Codestral-22B-v0.1 | non publié | 22,2 Mds | 44,4 Go | non | mnpl | non commerciale |  | écarté, taille |
| Qwen/Qwen2.5-Coder-3B | 7 605 | 3,09 Mds | 6,2 Go | oui | qwen-research | recherche seule |  | écarté, licence |
| 01-ai/Yi-Coder-9B | 716 | 8,8 Mds | 17,6 Go | oui | apache-2.0 | libre | 53,7 | classé 2e |
| Qwen/Qwen2.5-Coder-7B | 3 092 | 7,61 Mds | 15,2 Go | oui | apache-2.0 | libre | 61,6 | retenu |
| Qwen/Qwen2.5-Coder-1.5B | 15 260 | 1,54 Md | 3,1 Go | oui | apache-2.0 | libre |  | témoin |

## La décision

- moteur retenu : Qwen/Qwen2.5-Coder-7B
- témoin : Qwen/Qwen2.5-Coder-1.5B
- pourquoi, en trois phrases : Codestral est écarté par la taille, car ses 22,2 Mds (44,4 Go) dépassent le N_max de 10,3 Mds du L4, et le 3B est écarté par la licence, car qwen-research le réserve à un usage non commercial. Les deux survivants tiennent, sont sous apache-2.0 et ont lu bien plus de vingt tokens par paramètre (3 092 et 716), mais les bancs ne les départagent pas seuls : le 7B mène sur HumanEval avec 61,6 contre 53,7 (1,5 σ écart) et MBPP donne une égalité. Je retiens donc Qwen2.5-Coder 7B sur l'ensemble, plus petit de 1,2 Md (7,6 contre 8,8 Mds) et avec le plus grand D/N, le 1,5 Md de la même famille servant de témoin.

## La mesure interne

Bits par caractère du moteur retenu sur le test de la séance 2.

| bloc | bits par caractère |
|---|---|
| code |  |
| anglais |  |
| français |  |
| darija |  |
# 🔐 Python Secret Code

## 📖 Description

Le programme manipule une chaîne de caractères afin de construire, analyser, valider et transformer un **code secret** à travers plusieurs fonctions dépendantes.

🎯 L'objectif principal est de développer une bonne maîtrise de la programmation modulaire, des chaînes de caractères, des boucles et des algorithmes de vérification.

---

## ✨ Fonctionnalités

* 🔤 Validation d'une chaîne de caractères
* 📏 Calcul de la longueur sans utiliser `len()`
* 🚫 Suppression des espaces
* 🔄 Inversion d'une chaîne
* 🔐 Construction d'un code secret
* 🅰️ Comptage des voyelles
* 📊 Recherche de la lettre la plus fréquente
* ✅ Vérification de la validité du code
* 🔀 Transformation du code par décalage alphabétique
* 🪞 Détection d'un palindrome

---

## 🧠 Concepts d'algorithmique

Ce projet permet de travailler :

* 🧩 La programmation modulaire
* 🔁 Les boucles `for` et `while`
* 🔤 La manipulation des chaînes
* 🔢 Les indices
* ⚖️ Les conditions
* 🔎 La recherche
* 🔄 La construction de nouvelles chaînes
* 🧮 Les calculs sur les caractères
* 🧪 La validation de données
* 🏗️ La décomposition d'un problème en fonctions

---

## 🛠️ Technologies

```text
🐍 Python 3
```

Aucune bibliothèque externe n'est nécessaire.

---

## 📂 Structure du projet

```text
Python-Secret-Code/
│
├── main.py
└── README.md
```

### Fonctions principales

```text
saisie()
supprimerEspaces()
inverse()
construireCode()
nbVoyelles()
plusFrequente()
estValide()
transformer()
estPalindrome()
```

---

## 🔐 Fonctionnement

Le programme suit plusieurs étapes :

```text
Saisie
  ↓
Validation
  ↓
Suppression des espaces
  ↓
Analyse de la chaîne
  ↓
Construction du code
  ↓
Vérification
  ↓
Transformation
  ↓
Test du palindrome
```

---

## 📋 Règles de validation

La chaîne saisie doit respecter plusieurs contraintes :

* 📏 Longueur comprise entre **8 et 30 caractères**
* 🔠 Uniquement des lettres majuscules et des espaces
* 🔢 Au moins **5 lettres**

Le code généré doit ensuite respecter plusieurs critères :

* 📏 Longueur minimale
* 🔤 Nombre minimal de voyelles
* 🔁 Présence de lettres consécutives identiques
* ➗ Somme des positions alphabétiques divisible par 3

Avec :

```text
A = 1
B = 2
C = 3
...
Z = 26
```

---

## 🚫 Contraintes

Pour se rapprocher des conditions d'un exercice d'algorithmique du Bac, certaines fonctions Python intégrées peuvent être volontairement évitées :

```text
len()
count()
max()
min()
sort()
reverse()
index()
```

Les traitements sont réalisés principalement avec des **boucles, conditions et fonctions personnelles**.

---

## 🚀 Exécution

Lancer le programme :

```bash
python main.py
```

Puis saisir une chaîne valide lorsque le programme le demande.

---

## 🎯 Niveau

**🔥 Difficulté : 9/10**

Projet destiné à un entraînement avancé en algorithmique, notamment pour travailler les exercices où plusieurs fonctions sont **dépendantes les unes des autres**.

---

## 📚 Objectif

Ce projet a été réalisé dans le but de progresser en :

> **Algorithmique → Python → Programmation modulaire → Préparation Bac Maths Tunisie**

L'objectif est de passer progressivement d'exercices classiques à des problèmes nécessitant davantage de raisonnement algorithmique.

---

## 👨‍💻 Author
⭐ Si ce projet t'aide dans ton apprentissage, n'hésite pas à lui donner une étoile !

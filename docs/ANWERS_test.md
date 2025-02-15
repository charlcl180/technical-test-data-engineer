# 📌 Réponses du test technique

## ✅ **Utilisation de la solution (Étapes 1 à 3)**

### **Étape 1 : Création et activation de l'environnement virtuel**

Pour exécuter ce projet, nous devons d'abord configurer un environnement virtuel et y installer les dépendances requises.

#### **1️⃣ Vérifier si `venv` est disponible**
Avant de créer un environnement virtuel, nous nous assurons que `venv` est bien installé :
```powershell
python -m venv --help
```
Si cette commande retourne une aide sur `venv`, nous pouvons passer à la prochaine étape.

#### **2️⃣ Créer un environnement virtuel**
Nous créons un nouvel environnement virtuel nommé `venv` avec la commande suivante :
```powershell
python -m venv venv
```
Cela générera un dossier `venv/` contenant tous les fichiers nécessaires.

#### **3️⃣ Activer l'environnement virtuel**
- **Sous Windows (PowerShell) :**
  ```powershell
  venv\Scripts\activate
  ```
  ⚠️ **Note :** Si vous obtenez une erreur liée aux politiques d’exécution des scripts, exécutez cette commande pour autoriser temporairement les scripts :
  ```powershell
  Set-ExecutionPolicy Unrestricted -Scope Process
  ```
- **Sous macOS/Linux :**
  ```bash
  source venv/bin/activate
  ```

#### **4️⃣ Installer les dépendances du projet**
Une fois l'environnement activé, nous installons les dépendances requises à partir du fichier `requirements.txt` :
```powershell
pip install -r requirements.txt
```
Après cette étape, l'environnement virtuel est prêt à être utilisé.

---

### **Étape 2 : Automatisation de la récupération des données**
Nous planifions l'exécution automatique du script `fetch_and_save.py` pour récupérer quotidiennement les données depuis l'API.

#### **1️⃣ Créer une tâche planifiée sous Windows**
Nous utilisons `schtasks` pour exécuter le script chaque jour à 08h00 du matin :
```powershell
schtasks /create /tn "FetchAPIData" /tr "\"C:\\Users\\Clayton\\git\\technical-test-data-engineer\\venv\\Scripts\\python.exe\" \"C:\\Users\\Clayton\\git\\technical-test-data-engineer\\src\\moovitamix_fastapi\\fetch_and_save.py\"" /sc daily /st 08:00 /F
```

#### **2️⃣ Vérifier que la tâche a bien été créée**
```powershell
schtasks /query /tn "FetchAPIData"
```
Cela affiche les détails de la tâche planifiée.

#### **3️⃣ Tester l’exécution immédiate de la tâche**
```powershell
schtasks /run /tn "FetchAPIData"
```
Si tout fonctionne correctement, les fichiers CSV seront mis à jour dans le dossier de destination.

---

### **Étape 3 : Vérification et tests**

Pour nous assurer que notre pipeline de récupération de données fonctionne correctement, nous avons mis en place des tests unitaires avec `pytest`.

#### **1️⃣ Exécuter les tests**
```powershell
pytest test/unit/
```
Si tous les tests passent, le pipeline est bien fonctionnel. Sinon, nous analysons les erreurs et ajustons le code en conséquence.

#### **2️⃣ Automatiser les tests avant chaque commit**
Nous avons mis en place un hook `pre-commit` pour exécuter les tests avant chaque commit Git. Ainsi, aucun commit ne sera accepté si un test échoue.

```powershell
pip install pre-commit
pre-commit install
```

Ensuite, nous avons ajouté la configuration suivante dans `.pre-commit-config.yaml` :
```yaml
repos:
  - repo: local
    hooks:
      - id: pytest
        name: Run Pytest
        entry: pytest
        language: system
        types: [python]
```
Désormais, à chaque commit, `pytest` sera automatiquement exécuté.

---

## ✅ **Questions (Étapes 4 à 7)**

### **Étape 4 : Schéma de base de données**
_votre réponse ici_

### **Étape 5 : Suivi de la santé du pipeline de données**
_votre réponse ici_

### **Étape 6 : Automatisation du calcul des recommandations**
_votre réponse ici_

### **Étape 7 : Automatisation du réentraînement du modèle**
_votre réponse ici_

---

🎯 **Cette documentation assure une installation fluide et une bonne gestion du pipeline de récupération des données.**

💡 **Des améliorations ou questions ?** 🚀


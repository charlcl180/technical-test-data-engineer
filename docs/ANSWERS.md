# Réponses du test

## _Utilisation de la solution (étape 1 à 3)_

_Inscrire la documentation technique_

### **Étape 1 : Création de l'environnement virtuel**
Pour la création de l'environnement virtuel, nous avons fait différentes commandes pour faire le tout.

Nous voulons nous assurer que venv est installé pour pouvoir exécuter la prochaine commande:
```powershell
python -m venv --help
```

Une fois que la commande retourne une aide sur venv, nous pouvons créer notre environnement virtuel avec cette commande:

```powershell
python -m venv venv
```
Cette commande créera un nouveau dossier venv avec plusieurs documents différents. Une fois le document créé, on exécute cette commande.

```powershell
venv\Scripts\activate
```
    Il est possible que par défaut, il y a une politique d’exécution des scripts sous PowerShell, alors Windows bloque l'exécution des fichiers .ps1. Il faut donc autoriser temporairement l'exécution des scripts

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Une fois l'environnement virtuelle activé, on peut installer les différents dépendances nécessaires dans le fichier requirements.txt en faisant la commande:
    
```powershell
pip install -r requirements.txt
```

Étape 2:

Nous utilisons `schtasks` pour exécuter le script chaque jour à 08h00 du matin :
```powershell
schtasks /create /tn "FetchAPIData" /tr "\"C:\\Users\\Clayton\\git\\technical-test-data-engineer\\venv\\Scripts\\python.exe\" \"C:\\Users\\Clayton\\git\\technical-test-data-engineer\\src\\moovitamix_fastapi\\fetch_and_save.py\"" /sc daily /st 08:00 /F
```

Nous pouvons s'assurer que la tâche a bien été créée avec cette commande:

```powershell
schtasks /query /tn "FetchAPIData"
```
Si tout fonctionne correctement, les fichiers CSV seront mis à jour dans le dossier datas.

Étape 3


## Questions (étapes 4 à 7)

### Étape 4

_votre réponse ici_

### Étape 5

_votre réponse ici_

### Étape 6

_votre réponse ici_

### Étape 7

_votre réponse ici_

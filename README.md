# Utilisation de GANG-siteweb


## Avec environnement de travail

### Manipulation pour window

1. Ouvrir GitBash
2. Faire les commandes suivantes :
   * pip install virtualenvwrapper
   * cd ~
   * touch .bashrc
   * vim .bashrc
   * Appuyez sur I puis ecrire :
      * source /c/Python34/Scripts/virtualenvwrapper.sh (remplacer le chemin par votre chemin Python)
      * export WORKON_HOME=~/.virtualenvs (remplacer par le chemin ou vous voulez que vos env soient stockés)
   
   * Appuyez sur Echap puis sur :wq
   
   
### Créer un environnement 
   * mkvirtualenv envname
   
   
### Activer un environnement
   * workon envname
    

## Installation

1. Install GitBash https://git-for-windows.github.io/
2. Ouvrir GitBash dans le dossier du projet (click droit git bash here)
3. Faire les commandes suivantes : 
   * pip install -r requirement.txt
   * export DJANGO_SETTINGS_MODULE=gangdev.settings.dev
   * python manage.py runserver
   * Ouvrir votre navigateur a l'adresse : localhost:8000

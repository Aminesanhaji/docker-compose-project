# Utiliser une image Python
FROM python:3.9

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]

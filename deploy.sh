#!/bin/bash

# Script de déploiement automatique pour Codex
# Ce script permet à l'outil Codex AI de déployer le site automatiquement

# Vérifier si Netlify CLI est installé
if ! command -v netlify &> /dev/null; then
    echo "Installation de Netlify CLI..."
    npm install netlify-cli -g
fi

# Définir l'ID du site Netlify (à partir du fichier de configuration windsurf_deployment.yaml)
SITE_ID=$(grep -o 'project_id: .*' windsurf_deployment.yaml | cut -d ' ' -f 2)

if [ -z "$SITE_ID" ]; then
    echo "Erreur: ID de site non trouvé dans windsurf_deployment.yaml"
    exit 1
fi

echo "Déploiement du site avec l'ID: $SITE_ID"

# Déployer le site
netlify deploy --dir=. --prod --site="$SITE_ID"

# Vérifier si le déploiement a réussi
if [ $? -eq 0 ]; then
    echo "✅ Déploiement réussi ! Le site est en ligne."
    echo "URL: https://codex-site-web.windsurf.build"
else
    echo "❌ Erreur lors du déploiement. Veuillez vérifier les logs ci-dessus."
fi

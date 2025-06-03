#!/bin/bash

# Script de déploiement automatique simplifié pour Codex
# Ce script déploie automatiquement le site sur Surge.sh sans authentification complexe

echo "🚀 Déploiement simplifié du site web Codex"
echo "============================================="

# Vérifier si npm est installé
if ! command -v npm &> /dev/null; then
    echo "❌ npm n'est pas installé. Veuillez installer Node.js et npm."
    exit 1
fi

# Créer un sous-domaine unique basé sur la date et un identifiant aléatoire
RANDOM_ID=$(cat /dev/urandom | LC_ALL=C tr -dc 'a-z0-9' | fold -w 6 | head -n 1)
TIMESTAMP=$(date +%Y%m%d)
SUBDOMAIN="codex-site-${TIMESTAMP}-${RANDOM_ID}"

echo "📦 Installation de Surge.sh..."
npm install --quiet --no-progress surge

echo "🌐 Déploiement du site vers https://${SUBDOMAIN}.surge.sh"
npx surge --project . --domain ${SUBDOMAIN}.surge.sh

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Déploiement réussi!"
    echo "🔗 Votre site est maintenant disponible à l'adresse:"
    echo "   https://${SUBDOMAIN}.surge.sh"
    echo ""
    echo "📝 URL sauvegardée dans deploy_info.txt"
    echo "https://${SUBDOMAIN}.surge.sh" > deploy_info.txt
else
    echo "❌ Erreur lors du déploiement."
fi

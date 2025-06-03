# Codex

Un site web simple créé avec HTML, CSS et JavaScript.

## Structure du projet

- `index.html` - La page principale du site
- `styles.css` - Les styles CSS du site
- `script.js` - Les fonctionnalités JavaScript
- `deploy.sh` - Script shell de déploiement manuel
- `codex_deploy.py` - Script Python pour déploiement automatisé par Codex AI
- `.github/workflows/deploy.yml` - Configuration GitHub Actions pour déploiement automatisé

## Déploiement

Ce site est déployé sur Netlify avec l'URL: https://codex-site-web.windsurf.build

### Options de déploiement pour Codex AI

#### 1. Utiliser le script Python (recommandé)

```bash
# Déploiement en production
python3 codex_deploy.py

# Déploiement d'une version préliminaire
python3 codex_deploy.py --draft
```

#### 2. Utiliser le script shell

```bash
./deploy.sh
```

#### 3. Utiliser npm scripts

```bash
# Installer les dépendances
npm install

# Déploiement en production
npm run deploy

# Déploiement d'une version préliminaire
npm run deploy:draft
```

#### 4. Déploiement automatique via GitHub Actions

Pour utiliser GitHub Actions, définissez les secrets suivants dans votre dépôt GitHub :
- `NETLIFY_AUTH_TOKEN` : Votre token d'authentification Netlify
- `NETLIFY_SITE_ID` : L'ID du site (présent dans windsurf_deployment.yaml)

Ensuite, chaque push sur la branche main déclenchera automatiquement un déploiement.

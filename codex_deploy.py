#!/usr/bin/env python3
"""
Script de déploiement automatique pour Codex AI.
Ce script permet à l'outil Codex AI de déployer le site automatiquement sur Netlify.

Usage:
    python3 codex_deploy.py [--draft]

Options:
    --draft     Déployer une version préliminaire (non en production)
"""

import os
import sys
import subprocess
import yaml
import re

def get_site_id():
    """Récupérer l'ID du site depuis le fichier de configuration."""
    try:
        with open("windsurf_deployment.yaml", "r") as file:
            config = yaml.safe_load(file)
            return config.get("project_id", "")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier de configuration: {e}")
        # Fallback vers la méthode regex pour les cas où PyYAML n'est pas disponible
        try:
            with open("windsurf_deployment.yaml", "r") as file:
                content = file.read()
                match = re.search(r'project_id:\s*([^\s]+)', content)
                if match:
                    return match.group(1)
        except Exception:
            pass
        return ""

def check_netlify_cli():
    """Vérifie si Netlify CLI est installé et l'installe si nécessaire."""
    try:
        subprocess.run(["netlify", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        print("Netlify CLI n'est pas installé. Installation en cours...")
        try:
            subprocess.run(["npm", "install", "-g", "netlify-cli"], check=True)
            return True
        except Exception as e:
            print(f"Erreur lors de l'installation de Netlify CLI: {e}")
            return False

def deploy(draft=False):
    """Déploie le site sur Netlify."""
    if not check_netlify_cli():
        print("❌ Netlify CLI n'est pas disponible. Installation échouée.")
        return False
    
    site_id = get_site_id()
    if not site_id:
        print("❌ ID du site non trouvé dans le fichier de configuration.")
        return False
    
    print(f"📦 Déploiement du site avec l'ID: {site_id}")
    
    # Préparation de la commande de déploiement
    cmd = ["netlify", "deploy", "--dir=."]
    if not draft:
        cmd.append("--prod")
    cmd.extend(["--site", site_id])
    
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(result.stdout)
        print("✅ Déploiement réussi!")
        # Extraire l'URL du site déployé
        match = re.search(r'Website URL:\s*(https://[^\s]+)', result.stdout)
        if match:
            url = match.group(1)
            print(f"🌐 URL du site: {url}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du déploiement: {e}")
        print(e.stdout)
        print(e.stderr)
        return False

if __name__ == "__main__":
    draft_mode = "--draft" in sys.argv
    deploy(draft_mode)

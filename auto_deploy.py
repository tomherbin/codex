#!/usr/bin/env python3
"""
Script d'automatisation du déploiement pour Codex AI.
Ce script permet de:
1. Mettre à jour le site local
2. Commiter les changements
3. Pousser vers la branche master pour déclencher le déploiement GitHub Actions
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime

def run_command(command, cwd=None):
    """Exécute une commande shell et retourne la sortie"""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, 
                               capture_output=True, cwd=cwd)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Erreur: {e.stderr}"

def git_is_setup():
    """Vérifie si Git est configuré avec un remote"""
    success, output = run_command("git remote -v")
    return success and len(output.strip()) > 0

def setup_git_remote(repo_url=None):
    """Configure le dépôt Git remote si nécessaire"""
    if git_is_setup():
        print("✅ Dépôt Git déjà configuré")
        return True
    
    if not repo_url:
        print("❌ URL du dépôt Git non fournie. Impossible de configurer le remote.")
        return False
    
    # Configurer le remote
    success, output = run_command(f"git remote add origin {repo_url}")
    if not success:
        print(f"❌ Échec de la configuration du remote: {output}")
        return False
    
    print("✅ Remote Git configuré avec succès")
    return True

def auto_deploy(message=None, repo_url=None):
    """Procédure complète de déploiement automatique"""
    # Vérifier si nous sommes dans un dépôt Git
    success, _ = run_command("git rev-parse --is-inside-work-tree")
    if not success:
        print("❌ Ce dossier n'est pas un dépôt Git valide.")
        return False
    
    # Créer un message de commit par défaut si non fourni
    if not message:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Mise à jour automatique par Codex AI - {now}"
    
    # Configurer le remote si nécessaire
    if repo_url and not git_is_setup():
        if not setup_git_remote(repo_url):
            return False
    
    # 1. Ajouter tous les fichiers modifiés
    print("📝 Ajout des fichiers modifiés...")
    success, output = run_command("git add .")
    if not success:
        print(f"❌ Échec lors de l'ajout des fichiers: {output}")
        return False
    
    # 2. Créer un commit
    print(f"📦 Création du commit: {message}")
    success, output = run_command(f"git commit -m \"{message}\"")
    if not success:
        # Si rien à commiter, pas d'erreur
        if "nothing to commit" in output:
            print("ℹ️ Aucun changement à commiter.")
            return True
        print(f"❌ Échec lors de la création du commit: {output}")
        return False
    
    # 3. Pousser vers la branche master/main
    branch = "master"  # Par défaut, on utilise master
    
    # Vérifier la branche actuelle
    success, current_branch = run_command("git rev-parse --abbrev-ref HEAD")
    if success:
        branch = current_branch.strip()
    
    print(f"🚀 Envoi des modifications vers la branche {branch}...")
    success, output = run_command(f"git push origin {branch}")
    if not success:
        print(f"❌ Échec lors de l'envoi des modifications: {output}")
        print("💡 Si c'est la première fois que vous poussez, utilisez: git push -u origin master")
        return False
    
    print("✅ Déploiement automatique déclenché avec succès!")
    print("   Le site sera mis à jour automatiquement par GitHub Actions.")
    print("   Vous pouvez vérifier le statut du déploiement dans l'onglet 'Actions' de votre dépôt GitHub.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Outil de déploiement automatique pour Codex AI")
    parser.add_argument("-m", "--message", help="Message de commit personnalisé")
    parser.add_argument("-r", "--repo", help="URL du dépôt Git (seulement pour la configuration initiale)")
    args = parser.parse_args()
    
    auto_deploy(args.message, args.repo)

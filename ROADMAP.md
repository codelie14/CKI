# 🗺 ROADMAP - Cyber Knowledge Intelligence (CKI)

Ce document suit l'évolution du projet CKI, de la fondation à la production.

---

## 🏗 Phase 1 : Fondation & Modélisation (✅ Terminé)
- [x] Initialisation de l'environnement Django (cki_project, core, theme)
- [x] Création des applications modulaires (scraper, ai_engine, knowledge, scanner)
- [x] Configuration MySQL & Tailwind CSS
- [x] **Modélisation de la base de données (App: knowledge)**
    - [x] Définition des modèles : Vulnerability, Vendor, Product, Exploit, ThreatGroup, etc.
    - [x] Migration vers SQLite (développement) / MySQL (production)
- [x] **Interface de base (App: core)**
    - [x] Layout principal avec Tailwind & DaisyUI
    - [x] Dashboard vide avec indicateurs globaux
    - [x] Interface d'administration complète

## 🔍 Phase 2 : Cyber Scraper Engine (App: scraper)
- [ ] Mise en place du moteur de scraping multi-sources
    - [ ] Intégration CVE (NVD API/Feed)
    - [ ] Scraping Blogs (BeautifulSoup/Requests)
    - [ ] Gestion des doublons & scheduler local (APScheduler)
- [ ] Dashboard de monitoring des scans

## 🧠 Phase 3 : AI Intelligence Engine (App: ai_engine)
- [ ] Intégration locale d'Ollama (via API locale)
- [ ] Pipeline d'analyse automatique des contenus collectés
    - [ ] Résumé technique & extraction d'entités (CVE ID, CVSS, Vendor)
    - [ ] Classification des menaces (Malware, Phishing, Ransomware)
- [ ] Mapping MITRE ATT&CK & détection IoC

## 🧬 Phase 4 : Knowledge Graph & Visualisation (App: knowledge)
- [ ] Création du graphe de connaissances (Relations CVE → Produit → Vendor)
- [ ] Visualisation interactive des données
- [ ] Moteur de recherche avancée & filtrage multicritères

## 🚨 Phase 5 : Alerting & Reporting (App: core)
- [ ] Système d'alerte intelligent basé sur la criticité
- [ ] Génération automatique de rapports (PDF, Markdown, CSV)
- [ ] Notification locale

---

## 🎉 Prochaines étapes immédiates :
1. ✅ Définir les modèles dans `knowledge/models.py` - **FAIT**
2. ✅ Lancer la migration initiale - **FAIT**
3. ✅ Finaliser le layout du Dashboard - **FAIT**
4. 🔄 Commencer Phase 2 : Cyber Scraper Engine (App: scraper)
   - [ ] Intégration CVE (NVD API/Feed)
   - [ ] Scraping Blogs (BeautifulSoup/Requests)
   - [ ] Gestion des doublons & scheduler local (APScheduler)

---

## 📊 État actuel du projet :

### ✅ Ce qui est fonctionnel :
- **Base de données** : Tous les modèles sont créés et migrés
- **Dashboard** : Interface moderne avec Tailwind CSS + DaisyUI
- **Admin Django** : Interface d'administration complète pour tous les modèles
- **Architecture modulaire** : 5 apps prêtes (core, knowledge, scraper, ai_engine, scanner)

### 🔧 Accès à l'application :
- **Dashboard** : http://127.0.0.1:8000/
- **Admin** : http://127.0.0.1:8000/admin/
  - Username: `admin`
  - Password: `admin123`

### 📝 Notes importantes :
- **Base de données** : SQLite pour le développement (facile à configurer)
- **Production** : Prévu pour MySQL/MariaDB 10.5+ (à upgrader si nécessaire)
- **CSS Framework** : Tailwind CSS v4 + DaisyUI avec thème dark

# 🗺 ROADMAP - Cyber Knowledge Intelligence (CKI)

Ce document suit l'évolution du projet CKI, de la fondation à la production.

---

## 🏗 Phase 1 : Fondation & Modélisation (En cours)
- [x] Initialisation de l'environnement Django (cki_project, core, theme)
- [x] Création des applications modulaires (scraper, ai_engine, knowledge, scanner)
- [x] Configuration MySQL & Tailwind CSS
- [ ] **Modélisation de la base de données (App: knowledge)**
    - [ ] Définition des modèles : Vulnerability, Vendor, Product, Exploit, ThreatGroup, etc.
    - [ ] Migration vers MySQL
- [ ] **Interface de base (App: core)**
    - [ ] Layout principal avec Tailwind & DaisyUI
    - [ ] Dashboard vide avec indicateurs globaux

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

## 🛠 Prochaines étapes immédiates :
1. Définir les modèles dans `knowledge/models.py`.
2. Lancer la migration initiale vers MySQL.
3. Finaliser le layout du Dashboard.

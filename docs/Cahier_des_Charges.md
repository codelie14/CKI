# 🛡 CYBER KNOWLEDGE INTELLIGENCE (CKI)

### Plateforme Locale d’Intelligence et de Veille Cybersécurité

---

# 1️⃣ Contexte du Projet

Dans un contexte d’augmentation continue des cybermenaces, les professionnels de la cybersécurité ont besoin d’un système autonome capable de :

* Collecter automatiquement des données de cybersécurité
* Les analyser intelligemment
* Les structurer
* Générer des alertes pertinentes
* Produire des rapports stratégiques

Le projet **Cyber Knowledge Intelligence (CKI)** est une plateforme **100% locale** développée avec :

* Django
* MySQL
* Tailwind CSS
* JavaScript
* Ollama

---

# 2️⃣ Objectifs du Projet

## 🎯 Objectif Principal

Créer un système local d’intelligence cyber capable de :

* Scraper automatiquement des sources de cybersécurité
* Analyser les contenus avec IA locale
* Extraire des entités structurées
* Détecter les menaces critiques
* Générer des alertes personnalisées
* Construire une base de connaissance évolutive

---

# 3️⃣ Portée Fonctionnelle

---

## 🔎 3.1 Module 1 – Cyber Scraper Engine

### Fonctionnalités :

* Scraping automatique multi-sources :

  * CVE databases
  * Blogs cybersécurité
  * CERT
  * GitHub advisories
* Planification automatique (scheduler local)
* Rotation User-Agent
* Détection doublons
* Gestion erreurs réseau
* Respect robots.txt
* Mode scraping manuel (URL personnalisée)

---

## 🧠 3.2 Module 2 – AI Intelligence Engine (via Ollama)

Analyse automatique :

* Résumé technique
* Extraction :

  * CVE ID
  * CVSS
  * Vendor
  * Produit affecté
  * Version
* Classification :

  * Ransomware
  * Malware
  * Phishing
  * Zero-day
  * Data breach
* Niveau de criticité
* Détection exploit public
* Mapping MITRE ATT&CK
* Détection IoC (IP, hash, domain)

---

## 🗄 3.3 Module 3 – Base de Données Structurée

### Tables principales :

* vulnerabilities
* vendors
* products
* exploits
* threat_groups
* articles
* attack_patterns
* indicators_of_compromise
* ai_analysis
* alerts
* reports

### Fonctionnalités :

* Détection doublons
* Indexation full-text
* Relations entités multiples
* Historique des modifications

---

## 📊 3.4 Module 4 – Dashboard & Visualisation

Interface moderne avec Tailwind.

Fonctionnalités :

* Vue globale menace
* Graphiques évolution CVE
* Heatmap criticité
* Top vendors vulnérables
* Timeline interactive
* Recherche avancée
* Filtrage multicritères
* Score global de menace (CTI)

---

## 🧬 3.5 Module 5 – Knowledge Graph

* Relations dynamiques :

  * CVE → Produit
  * CVE → Vendor
  * Exploit → Groupe APT
* Visualisation interactive
* Mise à jour automatique

---

## 🚨 3.6 Module 6 – Smart Alert System

* Alertes basées sur criticité
* Alertes personnalisées
* Notification locale
* Génération rapport automatique si critique

---

## 📄 3.7 Module 7 – Génération de Rapport

* Rapport quotidien
* Rapport hebdomadaire
* Résumé exécutif
* Export :

  * PDF
  * Markdown
  * CSV

---

# 4️⃣ Exigences Techniques

## 4.1 Architecture

Architecture modulaire :

```text
CyberKnowledge/
│
├── core/
├── scraper/
├── ai_engine/
├── knowledge/
├── graph/
├── alerts/
├── reports/
├── dashboard/
├── scheduler/
```

---

## 4.2 Environnement

* Système 100% local
* Compatible Windows / Linux
* Exécution via serveur Django local
* IA via Ollama en local
* MySQL local

---

## 4.3 Performance

* Scraping asynchrone
* Limitation consommation CPU
* Cache intelligent
* Gestion mémoire optimisée

---

## 4.4 Sécurité

* Authentification locale
* Gestion rôles (Admin / Analyste)
* Protection CSRF
* Validation entrées
* Journalisation (logs sécurité)

---

# 5️⃣ Exigences Non Fonctionnelles

* Interface ergonomique
* Code modulaire
* Documentation complète
* Facilité d’extension
* Maintenance simplifiée
* Scalabilité future (cloud-ready)

---

# 6️⃣ Contraintes

* 100% offline
* Pas d’API externe payante
* Utilisation exclusive d’Ollama local
* Respect légalité scraping

---

# 7️⃣ Planning Prévisionnel

### Phase 1

* Conception base de données
* Scraper basique
* Intégration Ollama simple

### Phase 2

* Extraction entités
* Dashboard
* Alertes

### Phase 3

* Knowledge graph
* Rapports automatiques
* Score CTI

### Phase 4

* Optimisation
* Tests
* Documentation finale

---

# 8️⃣ Livrables

* Code source complet
* Base de données structurée
* Documentation technique
* Manuel utilisateur
* Diagramme architecture
* Rapport projet

---

# 9️⃣ Perspectives d’Évolution

* Intégration IDS/IPS
* Intégration SIEM
* Mode SaaS futur
* API REST publique
* Analyse prédictive ML

---

# 🔥 Conclusion

Le projet **Cyber Knowledge Intelligence (CKI)** vise à devenir une plateforme locale complète d’intelligence cyber, combinant scraping automatisé, analyse IA locale, structuration avancée et visualisation stratégique.

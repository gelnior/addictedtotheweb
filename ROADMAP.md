# Roadmap — addictedtotheweb

Améliorations possibles pour la page perso, en gardant le style minimaliste.

## Fait

- [x] Nettoyage HTML (structure, liens cassés, typo)
- [x] Mise à jour contenu (Kitsu/CGWire, bio, presse)
- [x] Open Graph + URL canonique
- [x] Liens externes en HTTPS
- [x] Dimensions images + lazy loading (footer, contributions)
- [x] Photo de profil LinkedIn
- [x] Retrait de Twitter
- [x] Icônes Mastodon et Bluesky (taille harmonisée)
- [x] CSS : espacement des titres, survol des liens, hero mobile, liste projets

## Contenu

Priorité haute — clarifier qui tu es aujourd’hui.

- [ ] Lien discret vers Kitsu ou CGWire dès la première phrase de **Career**
- [ ] **Press** : garder 3–5 liens récents (Kitsu, indie, podcasts) + une ligne du type *« Older press about Cozy Cloud »* avec 2–3 liens
- [ ] **Inspirations** : réduire à un paragraphe, ou déplacer vers le blog (*more about me*)
- [ ] **Past projects** : ne garder que 4–5 projets les plus parlants pour ton profil actuel

## Structure

Sans changer le look.

- [x] Ancres sur les `h3` (`#career`, `#press`, etc.) pour partager une section
- [x] Fusionner **Contact** et **Social** en une seule section
- [x] Lien discret sous le hero pour inviter au scroll (optionnel)

## Technique

- [ ] `rel="noopener noreferrer"` sur les liens `target="_blank"` si ajoutés
- [ ] `mailto:` optionnel à côté de `frank[at]addictedtointer.net`
- [ ] Préchargement de la police Lato (si le fichier est versionné)

## Style

- [ ] Affiner l’équilibre visuel des icônes legacy (blog, GitHub, LinkedIn) si besoin
- [ ] Ajuster le hero desktop si le vide en haut paraît trop grand

## À éviter (hors scope minimaliste)

- Menu fixe, dark mode, carrousel
- Traduction FR/EN complète
- Analytics lourds (préférer rien ou compteur auto-hébergé)

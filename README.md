# Spiral Knights — French Localisation

**Community-driven French localisation of Spiral Knights.**

This repository is a community-maintained fork of [greyhavens/spiral-knights-i18n](https://github.com/greyhavens/spiral-knights-i18n), dedicated to improving and maintaining the French localisation of *Spiral Knights*.

Our goal is to provide accurate, consistent and natural French translations while preserving the original meaning, terminology and technical structure of the game's localisation files.

This is an independent community translation initiative, not an official Grey Havens localisation team.

## Contributing

Contributions are welcome! You can report translation issues, suggest improvements or submit Pull Requests.

**Each translation or coherent group of translation changes must be developed on a dedicated branch and submitted through a separate Pull Request targeting `main`.** Direct changes to `main` are not permitted.

All contributions are subject to automated validation and review before being merged.

If you would like to join the translation team as a regular collaborator, you can get in touch through:

- **Discord:** `saukko33` / `overlarde` (direct message) 
- **Email:** mgouilhers@asteeriks.com / `overlarde.producer@gmail.com`

You do not need to be a repository collaborator to suggest a translation or submit a contribution.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## Français

Ce dépôt est un fork communautaire du [projet officiel de localisation de Spiral Knights](https://github.com/greyhavens/spiral-knights-i18n), consacré à l'amélioration et à la maintenance des traductions françaises du jeu.

Notre objectif est de proposer des traductions fidèles, naturelles et cohérentes, tout en respectant la terminologie originale et les contraintes techniques des fichiers de localisation.

### Participer aux traductions

Toutes les contributions sont les bienvenues : corrections orthographiques, améliorations de formulations, traductions manquantes ou harmonisation terminologique.

**Chaque traduction ou ensemble cohérent de traductions doit être effectué sur une branche dédiée et faire l'objet d'une Pull Request distincte vers `main`.**

Les modifications directes sur `main` ne sont pas autorisées. Les contributions sont soumises aux contrôles automatiques et à une relecture avant leur intégration.

### Rejoindre l'équipe

Vous souhaitez participer régulièrement au projet et devenir collaborateur du dépôt ?

Contactez les mainteneurs :

- **Discord :** `saukko33` (message privé)
- **E-mail :** mgouilhers@asteeriks.com

Il n'est pas nécessaire de rejoindre l'équipe pour proposer des corrections.

Les modalités détaillées sont disponibles dans [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Original repository documentation

The following documentation originates from the official Grey Havens repository and is retained for reference.

---


# spiral-knights-i18n
Internationalization bundles for Spiral Knights

## How it works
We will occasionally publish new English translations here.

We will accept pull requests for other languages, including new ones.

Then these translations will make their way into the game.

### Fine details

If a translation doesn't need to change it can be omitted from a bundle and the English
version will be used.

The properties files need to be well-formatted and readable by Java. Characters above 127
should be escaped by using `\u00e7` convention.

Run `python3 tools/check_bundles.py` before sending a pull request. It reports keys that
aren't in the English bundle, unescaped characters, and placeholders, HTML tags or `|`
separators that don't match the English. To check only one language, pass it with `--lang`,
e.g. `python3 tools/check_bundles.py --lang es`, and to check only one bundle, use `--bundle`,
e.g. `--bundle pvp`. They can be combined: `--bundle pvp --lang es`.

If you edit a bundle in an editor that saves accented letters as-is, run
`python3 tools/fix_unicode.py pvp_es` (or a path to the file) to rewrite them as `\uXXXX`
escapes. Add `--check` to only list the files that need it.

## License and contributions

### Ownership

Copyright © Grey Havens. All rights reserved.

Spiral Knights, and all text, translations and other material in this repository, are
the property of Grey Havens. "Spiral Knights" and its logos are trademarks of Grey Havens.
This repository is made public only so that people can view it and contribute
translations. Grey Havens grants no license to copy, distribute, modify or otherwise use
any of this material for any other purpose, and grants no rights in its trademarks.

### Contributor terms

By submitting a pull request, issue, comment or any other material to this repository
(a "Contribution"), you agree to the following:

1. **License to Grey Havens.** You grant Grey Havens, and its successors and assigns, a
   perpetual, worldwide, non-exclusive, royalty-free, fully paid-up, irrevocable license,
   with the right to sublicense and transfer, to use, reproduce, modify, adapt, translate,
   create derivative works of, publicly display, publicly perform, distribute and
   otherwise exploit your Contribution, in whole or in part, in any media and for any
   purpose, including in Spiral Knights and its marketing and promotion.
2. **No compensation.** You will not receive any payment, royalty or other compensation
   for your Contribution.
3. **No obligation.** Grey Havens has no obligation to use your Contribution, to credit
   you, or to keep your Contribution in the game, and may edit or remove it at any time.
4. **Moral rights.** To the extent permitted by law, you waive, and agree not to assert
   against Grey Havens or its licensees, any moral rights or similar rights you have in
   your Contribution, including any right to be identified as its author or to object to
   changes to it.
5. **Your promises.** You represent that:
   - your Contribution is your own original work, or you otherwise have the right to
     grant the license above;
   - your Contribution does not include material copied from any other game, product or
     third party, and does not infringe or violate anyone's copyright, trademark, privacy
     or other rights;
   - if your employer or anyone else has rights to work you create, you have their
     permission to make the Contribution; and
   - you are of legal age to agree to these terms, or your parent or legal guardian has
     read and agreed to them on your behalf.
6. **No warranty.** You provide your Contribution "as is", without warranty of any kind,
   and you are not responsible for supporting it.

If you do not agree to these terms, do not submit a Contribution.

## Ancient history

We used to have a google spreadsheet. We could push a button and it would export the current
english translations and also import anything from any of the corresponding columns for
each language. Perhaps it would be nice to re-create something like that, built on top of this.

Having a front-end for nicely typing-in a label or message and having it automatically output
a well-formatted .properties file would be great!

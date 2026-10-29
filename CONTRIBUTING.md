# Contributing to Spiral Knights — French Localisation

Thank you for your interest in contributing to the French localisation of *Spiral Knights*!

This repository is a community-maintained fork of [greyhavens/spiral-knights-i18n](https://github.com/greyhavens/spiral-knights-i18n), dedicated to improving the quality, consistency and completeness of the game's French translations.

Contributions are welcome from everyone, regardless of previous translation experience.

## 1. How to contribute

You can contribute to the project by:

- Reporting missing, incorrect or inconsistent translations through GitHub Issues.
- Suggesting improvements to existing French translations.
- Submitting Pull Requests containing translation fixes or additions.
- Participating in discussions about terminology and localisation choices.

You do not need to be a member of the translation team to contribute.

### Joining the translation team

If you would like to become a regular collaborator and help maintain the repository, you can contact the project maintainers:

- **Discord:** `saukko33` / `overlarde` (direct message) 
- **Email:** mgouilhers@asteeriks.com / `overlarde.producer@gmail.com`

Requests to join the team are reviewed individually. Repository write access is not required to submit contributions.

## 2. Branch and Pull Request policy

**Every translation or coherent group of translation changes must be developed on a dedicated branch and submitted through a separate Pull Request.**

Direct modifications to `main` are not permitted.

This policy applies to all contributors, including collaborators with write access.

### Branch naming

Use descriptive branch names that identify the area being translated or corrected.

Examples:

- `fr/crucible-review` — Crucible interface translations.
- `fr/auction-terminology` — Auction House terminology.
- `fr/interface-fixes` — General interface corrections.
- `fr/missing-translations` — A defined group of missing translations.
- `docs/contributing-update` — Contribution documentation updates.

Branches should be created from the latest version of `main`.

Avoid including unrelated changes in the same branch or Pull Request.

### Submitting a Pull Request

1. Create a dedicated branch from `main`.
2. Make your translation changes.
3. Validate the modified localisation files.
4. Commit your changes with a descriptive message.
5. Open a Pull Request targeting `main` in this repository.
6. Describe what has been changed and why.
7. Address any feedback from reviewers.

Example Pull Request title:

`i18n(fr): improve Crucible translations`

Each Pull Request should remain focused on a clearly defined change or set of related changes.

### Review and merging

All Pull Requests are subject to automated checks and human review.

At least one approval from an authorised reviewer is required before merging, in accordance with the repository's branch protection rules.

Maintainers may request additional changes to ensure linguistic accuracy, terminology consistency or technical compatibility.

Approved Pull Requests are merged into `main` using **Squash and merge**.

Merged branches may be deleted once they are no longer required.

## 3. Translation guidelines

Our objective is to provide French translations that are accurate, natural, consistent and appropriate for the game's interface and setting.

### Accuracy and context

- Preserve the meaning and intent of the original English text.
- Prefer natural French expressions over literal word-for-word translations.
- Consider the context in which each message appears.
- Avoid introducing information that is not present in the original text.
- Check existing French translations before introducing new terminology.

When the meaning of a string is unclear, open an Issue or Discussion rather than making an unsupported assumption.

### French language conventions

- Use correct French grammar, spelling and punctuation.
- Maintain a consistent register suitable for the game's interface.
- Use appropriate French typographical conventions where technically supported.
- Prefer clear and concise wording, particularly for buttons, labels and notifications.
- Avoid unnecessary anglicisms when an established French equivalent exists.

### Terminology consistency

Terminology should remain consistent across localisation files.

For example, an interface action should not alternate between different French terms without a contextual reason.

If an existing translation is technically correct but stylistically inconsistent, explain the proposed change in the Pull Request.

## 4. Technical requirements

The localisation files use Java `.properties` syntax.

Contributors must preserve their structure and formatting.

### Translation keys

Do not rename, remove or duplicate existing translation keys unless the change is explicitly required and justified.

For example:

```properties
m.is_private = Test priv\u00e9
```

Only modify the translated value when correcting an existing translation.

### Unicode escaping

Characters above ASCII 127 must be represented using Unicode escape sequences, following the conventions of the original repository.

For example:

```properties
m.love_uploaded = Niveau charg\u00e9.
```

Do not replace `\u00e9` with an unescaped accented character.

The upstream repository provides a utility for converting Unicode characters:

```bash
python3 tools/fix_unicode.py crucible_fr.properties
```

You can also check whether a file requires conversion:

```bash
python3 tools/fix_unicode.py crucible_fr.properties --check
```

### Placeholders and formatting

Dynamic placeholders must be preserved.

Examples include:

- `{0}`, `{1}`, `{2}`
- `\n`
- HTML formatting tags
- `|` separators
- Line continuation characters

For example:

```properties
m.play_count = Parties jou\u00e9es : {0}
```

Removing or incorrectly modifying a placeholder can break the corresponding in-game message.

### Missing translations

The upstream repository allows translations to be omitted when the English fallback is sufficient.

However, contributors are encouraged to identify untranslated strings and propose suitable French translations where appropriate.

Missing keys should not be added blindly. Their context, meaning and relevance should be verified beforehand.

## 5. Validation

Before submitting a Pull Request, run the validation tool provided by the upstream repository:

```bash
python3 tools/check_bundles.py --lang fr
```

To validate a specific bundle:

```bash
python3 tools/check_bundles.py --bundle crucible --lang fr
```

The tool checks for issues such as:

- Keys that do not exist in the English reference bundle.
- Unescaped Unicode characters.
- Mismatched placeholders.
- Inconsistent HTML tags.
- Incorrect `|` separators.

Additional automated checks may also run through GitHub Actions when a Pull Request is opened or updated.

**Passing automated validation does not guarantee the linguistic accuracy of a translation.** Human review remains essential.

## 6. Contributing upstream

This repository is intended to facilitate collaborative French localisation work before proposing accepted improvements to Grey Havens.

Changes merged into our `main` branch are not automatically incorporated into the official game.

Selected changes may subsequently be submitted to the upstream repository through separate Pull Requests.

Contributors should ensure that their changes are compatible with the upstream project's requirements.

### Intellectual property and contributor terms

*Spiral Knights* and the original localisation resources belong to Grey Havens.

The upstream repository contains specific ownership, licensing and contributor terms.

**Before contributing, please read the official [README and contributor terms](https://github.com/greyhavens/spiral-knights-i18n#license-and-contributions).**

This community fork does not replace, amend or override Grey Havens' terms.

## 7. Community conduct

We aim to maintain a constructive and welcoming environment for everyone interested in improving the French localisation.

Please:

- Treat other contributors respectfully.
- Provide constructive feedback.
- Explain translation choices when appropriate.
- Respect differences of opinion concerning style and terminology.
- Focus discussions on linguistic quality and technical compatibility.

Disagreements should be resolved through discussion, with reference to the original English text, established game terminology and the relevant interface context.

---

Thank you for helping improve the French localisation of *Spiral Knights*.

**Spiral Knights — French Localisation Community**

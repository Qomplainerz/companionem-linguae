# Companionem Linguae

**A specialized language model for marginalized and classical languages**

## Current Status
Early development - proof of concept for Latin ↔ English dictionary

## Features (v0.3)
- Migrated from SQLite to MySQL
- Next steps: Add linker table for headwords

## Vocabulary Coverage
- Will be reworked after the migration from SQLite to MySQL

## Roadmap
- [x] Complete conjugation system for one Latin verb
- [ ] Expand to 10+ Latin verbs
- [ ] Add support for nouns, adjectives, adverbs
- [ ] Implement n-gram language detection
- [ ] Add support for: Marubo, other marginalized languages
- [ ] Build simple chat interface (tkinter)
- [ ] Integrate ML-based translation (for high-resource languages)

## Why?
Most NLP tools focus on major languages. This project aims to preserve and make accessible:
- **Dead languages** (Latin, Ancient Greek)
- **Marginalized languages** (Marubo, or other indigenous languages)
- **Hybrid approach:** Rule-based for low-resource, ML for high-resource

## Collaboration
Currently working with Claudio Marubo (native speaker) to collect Marubo language data.

Contributions welcome!

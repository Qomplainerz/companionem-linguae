# Companionem Linguae

**A specialized language model for marginalized and classical languages**

## Current Status
Early development - proof of concept for Latin ↔ English dictionary

## Features (v0.3)
- SQLite database with 36 Latin verbs (infinitive forms)
- 1 complete verb with full conjugations (discere - 126 forms)
- Covers all 4 conjugation classes + irregular verbs (esse, posse, ferre)
- Grammatical metadata for complete verb
- Next steps: Add conjugations for remaining 35 verbs

## Vocabulary Coverage
- 1st conjugation (a-stems): amāre, dare, portāre, vocāre, labōrāre, laudāre, parāre, stāre, spectāre, errāre
- 2nd conjugation (e-stems): habēre, vidēre, tenēre, movēre, dēbēre, docēre, monēre, timēre, manēre
- 3rd conjugation: agere, dīcere, dūcere, mittere, scrībere, capere, facere, pōnere, iacere, discere
- 4th conjugation (i-stems): venīre, audīre, sciīre, dormīre
- Irregular: esse, posse, ferre

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
- **Marginalized languages** (Marubo, other indigenous languages)
- **Hybrid approach:** Rule-based for low-resource, ML for high-resource

## Collaboration
Currently working with Claudio Marubo (native speaker) to collect Marubo language data.

Contributions welcome!

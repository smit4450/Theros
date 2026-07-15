---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/arctic
- monster/environment/forest
- monster/environment/hill
- monster/size/large
- monster/type/celestial
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Owl"
---
# Giant Owl
*Source: Monster Manual (2024) p. 358. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/celestial/img/owl.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Owl"
"size": "Large"
"type": "celestial"
"alignment": "Neutral"
"ac": !!int "12"
"hp": !!int "19"
"hit_dice": "3d10 + 3"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "15"
  - !!int "12"
  - !!int "10"
  - !!int "14"
  - !!int "10"
"speed": "5 ft., fly 60 ft."
"saves":
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+6"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
"damage_resistances": "necrotic, radiant"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 16"
"languages": "Celestial; understands Common, Elvish, and Sylvan but can't speak them"
"cr": "1/4"
"traits":
  - "desc": "The owl doesn't provoke an Opportunity Attack when it flies out of an\
      \ enemy's reach."
    "name": "Flyby"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (1d10 + 2) Slashing damage."
    "name": "Talons"
  - "desc": "The owl casts one of the following spells, requiring no spell components\
      \ and using Wisdom as the spellcasting ability:\n\n**At will:** [Detect Evil\
      \ and Good](/Compendium/spells/detect-evil-and-good-xphb.md), [Detect Magic](/Compendium/spells/detect-magic-xphb.md)\n\
      \n**1/day:** [Clairvoyance](/Compendium/spells/clairvoyance-xphb.md)"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "/Compendium/bestiary/celestial/token/giant-owl-xmm.webp"
```
^statblock

## Environment

arctic, forest, hill
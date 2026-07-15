---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/3
- monster/environment/underdark
- monster/size/medium
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Quaggoth Thonot"
---
# Quaggoth Thonot
*Source: Monster Manual (2024) p. 251*
![](/Compendium/bestiary/monstrosity/img/quaggoth-thonot.webp#right)

Quaggoth thonots possess psionic abilities, which they use to give themselves an edge in combat and to coerce the service of other quaggoths.

## Quaggoths

*Unpredictable Subterranean Stalkers*

- **Habitat.** Underdark  
- **Treasure.** None  

Beastly hunters endemic to subterranean depths, quaggoths scrape harsh existences from the Underdark. While they can survive on bitter lichens and toxic fungi, they viciously attack anything they can make a meal of, from giant spiders to explorers. Quaggoths sometimes serve as muscle for Underdark-dwelling villains.

Quaggoths frequently collect in small bands led by the most fearsome group member. These bands are proud and quick to hold grudges. Anyone who harms a quaggoth—or who is suspected of doing so—earns the enmity of that quaggoth's band regardless of reason or fault. These grudges sometimes extend to whole communities rather than individuals. Generations of quaggoths might seek revenge against a settlement's inhabitants for decades-old slights. Only the leader of a quaggoth band can demand that a grudge ends.

![](/Compendium/bestiary/monstrosity/img/quaggoths.webp#center)

## Statblock

```statblock
"name": "Quaggoth Thonot"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Neutral"
"ac": !!int "15"
"hp": !!int "67"
"hit_dice": "9d8 + 27"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "16"
  - !!int "6"
  - !!int "14"
  - !!int "7"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 12"
"languages": "Undercommon"
"cr": "3"
"traits":
  - "desc": "While [Bloodied](/Compendium/rules/conditions.md#Bloodied), the quaggoth\
      \ has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md) on attack\
      \ rolls."
    "name": "Bloodied Fury"
"actions":
  - "desc": "The quaggoth makes two Claw attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Slashing damage\
      \ plus 5 (2d4) Psychic damage."
    "name": "Claw"
  - "desc": "The quaggoth casts one of the following spells, requiring no spell components\
      \ and using Wisdom as the spellcasting ability (spell save DC 12):\n\n**At will:**\
      \ [Mage Hand](/Compendium/spells/mage-hand-xphb.md) (the hand is Invisible),\
      \ [Minor Illusion](/Compendium/spells/minor-illusion-xphb.md)\n\n**2/day:**\
      \ [Mind Spike](/Compendium/spells/mind-spike-xphb.md)"
    "name": "Spellcasting"
"reactions":
  - "desc": "The quaggoth casts [Feather Fall](/Compendium/spells/feather-fall-xphb.md)\
      \ or [Shield](/Compendium/spells/shield-xphb.md) in response to the spell's\
      \ trigger, requiring no spell components and using the same spellcasting ability\
      \ as Spellcasting.\n"
    "name": "Psionic Defense (3/Day)"
"source":
  - "XMM"
"image": "/Compendium/bestiary/monstrosity/token/quaggoth-thonot-xmm.webp"
```
^statblock

## Environment

underdark
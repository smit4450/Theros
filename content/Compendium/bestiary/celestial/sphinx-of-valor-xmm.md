---
title: Sphinx of Valor
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/17
- monster/environment/desert
- monster/environment/planar
- monster/environment/upper
- monster/size/large
- monster/type/celestial
statblock: inline
aliases: ["Sphinx of Valor"]
---
# Sphinx of Valor
*Source: Monster Manual (2024) p. 294. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/celestial/img/sphinx-of-valor.webp#right|850)  
Sphinxes of valor guard world-changing or dangerous secrets—evidence of weird truths, deadly Artifacts, and things that shouldn't exist. They inhabit hidden, magical sites and hold their duty above mortal life. If threatened, a sphinx of valor defends its charge with its supernaturally empowered roar and fierce strikes.

## Sphinxes

*Collectors and Keepers of Secrets*

- **Habitat.** Desert, Planar (Upper Planes)  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Sphinxes protect the secrets of the multiverse. Formed from the spirits of sages and explorers, sphinxes know the power of truth and the importance of preserving it. They share their wisdom only with those who prove themselves wise or overcome tests of worthiness, such as riddles or battles with dangerous beasts. Through their existences, sphinxes might change form as they gain more nuanced understanding of cosmic enigmas.

### Sphinx Lairs

Sphinxes typically dwell in places that hold great knowledge or prophetic magic.

> [!quote]  
> 
> Round she is, yet flat as a board
> 
> Altar of the Lupine Lords
> 
> Jewel on black velvet, pearl in the sea
> 
> Unchanged but e'erchanging eternally

> [!note]
> Answer to the riddle of White Plume Mountain: The Moon.
![](Compendium/bestiary/celestial/img/sphinxes.webp#center)  
## Statblock

```statblock
"name": "Sphinx of Valor (XMM)"
"size": "Large"
"type": "celestial"
"alignment": "Lawful Neutral"
"ac": !!int "17"
"hp": !!int "199"
"hit_dice": "19d10 + 95"
"modifier": !!int "12"
"stats":
  - !!int "22"
  - !!int "10"
  - !!int "20"
  - !!int "16"
  - !!int "23"
  - !!int "18"
"speed": "40 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "6"
  - "constitution": !!int "11"
  - "intelligence": !!int "9"
  - "wisdom": !!int "12"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+12"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+15"
"damage_resistances": "necrotic, radiant"
"damage_immunities": "psychic"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception\
  \ 22"
"languages": "Celestial, Common"
"cr": "17"
"traits":
  - "desc": "No magic can observe the sphinx remotely or detect its thoughts without\
      \ its permission. Wisdom ([[skills#Insight|Insight]]) checks\
      \ made to ascertain its intentions or sincerity are made with [[disadvantage-xphb|Disadvantage]]."
    "name": "Inscrutable"
  - "desc": "If the sphinx fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day, or 4/Day in Lair)"
"actions":
  - "desc": "The sphinx makes two Claw attacks and uses Roar."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +12, reach 5 ft. *Hit:* 20 (4d6 + 6) Slashing\
      \ damage."
    "name": "Claw"
  - "desc": "The sphinx emits a magical roar. Whenever it roars, the roar has a different\
      \ effect, as detailed below (the sequence resets when it takes a [[long-rest-xphb|Long Rest]]):\n\
      \n- **First Roar.** *Wisdom Saving Throw:* DC 20, each enemy in a 500-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the sphinx. *Failure:* The target has the [[conditions#Frightened|Frightened]]\
      \ condition for 1 minute.  \n- **Second Roar.** *Wisdom Saving Throw:* DC 20,\
      \ each enemy in a 500-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the sphinx. *Failure:* The target has the [[conditions#Paralyzed|Paralyzed]]\
      \ condition, and it repeats the save at the end of each of its turns, ending\
      \ the effect on itself on a success. After 1 minute, it succeeds automatically.\
      \  \n- **Third Roar.** *Constitution Saving Throw:* DC 20, each enemy in a 500-foot\
      \ [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the sphinx. *Failure:* 44 (8d10) Thunder damage, and the\
      \ target has the [[conditions#Prone|Prone]] condition. *Success:*\
      \ Half damage only.  "
    "name": "Roar (3/Day)"
  - "desc": "The sphinx casts one of the following spells, requiring no Material components\
      \ and using Wisdom as the spellcasting ability (spell save DC 20):\n\n**At will:**\
      \ [[detect-evil-and-good-xphb|Detect Evil and Good]], [[thaumaturgy-xphb|Thaumaturgy]]\n\
      \n**1/day each:** [[detect-magic-xphb|Detect Magic]], [[dispel-magic-xphb|Dispel\
      \ Magic]], [[greater-restoration-xphb|Greater Restoration]],\
      \ [[heroes-feast-xphb|Heroes' Feast]], [[zone-of-truth-xphb|Zone of Truth]]"
    "name": "Spellcasting"
"regional_effects":
  - "desc": "The region containing a sphinx of lore's or sphinx of valor's lair is\
      \ altered by its presence, creating the following effects:\n\n- **Distant Sight.**\
      \ While in its lair, the sphinx can cast [[clairvoyance-xphb|Clairvoyance]],\
      \ requiring no spell components and using the same spellcasting ability as its\
      \ Spellcasting action. When cast this way, the spell's range is 1 mile.  \n\
      - **Infusion of Knowledge.** Whenever the sphinx or one of its allies takes\
      \ a [[actions#Study|Study]] action while within 1 mile of\
      \ the lair, it adds 1d6 to any ability check it makes for that action.  \n\
      \nIf the sphinx dies or moves its lair elsewhere, these effects end immediately."
    "name": ""
"legendary_description": "Legendary Action Uses: 3 (4 in Lair). Immediately after\
  \ another creature's turn, the sphinx of valor can expend a use to take one of the\
  \ following actions. The sphinx of valor regains all expended uses at the start\
  \ of each of its turns."
"legendary_actions":
  - "desc": "The sphinx can teleport up to 30 feet to an unoccupied space it can see,\
      \ and it makes one Claw attack."
    "name": "Arcane Prowl"
  - "desc": "*Constitution Saving Throw:* DC 16, one creature the sphinx can see within\
      \ 120 feet. *Failure:* The target gains 1 [[conditions#Exhaustion|Exhaustion]]\
      \ level. While the target has any [[conditions#Exhaustion|Exhaustion]]\
      \ levels, it appears 3d10 years older. *Failure or Success:* The sphinx can't\
      \ take this action again until the start of its next turn."
    "name": "Weight of Years"
"source":
  - "XMM"
"image": "Compendium/bestiary/celestial/token/sphinx-of-valor-xmm.webp"
```
^statblock
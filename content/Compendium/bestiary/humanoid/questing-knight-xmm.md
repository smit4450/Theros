---
title: Questing Knight
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Questing Knight"]
---
# Questing Knight
*Source: Monster Manual (2024) p. 184*  

![](Compendium/bestiary/humanoid/img/knights.webp#right|850)  
Questing knights travel in pursuit of a cause, such as slaying a villain, defeating a monster, recovering an Artifact, or restoring their lost honor.

## Knights

*Battle Masters and Heroic Wanderers*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

Knights are skilled warriors trained for war and tested in battle. Many serve the rulers of a realm, a religion, or an order devoted to a cause.
## Statblock

```statblock
"name": "Questing Knight (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "18"
"hp": !!int "202"
"hit_dice": "27d8 + 81"
"modifier": !!int "7"
"stats":
  - !!int "20"
  - !!int "16"
  - !!int "16"
  - !!int "11"
  - !!int "12"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "strength": !!int "9"
  - "constitution": !!int "7"
  - "wisdom": !!int "5"
  - "charisma": !!int "8"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+8"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]]"
"senses": "passive Perception 15"
"languages": "Common plus one other language"
"cr": "12"
"traits":
  - "desc": "Creatures of the knight's choice in a 30-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from it have [[immunity-xphb|Immunity]]\
      \ to the [[conditions#Charmed|Charmed]] and [[conditions#Frightened|Frightened]]\
      \ conditions while there."
    "name": "Aura of Bravery"
"actions":
  - "desc": "The knight makes three attacks, using Greatsword or Longbow in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 5 ft. *Hit:* 12 (2d6 + 5) Slashing\
      \ damage plus 22 (5d8) Radiant damage."
    "name": "Greatsword"
  - "desc": "*Ranged Attack Roll:* +7, range 150/600 ft. *Hit:* 12 (2d8 + 3) Piercing\
      \ damage plus 22 (5d8) Radiant damage."
    "name": "Longbow"
  - "desc": "The knight casts one of the following spells, using Charisma as the spellcasting\
      \ ability (spell save DC 16):\n\n**1/day each:** [[daylight-xphb|Daylight]],\
      \ [[dispel-evil-and-good-xphb|Dispel Evil and Good]], [[greater-restoration-xphb|Greater\
      \ Restoration]], [[phantom-steed-xphb|Phantom Steed]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/questing-knight-xmm.webp"
```
^statblock
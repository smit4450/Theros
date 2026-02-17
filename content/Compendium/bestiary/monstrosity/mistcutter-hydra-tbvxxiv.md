---
title: Mistcutter Hydra
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxiv
- monster/cr/29
- monster/size/g
- monster/type/monstrosity
statblock: inline
aliases: ["Mistcutter Hydra"]
---
# Mistcutter Hydra
*Source: Theros Bestiary TBVXXIV*  

The mistcutter hydra has twelve heads and is able to breath underwater.

![Mistcutter Hydra](Compendium/bestiary/monstrosity/img/mistcutter-hydra.webp#right|850)  

```statblock
"name": "Mistcutter Hydra (TBVXXIV)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "1920"
"hit_dice": "120d20 + 720"
"modifier": !!int "0"
"stats":
  - !!int "22"
  - !!int "10"
  - !!int "22"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "40 ft., swim 40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+9"
"damage_immunities": "acid"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "29"
"traits":
  - "desc": "When the hydra takes piercing or slashing damage, each creature within 5 feet of the hydra takes 9 (2d8) acid damage."
    "name": "Acidic Blood"
  - "desc": "The hydra can breathe air and water."
    "name": "Amphibious"
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has twelve heads. While it has more than one head, the hydra has [[advantage-xphb|Advantage]] on saving throws against being [[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]], [[conditions#Deafened|deafened]], [[conditions#Frightened|frightened]], [[conditions#Stunned|stunned]], or knocked [[conditions#Unconscious|unconscious]]. Whenever the hydra takes 550 or more damage in a single turn, one of its heads dies. If all its heads die, the hydra dies. At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 165 [[hit-points-xphb|Hit Points]] for each head regrown in this way."
    "name": "Multiple Heads"
  - "desc": "For each head the hydra has beyond one, it gets an extra reaction that can be used only for opportunity attacks."
    "name": "Reactive Heads"
  - "desc": "The hydra deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "While the hydra sleeps, at least one of its heads is awake."
    "name": "Wakeful"
"actions":
  - "desc": "The hydra makes as many bite attacks as it has heads."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 60 (12d8 + 6) piercing damage."
    "name": "Bite"
"source":
  - "TBVXXIV"
"image": "Compendium/bestiary/monstrosity/token/mistcutter-hydra-tbvxxiv.webp"
```
^statblock
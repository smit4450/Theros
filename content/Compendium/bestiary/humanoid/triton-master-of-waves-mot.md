---
title: Triton Master of Waves
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/triton
statblock: inline
aliases: ["Triton Master of Waves"]
---
# Triton Master of Waves
*Source: Mythic Odysseys of Theros p. 245*  

![](Compendium/bestiary/humanoid/img/triton-master-of-waves.webp#right)  
Triton masters of waves sculpt storms and change the tides, bending the sea to their will. Drawing forth living currents and the icy cold of the deep, these mages make the ocean their ally, using it to defend their people or enact Thassa's wishes. While dire threats from the land might bring them to coastal shallows, most masters of waves keep to the ocean's depths.

Although many masters of waves resent land-dwellers and strike out at those who trespass upon their waters, most are devoted followers of the sea god. Those who share their faith or who bear earnest offerings to Thassa might defuse the tritons' ire—that is, if they survive the deadly winds and waves that typically herald these sea guardians' appearance.

Clever, far-ranging people of the sea, tritons live rich lives unknown to most land-dwelling individuals. While the waves separate most tritons from land-dwellers, occasionally the inhabitants of the surface and the deep come into conflict. In such cases, tritons prove skilled at sabotaging ocean-going vessels, employing water-based magic, and otherwise whipping up the fury of the sea. Few dare insult tritons in their home environment, but those who do and survive often learn that the tritons' wrath doesn't end at the shore.
```statblock
"name": "Triton Master of Waves (MOT)"
"size": "Medium"
"type": "humanoid"
"subtype": "triton"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"modifier": !!int "0"
"stats":
  - !!int "16"
  - !!int "11"
  - !!int "16"
  - !!int "10"
  - !!int "12"
  - !!int "19"
"speed": "30 ft., swim 30 ft."
"saves":
  - "dexterity": !!int "3"
  - "intelligence": !!int "3"
  - "charisma": !!int "7"
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+6"
  - "name": "[Nature](Compendium/rules/skills.md#Nature)"
    "desc": "+6"
  - "name": "[Survival](Compendium/rules/skills.md#Survival)"
    "desc": "+4"
"damage_resistances": "cold, fire"
"senses": "[darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 11"
"languages": "Common, Primordial"
"cr": "8"
"traits":
  - "desc": "The triton's spellcasting ability is Charisma (spell save DC 15, +7\
      \ to hit with spell attacks). It can innately cast the following spells, requiring\
      \ no material components:\n\n**At will:** [ray of frost](Compendium/spells/ray-of-frost-xphb.md)\
      \ (see \"Actions\" below)\n\n**2/day:** [cone of cold](Compendium/spells/cone-of-cold-xphb.md)\n\
      \n**1/day each:** [fog cloud](Compendium/spells/fog-cloud-xphb.md), [gust of\
      \ wind](Compendium/spells/gust-of-wind-xphb.md), [wind wall](Compendium/spells/wind-wall-xphb.md)"
    "name": "Innate Spellcasting"
  - "desc": "The triton can breathe air and water."
    "name": "Amphibious"
  - "desc": "As a bonus action, the triton magically summons 1d4 [water weirds](Compendium/bestiary/elemental/water-weird-xmm.md).\
      \ The summoned weirds appear in unoccupied spaces in water within 60 feet of\
      \ the triton. The water weirds act immediately after the triton on the same\
      \ initiative count and fight until they're destroyed. They disappear if the\
      \ triton dies."
    "name": "Summon Water Weird (Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The triton makes two attacks using Wave Touch and casts [ray of frost](Compendium/spells/ray-of-frost-xphb.md)."
    "name": "Multiattack"
  - "desc": "*Melee Spell Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 22\
      \ (4d10) cold damage."
    "name": "Wave Touch"
  - "desc": "*Ranged Spell Attack:* +7 to hit, range 60 ft., one creature. *Hit:*\
      \ 13 (3d8) cold damage, and the target's speed is reduced by 10 feet until\
      \ the start of the triton's next turn."
    "name": "Ray of Frost (Cantrip)"
"reactions":
  - "desc": "When a creature the triton can see targets the triton with an attack,\
      \ the triton gains 10 temporary hit points. If the attack hits and reduces the\
      \ temporary hit points to 0, each creature within 5 feet of the triton takes\
      \ 9 (2d8) cold damage."
    "name": "Frigid Shield"
"source":
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/triton-master-of-waves-mot.webp"
```
^statblock
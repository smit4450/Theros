---
title: Swarm of Piranhas
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Piranhas"]
---
# Swarm of Piranhas
*Source: Monster Manual (2024) p. 370. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/swarm-of-piranhas.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Swarm of Piranhas (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "28"
"hit_dice": "8d8 - 8"
"modifier": !!int "3"
"stats":
  - !!int "13"
  - !!int "16"
  - !!int "9"
  - !!int "1"
  - !!int "7"
  - !!int "2"
"speed": "5 ft., swim 40 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](Compendium/rules/conditions.md#Petrified), [prone](Compendium/rules/conditions.md#Prone),\
  \ [restrained](Compendium/rules/conditions.md#Restrained), [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "1"
"traits":
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny piranha. The swarm\
      \ can't regain [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or gain [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
    "name": "Swarm"
  - "desc": "The swarm can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +5 (with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
      \ if the target doesn't have all its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)),\
      \ reach 5 ft. *Hit:* 8 (2d4 + 3) Piercing damage, or 5 (1d4 + 3) Piercing\
      \ damage if the swarm is [Bloodied](Compendium/rules/conditions.md#Bloodied)."
    "name": "Bites"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/swarm-of-piranhas-xmm.webp"
```
^statblock
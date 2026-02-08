---
title: Swarm of Insects
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Insects"]
---
# Swarm of Insects
*Source: Monster Manual (2024) p. 370. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/swarm-of-insects.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Swarm of Insects (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "19"
"hit_dice": "3d8 + 6"
"modifier": !!int "1"
"stats":
  - !!int "3"
  - !!int "13"
  - !!int "14"
  - !!int "1"
  - !!int "7"
  - !!int "1"
"speed": "20 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](Compendium/rules/conditions.md#Petrified), [prone](Compendium/rules/conditions.md#Prone),\
  \ [restrained](Compendium/rules/conditions.md#Restrained), [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "If the swarm has a [Climb Speed](Compendium/rules/variant-rules/climb-speed-xphb.md),\
      \ the swarm can climb difficult surfaces, including along ceilings, without\
      \ needing to make an ability check."
    "name": "Spider Climb"
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny insect. The swarm\
      \ can't regain [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or gain [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 6 (2d4 + 1) Poison damage,\
      \ or 3 (1d4 + 1) Poison damage if the swarm is [Bloodied](Compendium/rules/conditions.md#Bloodied)."
    "name": "Bites"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/swarm-of-insects-xmm.webp"
```
^statblock
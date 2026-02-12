---
title: Swarm of Bats
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Bats"]
---
# Swarm of Bats
*Source: Monster Manual (2024) p. 370. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/swarm-of-bats.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Swarm of Bats (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "11"
"hit_dice": "2d10"
"modifier": !!int "2"
"stats":
  - !!int "5"
  - !!int "15"
  - !!int "10"
  - !!int "2"
  - !!int "12"
  - !!int "4"
"speed": "5 ft., fly 30 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](Compendium/rules/conditions.md#Petrified), [prone](Compendium/rules/conditions.md#Prone),\
  \ [restrained](Compendium/rules/conditions.md#Restrained), [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 60 ft., passive Perception\
  \ 11"
"languages": ""
"cr": "1/4"
"traits":
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny bat. The swarm\
      \ can't regain [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or gain [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (2d4) Piercing damage,\
      \ or 2 (1d4) Piercing damage if the swarm is [Bloodied](Compendium/rules/conditions.md#Bloodied)."
    "name": "Bites"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/swarm-of-bats-xmm.webp"
```
^statblock
---
title: Swarm of Venomous Snakes
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Venomous Snakes"]
---
# Swarm of Venomous Snakes
*Source: Monster Manual (2024) p. 371. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/swarm-of-venomous-snakes.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Swarm of Venomous Snakes (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "36"
"hit_dice": "8d8"
"modifier": !!int "4"
"stats":
  - !!int "8"
  - !!int "18"
  - !!int "11"
  - !!int "1"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Grappled|grappled]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Petrified|petrified]], [[conditions#Prone|prone]],\
  \ [[conditions#Restrained|restrained]], [[conditions#Stunned|stunned]]"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny snake. The swarm\
      \ can't regain [[hit-points-xphb|Hit Points]]\
      \ or gain [[temporary-hit-points-xphb|Temporary Hit Points]]."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 8 (1d8 + 4) Piercing\
      \ damage—or 6 (1d4 + 4) Piercing damage if the swarm is [[conditions#Bloodied|Bloodied]]—\
      plus 10 (3d6) Poison damage."
    "name": "Bites"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/swarm-of-venomous-snakes-xmm.webp"
```
^statblock
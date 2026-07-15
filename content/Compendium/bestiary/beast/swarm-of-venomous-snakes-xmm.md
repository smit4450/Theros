---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/2
- monster/environment/coastal
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/swamp
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Swarm of Venomous Snakes"
---
# Swarm of Venomous Snakes
*Source: Monster Manual (2024) p. 371. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/swarm-of-venomous-snakes.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Swarm of Venomous Snakes"
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
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [frightened](/Compendium/rules/conditions.md#Frightened),\
  \ [grappled](/Compendium/rules/conditions.md#Grappled), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](/Compendium/rules/conditions.md#Petrified), [prone](/Compendium/rules/conditions.md#Prone),\
  \ [restrained](/Compendium/rules/conditions.md#Restrained), [stunned](/Compendium/rules/conditions.md#Stunned)"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny snake. The swarm\
      \ can't regain [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or gain [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 8 (1d8 + 4) Piercing damage—\
      or 6 (1d4 + 4) Piercing damage if the swarm is [Bloodied](/Compendium/rules/conditions.md#Bloodied)—\
      plus 10 (3d6) Poison damage."
    "name": "Bites"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/swarm-of-venomous-snakes-xmm.webp"
```
^statblock

## Environment

coastal, desert, forest, grassland, hill, swamp
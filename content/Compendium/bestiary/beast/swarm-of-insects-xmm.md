---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/swamp
- monster/environment/underdark
- monster/environment/urban
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Swarm of Insects"
---
# Swarm of Insects
*Source: Monster Manual (2024) p. 370. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/swarm-of-insects.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Swarm of Insects"
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
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [frightened](/Compendium/rules/conditions.md#Frightened),\
  \ [grappled](/Compendium/rules/conditions.md#Grappled), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](/Compendium/rules/conditions.md#Petrified), [prone](/Compendium/rules/conditions.md#Prone),\
  \ [restrained](/Compendium/rules/conditions.md#Restrained), [stunned](/Compendium/rules/conditions.md#Stunned)"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "If the swarm has a [Climb Speed](/Compendium/rules/variant-rules/climb-speed-xphb.md),\
      \ the swarm can climb difficult surfaces, including along ceilings, without\
      \ needing to make an ability check."
    "name": "Spider Climb"
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny insect. The swarm\
      \ can't regain [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or gain [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 6 (2d4 + 1) Poison damage,\
      \ or 3 (1d4 + 1) Poison damage if the swarm is [Bloodied](/Compendium/rules/conditions.md#Bloodied)."
    "name": "Bites"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/swarm-of-insects-xmm.webp"
```
^statblock

## Environment

desert, forest, grassland, hill, swamp, underdark, urban
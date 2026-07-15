---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/forest
- monster/environment/swamp
- monster/environment/underdark
- monster/environment/urban
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Swarm of Rats"
---
# Swarm of Rats
*Source: Monster Manual (2024) p. 370. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/rats.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Swarm of Rats"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "14"
"hit_dice": "4d8 - 4"
"modifier": !!int "0"
"stats":
  - !!int "9"
  - !!int "11"
  - !!int "9"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., climb 30 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [frightened](/Compendium/rules/conditions.md#Frightened),\
  \ [grappled](/Compendium/rules/conditions.md#Grappled), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](/Compendium/rules/conditions.md#Petrified), [prone](/Compendium/rules/conditions.md#Prone),\
  \ [restrained](/Compendium/rules/conditions.md#Restrained), [stunned](/Compendium/rules/conditions.md#Stunned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 30 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "1/4"
"traits":
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny rat. The swarm\
      \ can't regain [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or gain [Temporary Hit Points](/Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 5 (2d4) Piercing damage,\
      \ or 2 (1d4) Piercing damage if the swarm is [Bloodied](/Compendium/rules/conditions.md#Bloodied)."
    "name": "Bites"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/swarm-of-rats-xmm.webp"
```
^statblock

## Environment

forest, swamp, underdark, urban
---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/desert
- monster/environment/forest
- monster/environment/swamp
- monster/environment/underwater
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Constrictor Snake"
---
# Constrictor Snake
*Source: Monster Manual (2024) p. 351, Player's Handbook (2024) p. 348. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/constrictor-snake.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Constrictor Snake"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "13"
"hit_dice": "2d10 + 2"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "12"
  - !!int "1"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "1/4"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 6 (1d8 + 2) Piercing damage."
    "name": "Bite"
  - "desc": "*Strength Saving Throw:* DC 12, one Medium or smaller creature the snake\
      \ can see within 5 feet. *Failure:* 7 (3d4) Bludgeoning damage, and the target\
      \ has the [Grappled](/Compendium/rules/conditions.md#Grappled) condition (escape\
      \ DC 12)."
    "name": "Constrict"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/constrictor-snake-xmm.webp"
```
^statblock

## Environment

desert, forest, swamp, underwater
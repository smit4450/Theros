---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/2
- monster/environment/desert
- monster/environment/forest
- monster/environment/swamp
- monster/environment/underwater
- monster/size/huge
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Constrictor Snake"
---
# Giant Constrictor Snake
*Source: Monster Manual (2024) p. 355. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/constrictor-snake.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Constrictor Snake"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "60"
"hit_dice": "8d12 + 8"
"modifier": !!int "2"
"stats":
  - !!int "19"
  - !!int "14"
  - !!int "12"
  - !!int "1"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "2"
"actions":
  - "desc": "The snake makes one Bite attack and uses Constrict."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 10 ft. *Hit:* 11 (2d6 + 4) Piercing damage."
    "name": "Bite"
  - "desc": "*Strength Saving Throw:* DC 14, one Large or smaller creature the snake\
      \ can see within 10 feet. *Failure:* 13 (2d8 + 4) Bludgeoning damage, and the\
      \ target has the [Grappled](/Compendium/rules/conditions.md#Grappled) condition\
      \ (escape DC 14)."
    "name": "Constrict"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/giant-constrictor-snake-xmm.webp"
```
^statblock

## Environment

desert, forest, swamp, underwater
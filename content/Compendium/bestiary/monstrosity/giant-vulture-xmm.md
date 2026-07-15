---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1
- monster/environment/desert
- monster/environment/grassland
- monster/environment/hill
- monster/size/large
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Vulture"
---
# Giant Vulture
*Source: Monster Manual (2024) p. 361. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/vulture.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Vulture"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "10"
"hp": !!int "25"
"hit_dice": "3d10 + 9"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "16"
  - !!int "6"
  - !!int "12"
  - !!int "7"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"damage_resistances": "necrotic"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": "understands Common but can't speak"
"cr": "1"
"traits":
  - "desc": "The vulture has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on an attack roll against a creature if at least one of the vulture's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition."
    "name": "Pack Tactics"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 9 (2d6 + 2) Piercing damage,\
      \ and the target has the [Poisoned](/Compendium/rules/conditions.md#Poisoned)\
      \ condition until the end of its next turn."
    "name": "Gouge"
"source":
  - "XMM"
"image": "/Compendium/bestiary/monstrosity/token/giant-vulture-xmm.webp"
```
^statblock

## Environment

desert, grassland, hill
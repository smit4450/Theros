---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/2
- monster/environment/arctic
- monster/environment/hill
- monster/environment/mountain
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Saber-Toothed Tiger"
---
# Saber-Toothed Tiger
*Source: Monster Manual (2024) p. 369. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/saber-toothed-tiger.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Saber-Toothed Tiger"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "52"
"hit_dice": "7d10 + 14"
"modifier": !!int "3"
"stats":
  - !!int "18"
  - !!int "17"
  - !!int "15"
  - !!int "3"
  - !!int "12"
  - !!int "8"
"speed": "40 ft."
"saves":
  - "strength": !!int "6"
  - "dexterity": !!int "5"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+5"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 15"
"languages": ""
"cr": "2"
"traits":
  - "desc": "With a 10-foot running start, the tiger can [Long Jump](/Compendium/rules/variant-rules/long-jump-xphb.md)\
      \ up to 25 feet."
    "name": "Running Leap"
"actions":
  - "desc": "The tiger makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 11 (2d6 + 4) Slashing damage."
    "name": "Rend"
"bonus_actions":
  - "desc": "The tiger takes the [Disengage](/Compendium/rules/actions.md#Disengage)\
      \ or [Hide](/Compendium/rules/actions.md#Hide) action."
    "name": "Nimble Escape"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/saber-toothed-tiger-xmm.webp"
```
^statblock

## Environment

arctic, hill, mountain
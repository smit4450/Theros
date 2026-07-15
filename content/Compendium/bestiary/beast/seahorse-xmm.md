---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/0
- monster/environment/underwater
- monster/size/tiny
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Seahorse"
---
# Seahorse
*Source: Monster Manual (2024) p. 369. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/seahorse.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Seahorse"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "1"
"hit_dice": "1d4 - 1"
"modifier": !!int "1"
"stats":
  - !!int "1"
  - !!int "12"
  - !!int "8"
  - !!int "1"
  - !!int "10"
  - !!int "2"
"speed": "5 ft., swim 20 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 12"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The seahorse can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "While underwater, the seahorse moves up to its [Swim Speed](/Compendium/rules/variant-rules/swim-speed-xphb.md)\
      \ without provoking [Opportunity Attacks](/Compendium/rules/actions.md#Opportunity%20Attack)."
    "name": "Bubble Dash"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/seahorse-xmm.webp"
```
^statblock

## Environment

underwater
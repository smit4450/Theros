---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/underwater
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Seahorse"
---
# Giant Seahorse
*Source: Monster Manual (2024) p. 359, Player's Handbook (2024) p. 350. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/seahorse.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Seahorse"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "16"
"hit_dice": "3d10"
"modifier": !!int "1"
"stats":
  - !!int "15"
  - !!int "12"
  - !!int "11"
  - !!int "2"
  - !!int "12"
  - !!int "5"
"speed": "5 ft., swim 40 ft."
"senses": "passive Perception 11"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The seahorse can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 9 (2d6 + 2) Bludgeoning damage,\
      \ or 11 (2d8 + 2) Bludgeoning damage if the seahorse moved 20+ feet straight\
      \ toward the target immediately before the hit."
    "name": "Ram"
"bonus_actions":
  - "desc": "While underwater, the seahorse moves up to half its [Swim Speed](/Compendium/rules/variant-rules/swim-speed-xphb.md)\
      \ without provoking [Opportunity Attacks](/Compendium/rules/actions.md#Opportunity%20Attack)."
    "name": "Bubble Dash"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/giant-seahorse-xmm.webp"
```
^statblock

## Environment

underwater
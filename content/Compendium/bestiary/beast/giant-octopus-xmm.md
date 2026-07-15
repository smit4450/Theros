---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1
- monster/environment/underwater
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Octopus"
---
# Giant Octopus
*Source: Monster Manual (2024) p. 358. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/octopus.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Octopus"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "45"
"hit_dice": "7d10 + 7"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "13"
  - !!int "13"
  - !!int "5"
  - !!int "10"
  - !!int "4"
"speed": "10 ft., swim 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 14"
"languages": ""
"cr": "1"
"traits":
  - "desc": "The octopus can breathe only underwater. It can hold its breath for 1\
      \ hour outside water."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 10 ft. *Hit:* 10 (2d6 + 3) Bludgeoning\
      \ damage. If the target is a Medium or smaller creature, it has the [Grappled](/Compendium/rules/conditions.md#Grappled)\
      \ condition (escape DC 13) from all eight tentacles. While [Grappled](/Compendium/rules/conditions.md#Grappled),\
      \ the target has the [Restrained](/Compendium/rules/conditions.md#Restrained)\
      \ condition."
    "name": "Tentacles"
"reactions":
  - "desc": "Trigger: The octopus takes damage while underwater. _Response:_ The octopus\
      \ releases ink that fills a 10-foot [Cube](/Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
      \ centered on itself, and the octopus moves up to its [Swim Speed](/Compendium/rules/variant-rules/swim-speed-xphb.md).\
      \ The [Cube](/Compendium/rules/variant-rules/cube-area-of-effect-xphb.md) is\
      \ [Heavily Obscured](/Compendium/rules/variant-rules/heavily-obscured-xphb.md)\
      \ for 1 minute or until a strong current or similar effect disperses the ink."
    "name": "Ink Cloud (1/Day)"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/giant-octopus-xmm.webp"
```
^statblock

## Environment

underwater
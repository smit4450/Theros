---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/4
- monster/environment/grassland
- monster/size/huge
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Elephant"
---
# Elephant
*Source: Monster Manual (2024) p. 353, Player's Handbook (2024) p. 349. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/elephant.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Elephant"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "76"
"hit_dice": "8d12 + 24"
"modifier": !!int "-1"
"stats":
  - !!int "22"
  - !!int "9"
  - !!int "17"
  - !!int "3"
  - !!int "11"
  - !!int "6"
"speed": "40 ft."
"senses": "passive Perception 10"
"languages": ""
"cr": "4"
"actions":
  - "desc": "The elephant makes two Gore attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +8, reach 5 ft. *Hit:* 15 (2d8 + 6) Piercing damage.\
      \ If the target is a Huge or smaller creature and the elephant moved 20+ feet\
      \ straight toward it immediately before the hit, the target has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Gore"
"bonus_actions":
  - "desc": "*Dexterity Saving Throw:* DC 16, one creature within 5 feet that has\
      \ the [Prone](/Compendium/rules/conditions.md#Prone) condition. *Failure:* 17\
      \ (2d10 + 6) Bludgeoning damage. *Success:* Half damage."
    "name": "Trample"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/elephant-xmm.webp"
```
^statblock

## Environment

grassland
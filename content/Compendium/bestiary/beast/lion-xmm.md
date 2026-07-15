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
- monster/environment/mountain
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Lion"
---
# Lion
*Source: Monster Manual (2024) p. 364, Player's Handbook (2024) p. 352. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/lion.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Lion"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "4d10"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "11"
  - !!int "3"
  - !!int "12"
  - !!int "8"
"speed": "50 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "1"
"traits":
  - "desc": "The lion has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on an attack roll against a creature if at least one of the lion's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition."
    "name": "Pack Tactics"
  - "desc": "With a 10-foot running start, the lion can [Long Jump](/Compendium/rules/variant-rules/long-jump-xphb.md)\
      \ up to 25 feet."
    "name": "Running Leap"
"actions":
  - "desc": "The lion makes two Rend attacks. It can replace one attack with a use\
      \ of Roar."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Slashing damage."
    "name": "Rend"
  - "desc": "*Wisdom Saving Throw:* DC 11, one creature within 15 feet. *Failure:*\
      \ The target has the [Frightened](/Compendium/rules/conditions.md#Frightened)\
      \ condition until the start of the lion's next turn."
    "name": "Roar"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/lion-xmm.webp"
```
^statblock

## Environment

desert, grassland, hill, mountain
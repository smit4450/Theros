---
title: Seahorse
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Seahorse"]
---
# Seahorse
*Source: Monster Manual (2024) p. 369. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/seahorse.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Seahorse (XMM)"
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
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 12"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The seahorse can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "While underwater, the seahorse moves up to its [Swim Speed](Compendium/rules/variant-rules/swim-speed-xphb.md)\
      \ without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack)."
    "name": "Bubble Dash"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/seahorse-xmm.webp"
```
^statblock
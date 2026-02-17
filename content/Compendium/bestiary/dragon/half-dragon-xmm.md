---
title: Half-Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/5
- monster/environment/any
- monster/size/medium
- monster/type/dragon
statblock: inline
aliases: ["Half-Dragon"]
---
# Half-Dragon
*Source: Monster Manual (2024) p. 163. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/half-dragon.webp#right|850)  
## Half-Dragon

*Warrior Created by Dragons*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Born through magical rites involving the essences of dragons, half-dragons serve their creators and their own draconic whims. Most half-dragons are created by chromatic dragons who desire servants with some trace of their own might and grandeur. Half-dragons frequently command other servants of a villainous dragon or act as agents in lands where their draconic master would attract unwanted attention.

Half-dragons share personality traits and agendas with the dragon who spawned them. Those resembling chromatic dragons typically loathe their creator even as they seek the same ends. Half-dragons with the traits of metallic dragons are especially rare, but they might arise through magical accidents, the efforts of reckless magic-users, or the last act of a dying dragon.

> [!quote] A quote from Wyrmlord Azarr Kul, Half–Dragon  
> 
> What blessing demands more yet inspires greater works than the blood of Tiamat?

```statblock
"name": "Half-Dragon (XMM)"
"size": "Medium"
"type": "dragon"
"alignment": "Neutral"
"ac": !!int "18"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"modifier": !!int "5"
"stats":
  - !!int "19"
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "15"
  - !!int "14"
"speed": "40 ft."
"saves":
  - "dexterity": !!int "5"
  - "wisdom": !!int "5"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+7"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"damage_resistances": "Damage type chosen for the Draconic Origin trait below"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., [[senses#Darkvision|Darkvision]]\
  \ 60 ft., passive Perception 15"
"languages": "Common, Draconic"
"cr": "5"
"traits":
  - "desc": "The half-dragon is related to a type of dragon associated with one of\
      \ the following damage types (DM's choice): Acid, Cold, Fire, Lightning, or\
      \ Poison. This choice affects other aspects of the stat block."
    "name": "Draconic Origin"
"actions":
  - "desc": "The half-dragon makes two Claw attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 6 (1d4 + 4) Slashing\
      \ damage plus 7 (2d6) damage of the type chosen for the Draconic Origin trait."
    "name": "Claw"
  - "desc": "*Dexterity Saving Throw:* DC 14, each creature in a 30-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 28 (8d6) damage of the type chosen for the Draconic Origin trait.\
      \ *Success:* Half damage."
    "name": "Dragon's Breath (Recharge 5-6)"
"bonus_actions":
  - "desc": "The half-dragon jumps up to 30 feet by spending 10 feet of movement."
    "name": "Leap"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/half-dragon-xmm.webp"
```
^statblock
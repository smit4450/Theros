---
title: Phylaskia
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/9
- monster/size/large
- monster/type/undead
statblock: inline
aliases: ["Phylaskia"]
---
# Phylaskia
*Source: Mythic Odysseys of Theros p. 239*  

![](Compendium/bestiary/undead/img/phylaskia.webp#right|850)  
These armored skeletal spirits guard the borders of the Underworld and its various wards. Sleepless and merciless, they scrutinize all who would pass, and they slay those who defy them.
```statblock
"name": "Phylaskia (MOT)"
"size": "Large"
"type": "undead"
"alignment": "Lawful Neutral"
"ac": !!int "18"
"ac_class": "[[plate-armor-xphb|plate]]"
"hp": !!int "104"
"hit_dice": "11d10 + 44"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "15"
  - !!int "18"
  - !!int "10"
  - !!int "16"
  - !!int "14"
"speed": "40 ft."
"saves":
  - "constitution": !!int "8"
  - "wisdom": !!int "7"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+7"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+7"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]],\
  \ [[conditions#Deafened|deafened]], [[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Truesight|truesight]] 120 ft., passive Perception\
  \ 17"
"languages": "all"
"cr": "9"
"traits":
  - "desc": "Any creature that starts its turn within 10 feet of the phylaskia must\
      \ make a DC 15 Wisdom saving throw. On a successful save, the creature is immune\
      \ to this aura for the next 24 hours. On a failed save, the creature has disadvantage\
      \ on saving throws and its speed is halved until the start of its next turn."
    "name": "Gatekeeper's Aura"
  - "desc": "If damage reduces the phylaskia to 0 hit points, it must make a Constitution\
      \ saving throw with a DC equal to 5 + the damage taken, unless the damage is\
      \ radiant or from a critical hit. On a success, the phylaskia drops to 1 hit\
      \ point instead."
    "name": "Undead Fortitude"
  - "desc": "The phylaskia can't be [[conditions#Surprised|surprised]]."
    "name": "Vigilant"
"actions":
  - "desc": "The phylaskia makes two longsword attacks and uses its Strength Drain\
      \ once."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +9 to hit, reach 10 ft., one target. *Hit:*\
      \ 14 (2d8 + 5) slashing damage, or 16 (2d10 + 5) slashing damage if used\
      \ with two hands, plus 11 (2d10) necrotic damage."
    "name": "Longsword"
  - "desc": "*Melee Weapon Attack:* +9 to hit, reach 5 ft., one creature. *Hit:*\
      \ 12 (2d6 + 5) necrotic damage. Unless the target is immune to necrotic damage,\
      \ its Strength score is reduced by 1d4. The target dies if this reduces its\
      \ Strength to 0. Otherwise, the reduction lasts until the target finishes a\
      \ short or long rest."
    "name": "Strength Drain"
"source":
  - "MOT"
"image": "Compendium/bestiary/undead/token/phylaskia-mot.webp"
```
^statblock
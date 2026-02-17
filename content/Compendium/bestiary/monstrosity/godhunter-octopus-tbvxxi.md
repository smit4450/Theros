---
title: Godhunter Octopus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxi
- monster/cr/23
- monster/size/g
- monster/type/monstrosity
statblock: inline
aliases: ["Godhunter Octopus"]
---
# Godhunter Octopus
*Source: Theros Bestiary TBVXXI*  

<blockquote><small>“I will match Thassa drop for drop and show a god what true power is.”

—Kiora</small></blockquote>The godhunter octopus feeds on magic. It possesses olfactory senses that can discern various types of magic that aid in its hunt.

![Godhunter Octopus](https://img.scryfall.com/cards/art_crop/front/d/a/da106c23-fd1c-461b-9301-159f93ef489b.jpg?1593095444#right)  

```statblock
"name": "Godhunter Octopus (TBVXXI)"
"size": "Gargantuan"
"type": "monstrosity"
"subtype": "octopus"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "13"
  - !!int "20"
  - !!int "6"
  - !!int "12"
  - !!int "6"
"speed": "10 ft., swim 60 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+8"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+8"
"senses": "arcane smell, [[senses#Blindsight|Blindsight]] 0 ft. (can't see beyond this radius), passive Perception 10"
"languages": ""
"cr": "23"
"traits":
  - "desc": "The octopus can smell magic and discern precise details about the magic it smells. It has [[advantage-xphb|Advantage]] on Wisdom (perception) checks that rely on smelling magic."
    "name": "Keen Arcane Smell"
  - "desc": "The octopus deals double damage to creatures that are spells and to creatures under spells."
    "name": "Godhunter"
  - "desc": "The octopus has [[advantage-xphb|Advantage]] on Dexterity (Stealth) checks made while underwater."
    "name": "Underwater Camouflage"
  - "desc": "The octopus can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "The monster makes three attacks: one attack with its arms and two with its bite."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 40 (10d6 + 5) bludgeoning damage. If the target is a creature, it is [[conditions#Grappled|grappled]] (escape DC 16) and brought within 5 ft. of the octopus's mouth. Until this grapple ends, the target is [[conditions#Restrained|restrained]], and the octopus can't use its arms on another target."
    "name": "Arms"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target [[conditions#Grappled|grappled]] by the octopus's arms. Hit: 40 (10d6 + 5) piercing damage."
    "name": "Bite"
  - "desc": "A 40-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action."
    "name": "Ink Cloud (Recharges after a Short or Long Rest)"
"source":
  - "TBVXXI"
"image": "Compendium/bestiary/monstrosity/token/godhunter-octopus-tbvxxi.webp"
```
^statblock
---
title: Sealock Monster
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxi
- monster/cr/6
- monster/size/l
- monster/type/beast
statblock: inline
aliases: ["Sealock Monster"]
---
# Sealock Monster
*Source: Theros Bestiary TBVXXI*  

The largest monsters of the seas are confined to sealocks by the tritons. However, sailors are free to enter these sealocks.

![Sealock Monster](Homebrew/bestiary/beast/img/sealock-monster.webp#right)  

```statblock
"name": "Sealock Monster (TBVXXI)"
"size": "Large"
"type": "beast"
"subtype": "octopus"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "210"
"hit_dice": "21d10 + 105"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "13"
  - !!int "20"
  - !!int "4"
  - !!int "10"
  - !!int "4"
"speed": "10 ft., swim 60 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "6"
"traits":
  - "desc": "While out of water, the monster can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The monster has [[advantage-xphb|Advantage]] on Dexterity (Stealth) checks made while underwater."
    "name": "Underwater Camouflage"
  - "desc": "The monster can breathe only underwater."
    "name": "Water Breathing"
  - "desc": "When the monster is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, the damage creates tears in its skin, revealing its hearts. The monster has three hearts in its cephalothorax. A heart has an AC of 11 and 40 [[hit-points-xphb|Hit Points]]. It is immune to all conditions. If it is forced to make a saving throw, treat its ability scores as 10 (+0). If it finishes a short or long rest, the skin heals, any destroyed hearts regenerate, and the hearts are covered again. The monster dies when all the hearts are destroyed."
    "name": "Hearts of the Monster (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The monster makes two attacks: one attack with its tentacles and one with its bite."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 15 ft., one target. Hit: 12 (2d6 + 5) bludgeoning damage. If the target is a creature, it is [[conditions#Grappled|grappled]] (escape DC 16) and brought within 5 ft. of the monster's mouth. Until this grapple ends, the target is [[conditions#Restrained|restrained]], and the monster can't use its tentacles on another target."
    "name": "Tentacles"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target [[conditions#Grappled|grappled]] by the monster's tentacles. Hit: 12 (2d6 + 5) piercing damage."
    "name": "Bite"
  - "desc": "A 20-foot-radius cloud of ink extends all around the monster if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the monster can use the Dash action as a bonus action."
    "name": "Ink Cloud (Recharges after a Short or Long Rest)"
"legendary_actions":
  - "desc": "**Mythic Actions**If Tromokratis’s mythic trait is active, it can use the options below as legendary actions for 1 hour after using Hearts of the Octopus. **_Flood._** The monster splashes water from the sea, causing the water level of all standing water in a 100-foot cube area around it to rise by as much as 20 feet. If the area includes a shore, the flooding water spills over onto dry land. If the monster isn't near land, it instead creates a 20-foot tall wave that travels from one side of the area to the other and then crashes down. Any Huge or smaller vehicles in the wave’s path are carried with it to the other side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance of capsizing. Water that doesn't run off the land back into the sea gradually disappears over the course of 2 weeks."
    "name": ""
"source":
  - "TBVXXI"
"image": "Homebrew/bestiary/beast/token/sealock-monster-tbvxxi.webp"
```
^statblock
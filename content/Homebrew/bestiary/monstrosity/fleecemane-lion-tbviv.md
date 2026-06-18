---
title: Fleecemane Lion
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviv
- monster/cr/4
- monster/size/l
- monster/type/monstrosity
statblock: inline
aliases: ["Fleecemane Lion"]
---
# Fleecemane Lion
*Source: Theros Bestiary TBVIV*  

The fleecemane lion is virtually indestructible. However, it does have a weakness: an olive wood stake.

![Fleecemane Lion](https://media.dndbeyond.com/compendium-images/moot/ds6d2NLXmv1wnY8q/06-16.png#right)  

```statblock
"name": "Fleecemane Lion (TBVIV)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d10 + 6"
"modifier": !!int "3"
"stats":
  - !!int "19"
  - !!int "16"
  - !!int "14"
  - !!int "6"
  - !!int "14"
  - !!int "10"
"speed": "50 ft."
"saves":
  - "strength": !!int "6"
  - "constitution": !!int "4"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": ""
"cr": "4"
"traits":
  - "desc": "The lion has [[advantage-xphb|Advantage]] on Wisdom (Perception) checks that rely on smell."
    "name": "Keen Smell"
  - "desc": "If the lion takes piercing damage from a stake made of olive wood, the lion loses its lion's blessing and (if it had it) its indestructibility."
    "name": "Olive Stake Weakness"
  - "desc": "If the lion moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the target is [[conditions#Prone|prone]], the lion can make one bite attack against it as a bonus action."
    "name": "Pounce"
  - "desc": "With a 10-foot running start, the lion can long jump up to 25 feet."
    "name": "Running Leap"
  - "desc": "If the lion is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, it gains 7 (1d10+2) [[hit-points-xphb|Hit Points]] and the following traits: **_Indestructible._** The lion can't be destroyed, and having 0 or less [[hit-points-xphb|Hit Points]] doesn't kill it. **_Spell Turning._** The lion has [[advantage-xphb|Advantage]] on saving throws against any spell that targets only the lion (not an area). If the lion’s saving throw succeeds and the spell is of 4th level or lower, the spell has no effect on the lion and instead targets the caster."
    "name": "Lion's Blessing (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The lion makes two attacks: one with its bite and one with its claw."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage."
    "name": "Claw"
"legendary_actions":
  - "desc": "The lion makes one claw attack."
    "name": "Claw"
  - "desc": "The lion emits a magical roar. Each creature within 60 feet of the lion that can hear the roar must succeed on a DC 12 Wisdom saving throw or be [[conditions#Frightened|frightened]] of the lion until the end of the lion’s next turn."
    "name": "Roar (Costs 2 Actions)"
"source":
  - "TBVIV"
"image": "Homebrew/bestiary/monstrosity/token/fleecemane-lion-tbviv.webp"
```
^statblock
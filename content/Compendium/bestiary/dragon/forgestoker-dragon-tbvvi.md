---
title: Forgestoker Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/23
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Forgestoker Dragon"]
---
# Forgestoker Dragon
*Source: Theros Bestiary TBVVI*  

<small><blockquote>The Akroans fashion their helms to honor the dragons, not to protect against them, as that would be of little help.</blockquote></small>

![Forgestoker Dragon](https://img.scryfall.com/cards/art_crop/front/4/f/4fd44170-ded7-4895-8950-bfa9d19e471d.jpg?1578452158#right)  

```statblock
"name": "Forgestoker Dragon (TBVVI)"
"size": "Gargantuan"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "22"
"hp": !!int "560"
"hit_dice": "40d20 + 160"
"modifier": !!int "0"
"stats":
  - !!int "21"
  - !!int "10"
  - !!int "19"
  - !!int "15"
  - !!int "15"
  - !!int "23"
"speed": "40 ft., fly 80 ft., climb 40 ft."
"saves":
  - "dexterity": !!int "7"
  - "constitution": !!int "11"
  - "wisdom": !!int "9"
  - "charisma": !!int "13"
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+16"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"damage_immunities": "fire"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 10"
"languages": "Draconic, Common (barely)"
"cr": "23"
"traits":
  - "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
"actions":
  - "desc": "The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 15 (2d10 + 5) piercing damage plus 14 (4d6) fire damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 20 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage."
    "name": "Tail"
  - "desc": "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."
    "name": "Frightful Presence"
  - "desc": "The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one."
    "name": "Fire Breath (Recharge 5-6)"
"legendary_actions":
  - "desc": "The dragon makes a Wisdom (Perception) check."
    "name": "Detect"
  - "desc": "The dragon makes a tail attack."
    "name": "Tail Attack"
  - "desc": "The dragon beats its wings. Each creature within 15 ft. of the dragon must succeed on a DC 25 Dexterity saving throw or take 12 (2d6 + 5) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
    "name": "Wing Attack (Costs 2 Actions)"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/dragon/token/forgestoker-dragon-tbvvi.webp"
```
^statblock
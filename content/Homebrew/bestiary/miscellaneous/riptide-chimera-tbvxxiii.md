---
title: Riptide Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxiii
- monster/cr/5
- monster/size/l
- monster/type/miscellaneous
statblock: inline
aliases: ["Riptide Chimera"]
---
# Riptide Chimera
*Source: Theros Bestiary TBVXXIII*  

<blockquote><small>"I want one." - Kiora</small></blockquote>

The riptide chimera is a nyxborn creature with a bear's body, the heads of a shark and a piranha, crab claws, bat wings, and a tail of jellyfish tentacles.

![Riptide Chimera](Homebrew/bestiary/miscellaneous/img/riptide-chimera.webp#right|850)  

```statblock
"name": "Riptide Chimera (TBVXXIII)"
"size": "Large"
"type": "3rd-level transmutation monstrosity"
"alignment": "Unaligned"
"ac": !!int "11"
"ac_class": "natural armor"
"hp": !!int "32"
"hit_dice": "4d10 + 12"
"modifier": !!int "3"
"stats":
  - !!int "19"
  - !!int "16"
  - !!int "16"
  - !!int "1"
  - !!int "10"
  - !!int "4"
"speed": "10 ft., fly 60 ft., swim 40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Paralyzed|paralyzed]], [[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 10"
"languages": ""
"cr": "5"
"traits":
  - "desc": "The chimera can breathe air and water."
    "name": "Amphibious"
  - "desc": "The chimera is [[conditions#Incapacitated|incapacitated]] while in the area of an [[antimagic-field-xphb|Antimagic Field]]. If targeted by [[dispel-magic-xphb|Dispel Magic]], the chimera must succeed on a Constitution saving throw against the caster's spell save DC or fall [[conditions#Unconscious|unconscious]] for 1 minute."
    "name": "Antimagic Susceptibility"
  - "desc": "The chimera has [[advantage-xphb|Advantage]] on melee attack rolls against any creature that doesn't have all its [[hit-points-xphb|Hit Points]]."
    "name": "Blood Frenzy"
  - "desc": "The chimera's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "At the start of each of its turns, the chimera deals 5 (1d10) poison damage to any creature within 5 ft. of it."
    "name": "Minor Stings"
  - "desc": "The chimera can’t be surprised, and it has [[advantage-xphb|Advantage]] on saving throws against being knocked [[conditions#Unconscious|unconscious]]."
    "name": "Multiheaded"
  - "desc": "In addition to being a creature, the chimera is a 3rd-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The chimera glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "The chimera makes five attacks: two with its bite, one with its claw, and one with its tentacles."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 10 (1d6 + 4) bludgeoning damage, and the target is [[conditions#Grappled|grappled]] (escape DC 11). The chimera has two claws, each of which can grapple only one target."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +2 to hit, reach 10 ft., one creature. Hit: 5 (1d10) poison damage and the creature must make a DC 16 Constitution saving throw. On a failed save, it is [[conditions#Paralyzed|paralyzed]] until the start of its next turn. On a successful save, it isn't [[conditions#Paralyzed|paralyzed]] but its movement is halved until the start of its next turn."
    "name": "Tentacles"
"source":
  - "TBVXXIII"
"image": "Homebrew/bestiary/miscellaneous/token/riptide-chimera-tbvxxiii.webp"
```
^statblock
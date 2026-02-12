---
title: Archetype of Courage
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxviii
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Archetype of Courage"]
---
# Archetype of Courage
*Source: Theros Bestiary TBVXVIII*  

<blockquote><small>"It has been my experience that soldiers most fervently follow generals who lead by example." - Elspeth</small></blockquote>
The archetype of courage is a human soldier blessed by Iroas. His blessing extends to his allies.

![Archetype of Courage](Compendium/bestiary/miscellaneous/img/archetype-of-courage.webp#right|850)  

```statblock
"name": "Archetype of Courage (TBVXVIII)"
"size": "Medium"
"type": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "14"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"condition_immunities": "frightened"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "4"
"traits":
  - "desc": "Allies of the archetype that it can see within 120 ft. have the archetype's Hold the Line ability. As long as the archetype can see any non-allies within 120 ft., they do not have the Hold the Line ability and cannot gain it."
    "name": "Blessing of Iroas"
  - "desc": "While the archetype is holding a spear, other creatures provoke an opportunity attack from the archetype when they move within 5 feet of it. When the archetype hits a creature with an opportunity attack using its spear, the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed becomes 0 for the rest of the turn."
    "name": "Hold the Line"
  - "desc": "The archetype's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The archetype glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "The archetype makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
    "name": "Shield Bash"
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft., or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
"source":
  - "TBVXVIII"
"image": "Compendium/bestiary/miscellaneous/token/archetype-of-courage-tbvxviii.webp"
```
^statblock
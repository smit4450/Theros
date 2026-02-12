---
title: Archetype of Endurance
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvii
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Archetype of Endurance"]
---
# Archetype of Endurance
*Source: Theros Bestiary TBVXVII*  

<blockquote><small>Despite its fearsome stature, it is as elusive as a shadow, circling round to stalk those who presume to hunt it.</small></blockquote>
The archetype of endurance is a wild boar blessed by Nylea. Its blessing extends to its allies.

![Archetype of Endurance](Compendium/bestiary/beast/img/archetype-of-endurance.webp#right|850)  

```statblock
"name": "Archetype of Endurance (TBVXVII)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "40"
"hit_dice": "5d10 + 15"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "10"
  - !!int "16"
  - !!int "2"
  - !!int "7"
  - !!int "5"
"speed": "40 ft."
"senses": "passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "Allies of the archetype that it can see within 120 ft. have the archetype's Limited Magic Immunity ability. As long as the archetype can see any non-allies within 120 ft., they do not have the Limited Magic Immunity ability and cannot gain it."
    "name": "Blessing of Nylea"
  - "desc": "If the archetype moves at least 20 ft. straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 7 (2d6) slashing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
    "name": "Charge"
  - "desc": "The archetype can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects."
    "name": "Limited Magic Immunity"
  - "desc": "The archetype's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "If the archetype takes 10 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
    "name": "Relentless (Recharges after a Short or Long Rest)"
  - "desc": "The archetype glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."
    "name": "Tusk"
"source":
  - "TBVXVII"
"image": "Compendium/bestiary/beast/token/archetype-of-endurance-tbvxvii.webp"
```
^statblock
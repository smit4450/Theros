---
title: Returned Sentry
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Returned Sentry"]
---
# Returned Sentry
*Source: Mythic Odysseys of Theros p. 241*  

![](Compendium/bestiary/undead/img/returned.webp#right|850)  
Most new or purposeless Returned are easily manipulated into serving their more forceful brethren. Having purpose forced upon them, these Returned perform simple, artless tasks with middling efficiency. Their one virtue is their tirelessness, which makes them exceptional guards. In the necropoleis, this sees many Returned employed as sentries, though they might also be messengers or laborers. If threatened, groups of these Returned work well together, sharing the unified goals of overcoming their foes and getting back to the task at hand.

Returned have escaped the Underworld and dwell among the living once more, but their second lives are rarely what they expected—not that they remember what it was they expected. As a result of having followed the Path of Phenax (see chapter 4), the Returned lose their identities, which manifest as separate beings known as eidolons. The experience of escaping the Underworld also causes them to lose their faces, which become expressionless surfaces with empty eye sockets and gaping mouths. These blank surfaces they cover with distinctive golden masks.

Returned reenter the world blank and undead. No longer possessing the ability to form long-term memories, they generally can't build meaningful relationships or establish new lives. Instead, most experience fleeting emotions and follow hollow routines, their existences reduced to shadow plays without weight or substance.
```statblock
"name": "Returned Sentry (MOT)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "[leather armor](Compendium/items/leather-armor-xphb.md), [shield](Compendium/items/shield-xphb.md)"
"hp": !!int "22"
"hit_dice": "4d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "15"
  - !!int "12"
  - !!int "10"
  - !!int "12"
  - !!int "11"
"speed": "30 ft."
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "passive Perception 11"
"languages": "the languages it knew in life"
"cr": "1"
"traits":
  - "desc": "The Returned has advantage on an attack roll against a creature if at\
      \ least one of the Returned's allies is within 5 feet of the creature and the\
      \ ally isn't [incapacitated](Compendium/rules/conditions.md#Incapacitated)."
    "name": "Pack Tactics"
  - "desc": "The Returned has advantage on saving throws against any effect that turns\
      \ undead."
    "name": "Turn Resistance"
  - "desc": "The Returned is immune to any effect that would sense its emotions or\
      \ read its thoughts. Wisdom ([Insight](Compendium/rules/skills.md#Insight))\
      \ checks to ascertain the Returned's intentions or sincerity are made with disadvantage."
    "name": "Unreadable Face"
"actions":
  - "desc": "*Melee  or Ranged Weapon Attack:* +5 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. *Hit:* 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing\
      \ damage if used with two hands to make a melee attack, plus 7 (2d6) poison\
      \ damage."
    "name": "Spear"
  - "desc": "*Ranged Weapon Attack:* +4 to hit, range 30/120 ft., one target. *Hit:*\
      \ 4 (1d4 + 2) bludgeoning damage."
    "name": "Sling"
"source":
  - "MOT"
"image": "Compendium/bestiary/undead/token/returned-sentry-mot.webp"
```
^statblock
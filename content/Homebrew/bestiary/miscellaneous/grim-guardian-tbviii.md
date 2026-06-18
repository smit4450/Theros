---
title: Grim Guardian
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviii
- monster/cr/2
- monster/size/m
- monster/type/miscellaneous
statblock: inline
aliases: ["Grim Guardian"]
---
# Grim Guardian
*Source: Theros Bestiary TBVIII*  

<blockquote><small>Occasionally the living wander to the Rivers, but the wardens of Athreos ensure that only the dead pass.</small></blockquote>

![Grim Guardian](Homebrew/bestiary/miscellaneous/img/grim-guardian.webp#right|850)  

```statblock
"name": "Grim Guardian (TBVIII)"
"size": "Medium"
"type": "3rd-level transmutation undead humanoid"
"subtype": "human, returned"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "leather armor, shield"
"hp": !!int "32"
"hit_dice": "4d8 + 16"
"modifier": !!int "1"
"stats":
  - !!int "13"
  - !!int "13"
  - !!int "18"
  - !!int "10"
  - !!int "12"
  - !!int "11"
"speed": "30 ft."
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"traits":
  - "desc": "The guardian's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The Returned has [[advantage-xphb|Advantage]] on an attack roll against a creature if at least one of the Returned’s allies is within 5 feet of the creature and the ally isn’t [[conditions#Incapacitated|incapacitated]]."
    "name": "Pack Tactics"
  - "desc": "The Returned is undead. It needs water and air but not food or sleep. It thinks and speaks and even feels emotions based on its new experiences, but given its circumstances, those emotions tend to be muted."
    "name": "Returned Nature"
  - "desc": "In addition to being a creature, the guardian is a 3rd-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The guardian glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "While the guardian is in any of Theros's three realms, it can magically convey what it senses to Athreos."
    "name": "Telepathic Bond"
  - "desc": "The Returned has [[advantage-xphb|Advantage]] on saving throws against any effect that turns undead."
    "name": "Turn Resistance"
  - "desc": "The Returned is immune to any effect that would sense its emotions or read its thoughts. Wisdom (Insight) checks to ascertain the Returned’s intentions or sincerity are made with [[disadvantage-xphb|Disadvantage]]."
    "name": "Unreadable Face"
"actions":
  - "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack, plus 7 (2d6) necrotic damage."
    "name": "Spear"
  - "desc": "Ranged Weapon Attack: +3 to hit, range 30/120 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage."
    "name": "Sling"
"source":
  - "TBVIII"
"image": "Homebrew/bestiary/miscellaneous/token/grim-guardian-tbviii.webp"
```
^statblock
---
title: War-Wing Siren
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["War-Wing Siren"]
---
# War-Wing Siren
*Source: Theros Bestiary TBVVI*  

<blockquote><small>Once she sang sailors to their doom. Now she leads them to glory.</small></blockquote>

![War-Wing Siren](https://img.scryfall.com/cards/art_crop/front/8/d/8d88c942-3a69-4975-a08d-80405a549beb.jpg?1593095605#right)  

```statblock
"name": "War-Wing Siren (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"subtype": "siren"
"alignment": "Chaotic Evil"
"ac": !!int "18"
"ac_class": "chain mail, shield"
"hp": !!int "63"
"hit_dice": "9d8 + 27"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "14"
  - !!int "16"
  - !!int "7"
  - !!int "11"
  - !!int "14"
"speed": "20 ft., fly 40 ft."
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+3"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed)"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "The soldier has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being [charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled), or [restrained](Compendium/rules/conditions.md#Restrained) while it is within 5 feet of at least one ally."
    "name": "Formation Tactics"
"actions":
  - "desc": "The siren makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 10 ft., one target. _Hit:_ 6 (1d10 + 1) slashing damage."
    "name": "Glaive"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage."
    "name": "Claws"
  - "desc": "The siren sings a magical melody. Every humanoid and giant within 300 ft. of the siren that can hear the song must succeed on a DC 11 Wisdom saving throw or be [charmed](Compendium/rules/conditions.md#Charmed) until the song ends. The siren must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the siren is [incapacitated](Compendium/rules/conditions.md#Incapacitated). While [charmed](Compendium/rules/conditions.md#Charmed) by the siren, a target is [incapacitated](Compendium/rules/conditions.md#Incapacitated) and ignores the songs of other sirens. If the [charmed](Compendium/rules/conditions.md#Charmed) target is more than 5 ft. away from the siren, the must move on its turn toward the siren by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the siren, a target can repeat the saving throw. A creature can also repeat the saving throw at the end of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this siren's song for the next 24 hours."
    "name": "Luring Song"
"reactions":
  - "desc": "Whenever the siren is the target of a spell, that spell's caster chooses whether following happens: - Until the end of combat, the siren gains a +1 bonus to damage rolls and Dexterity checks, and it gains 4 (1d8) temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Heroic"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/war-wing-siren-tbvvi.webp"
```
^statblock
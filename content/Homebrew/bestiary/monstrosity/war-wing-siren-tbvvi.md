---
title: War-Wing Siren
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvvi
- monster/cr/3
- monster/size/m
- monster/type/monstrosity
statblock: inline
aliases: ["War-Wing Siren"]
---
# War-Wing Siren
*Source: Theros Bestiary TBVVI*  

<blockquote><small>Once she sang sailors to their doom. Now she leads them to glory.</small></blockquote>

![War-Wing Siren](Homebrew/bestiary/monstrosity/img/war-wing-siren.webp#right)  

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
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
"condition_immunities": "[[conditions#Charmed|charmed]]"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "The soldier has [[advantage-xphb|Advantage]] on saving throws against being [[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]], [[conditions#Grappled|grappled]], or [[conditions#Restrained|restrained]] while it is within 5 feet of at least one ally."
    "name": "Formation Tactics"
"actions":
  - "desc": "The siren makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 10 ft., one target. _Hit:_ 6 (1d10 + 1) slashing damage."
    "name": "Glaive"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage."
    "name": "Claws"
  - "desc": "The siren sings a magical melody. Every humanoid and giant within 300 ft. of the siren that can hear the song must succeed on a DC 11 Wisdom saving throw or be [[conditions#Charmed|charmed]] until the song ends. The siren must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the siren is [[conditions#Incapacitated|incapacitated]]. While [[conditions#Charmed|charmed]] by the siren, a target is [[conditions#Incapacitated|incapacitated]] and ignores the songs of other sirens. If the [[conditions#Charmed|charmed]] target is more than 5 ft. away from the siren, the must move on its turn toward the siren by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the siren, a target can repeat the saving throw. A creature can also repeat the saving throw at the end of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this siren's song for the next 24 hours."
    "name": "Luring Song"
"reactions":
  - "desc": "Whenever the siren is the target of a spell, that spell's caster chooses whether following happens: - Until the end of combat, the siren gains a +1 bonus to damage rolls and Dexterity checks, and it gains 4 (1d8) temporary [[hit-points-xphb|Hit Points]]."
    "name": "Heroic"
"source":
  - "TBVVI"
"image": "Homebrew/bestiary/monstrosity/token/war-wing-siren-tbvvi.webp"
```
^statblock
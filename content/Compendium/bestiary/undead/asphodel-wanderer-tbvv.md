---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvv
- monster/cr/1-4
- monster/size/medium
- monster/type/undead/skeleton
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Asphodel Wanderer"
---
# Asphodel Wanderer
*Source: Theros Bestiary, Vol. V*
![](/Compendium/bestiary/undead/img/asphodel-wanderer.webp#right)

He killed out of hate, so now only hate sustains him. He sought immortality, so the gods gave it to him.

```statblock
"name": "Asphodel Wanderer"
"size": "Medium"
"type": "undead"
"subtype": "skeleton"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"ac_class": "armor scraps"
"hp": !!int "12"
"hit_dice": "2d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "15"
  - !!int "6"
  - !!int "8"
  - !!int "5"
"speed": "30 ft."
"saves":
  - "strength": !!int "2"
  - "dexterity": !!int "4"
"damage_vulnerabilities": "bludgeoning"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Understands Common but can't speak"
"cr": "1/4"
"traits":
  - "desc": "While the wanderer is holding a shortsword, other creatures provoke an\
      \ opportunity attack from the wanderer when they move within 5 feet of it. When\
      \ the wanderer hits a creature with an opportunity attack using its shortsword,\
      \ the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed\
      \ becomes 0 for the rest of the turn."
    "name": "Hold the Line"
  - "desc": "The wanderer doesn’t require food, drink, or sleep."
    "name": "Immortal Nature"
  - "desc": "If damage reduces the wanderer to 0 Hit Points, it must make a Constitution\
      \ saving throw with a DC of 5 + the damage taken, unless the damage is radiant\
      \ or from a critical hit. On a success, the wanderer drops to 1 hit point instead."
    "name": "Undead Fortitude"
"actions":
  - "desc": "The wanderer makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft., one target. Hit:\
      \ 5 (1d6 + 2) piercing damage."
    "name": "Shortsword"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4\
      \ + 3) bludgeoning damage. If the target is a Medium or smaller creature, it\
      \ must succeed on a DC 13 Strength saving throw or be knocked prone."
    "name": "Shield Bash"
"source":
  - "TBVV"
```
^statblock
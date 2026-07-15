---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxvi
- monster/cr/4
- monster/size/medium
- monster/type/humanoid
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Staunch-Hearted Warrior"
---
# Staunch-Hearted Warrior
*Source: Theros Bestiary, Vol. XVI*
![](/Compendium/bestiary/humanoid/img/staunch-hearted-warrior.webp#right)

As soon as she faces a monster, she begins composing its epitaph.

```statblock
"name": "Staunch-Hearted Warrior"
"size": "Medium"
"type": "humanoid"
"alignment": "Any alignment"
"ac": !!int "20"
"ac_class": "plate, shield"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "15"
  - !!int "15"
  - !!int "11"
  - !!int "13"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common, any two languages"
"cr": "4"
"traits":
  - "desc": "The warrior has Advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "The warrior's attack rolls score a critical hit on a roll of 19 or 20\
      \ on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The warrior makes two attacks with its scimitar."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6\
      \ + 2) slashing damage, or 6 (1d8 + 2) slashing damage if used with two hands\
      \ to make a melee attack."
    "name": "Scimitar"
"reactions":
  - "desc": "Whenever the hero is the target of a spell, that spell's caster chooses\
      \ whether following happens: - Until the end of combat, the hero gains a +2\
      \ bonus to damage rolls and Strength checks, and it gains 9 (2d8) temporary\
      \ Hit Points."
    "name": "Heroic"
"source":
  - "TBVXVI"
```
^statblock
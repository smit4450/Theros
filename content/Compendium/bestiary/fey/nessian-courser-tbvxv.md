---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxv
- monster/cr/3
- monster/size/medium
- monster/type/fey/centaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Nessian Courser"
---
# Nessian Courser
*Source: Theros Bestiary, Vol. XV*
![](/Compendium/bestiary/fey/img/nessian-courser.webp#right)

Khestes the Adamant, the Champion’s closest ally among the centaurs, took one stone to his shoulder and another to his flank. He held his stride and his aim, and let fly the arrow that killed the giant Grinthax.

—The Theriad

```statblock
"name": "Nessian Courser"
"size": "Medium"
"type": "fey"
"subtype": "centaur"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "16"
  - !!int "16"
  - !!int "10"
  - !!int "13"
  - !!int "10"
"speed": "40 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+3"
  - "name": "[Nature](/Compendium/rules/skills.md#Nature)"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "3"
"traits":
  - "desc": "The courser has Advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "If the courser moves at least 30 feet straight toward a target and then\
      \ hits it with a melee attack on the same turn, it can immediately follow that\
      \ attack with a bonus action, making one attack against the target with its\
      \ hooves."
    "name": "Charge"
  - "desc": "The courser counts as one size larger when determining its carrying capacity\
      \ and the weight it can push or drag. In addition, any climb that requires hands\
      \ and feet is especially difficult for it because of its equine legs. When it\
      \ makes such a climb, each foot of movement costs it 4 extra feet instead of\
      \ the normal 1 extra foot."
    "name": "Equine Build"
  - "desc": "The courser's attack rolls score a critical hit on a roll of 19 or 20\
      \ on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The courser makes two attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 5 (1d4\
      \ + 3) bludgeoning damage."
    "name": "Hooves"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 10 ft., one target. _Hit:_ 8\
      \ (1d10 + 3) slashing damage."
    "name": "Glaive"
  - "desc": "_Ranged Weapon Attack:_ +7 to hit, range 150/600 ft., one target. _Hit:_\
      \ 7 (1d8 + 3) piercing damage."
    "name": "Longbow"
"source":
  - "TBVXV"
```
^statblock
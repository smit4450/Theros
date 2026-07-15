---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxiv
- monster/cr/3
- monster/size/medium
- monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Daring Thief"
---
# Daring Thief
*Source: Theros Bestiary, Vol. XIV*
![](/Compendium/bestiary/humanoid/img/daring-thief.webp#right)

Honesty is the first casualty of war.

```statblock
"name": "Daring Thief"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "leather"
"hp": !!int "78"
"hit_dice": "13d8 + 26"
"modifier": !!int "4"
"stats":
  - !!int "12"
  - !!int "19"
  - !!int "15"
  - !!int "12"
  - !!int "12"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "6"
  - "intelligence": !!int "3"
"skillsaves":
  - "name": "[Acrobatics](/Compendium/rules/skills.md#Acrobatics)"
    "desc": "+6"
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+3"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Sleight of Hand](/Compendium/rules/skills.md#Sleight%20of%20Hand)"
    "desc": "+6"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
  - "name": "[Deception](/Compendium/rules/skills.md#Deception)"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "thieves' cant, Common, Any one language"
"cr": "3"
"actions":
  - "desc": "The thief makes three attacks with its dagger."
    "name": "Multiattack"
  - "desc": "_Melee or Ranged Weapon Attack:_ +6 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. _Hit:_ 6 (1d4 + 4) piercing damage."
    "name": "Dagger"
"reactions":
  - "desc": "At the beginning of the thief's turn, if the thief attacked a creature\
      \ at any point since the thief's last turn, the thief may choose an object it\
      \ knows that creature is carrying and an object the thief is carrying, and attempts\
      \ to exchange possession of those objects as a bonus action. The objects must\
      \ be roughly equal in size, shape, and weight; for example, a nail for a key,\
      \ a rock for a piece of jewelry. The thief must know the exact location of the\
      \ object it tries to obtain. The thief makes a Dexterity (Sleight of Hand) check\
      \ equal to that 8 + creature's proficiency bonus + that creature's Dexterity\
      \ score. On a success, the thief completes the swap successfully. If the thief\
      \ succeeds by 4 or less, that creature saw the burglary but failed to prevent\
      \ it. If the thief succeeds by the check by 5-9, that creature knows it has\
      \ been burglarized, but doesn't know how or when it occurred. If the thief succeeds\
      \ by 10 or more, that creature is oblivious to the swap until it notices the\
      \ item has been replaced."
    "name": "Daring Swap"
  - "desc": "The thief halves the damage that it takes from an attack that hits it.\
      \ The thief must be able to see the attacker."
    "name": "Uncanny Dodge"
"source":
  - "TBVXIV"
```
^statblock
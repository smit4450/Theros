---
title: Agent of the Fates
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxiv
- monster/cr/9
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Agent of the Fates"]
---
# Agent of the Fates
*Source: Theros Bestiary TBVXIV*  

<small><blockquote>"You are breathing borrowed air."</blockquote></small>

![Agent of the Fates](Homebrew/bestiary/humanoid/img/agent-of-the-fates.webp#right)  

```statblock
"name": "Agent of the Fates (TBVXIV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Lawful Evil"
"ac": !!int "15"
"hp": !!int "72"
"hit_dice": "12d8 + 24"
"modifier": !!int "3"
"stats":
  - !!int "12"
  - !!int "17"
  - !!int "15"
  - !!int "14"
  - !!int "12"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "6"
  - "intelligence": !!int "5"
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+6"
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+9"
"damage_resistances": "poison"
"senses": "passive Perception 10"
"languages": "Thieves' cant plus any two languages, Common"
"cr": "9"
"traits":
  - "desc": "During its first turn, the assassin has [[advantage-xphb|Advantage]] on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit."
    "name": "Assassinate"
  - "desc": "If the assassin is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the assassin instead takes no damage if it succeeds on the saving throw, and only half damage if it fails."
    "name": "Evasion"
  - "desc": "The assassin deals an extra 14 (4d6) damage when it hits a target with a weapon attack and has [[advantage-xphb|Advantage]] on the attack roll, or when the target is within 5 ft. of an ally of the assassin that isn't [[conditions#Incapacitated|incapacitated]] and the assassin doesn't have [[disadvantage-xphb|Disadvantage]] on the attack roll."
    "name": "Sneak Attack (1/Turn)"
"actions":
  - "desc": "The assassin makes two dagger attacks."
    "name": "Multiattack"
  - "desc": "_Melee or Ranged Weapon Attack:_ +6 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 5 (1d4 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."
    "name": "Dagger"
"reactions":
  - "desc": "Whenever the agent becomes targeted by a spell, that spell's caster determines whether the following happens: - The agent makes a ranged dagger attack at each of up to 7 (1d6 + 1) creatures it can see."
    "name": "Heroic"
"source":
  - "TBVXIV"
"image": "Homebrew/bestiary/humanoid/token/agent-of-the-fates-tbvxiv.webp"
```
^statblock
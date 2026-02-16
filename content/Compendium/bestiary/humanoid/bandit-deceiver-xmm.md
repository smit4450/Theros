---
title: Bandit Deceiver
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Bandit Deceiver"]
---
# Bandit Deceiver
*Source: Monster Manual (2024) p. 28*  

![](Compendium/bestiary/humanoid/img/bandits.webp#right|850)  
Bandit deceivers use magic to disguise their activities or create flashy distractions.

## Bandits

*Criminals and Scoundrels*

- **Habitat.** Any  
- **Treasure.** Any  

Bandits use the threat of violence to take what they want. Such criminals include gang members, desperadoes, and lawless mercenaries. Yet not all bandits are motivated by greed. Some are driven to lives of crime by unjust laws, desperation, or the threats of merciless leaders.

Roll on or choose a result from the Bandit Motivations table to determine the circumstances behind a bandit's crimes.

> [!quote] A quote from Jarlaxle  
> 
> I am he who rules the world, don't you know? One little piece at a time.

**Bandit Motivations**

| dice: 1d6 | The Bandit... |
|-----------|---------------|
| 1 | Fights only oppressors. |
| 2 | Is an ex-soldier who was discarded by their nation and now takes what they were promised. |
| 3 | Is in a gang that views nonmembers as foes. |
| 4 | Hesitantly serves a villainous leader. |
| 5 | Secretly works for a government or a regional ruler to sow chaos. |
| 6 | Takes what they need to survive. |
^bandit-motivations
## Statblock

```statblock
"name": "Bandit Deceiver (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "16"
"hp": !!int "130"
"hit_dice": "20d8 + 40"
"modifier": !!int "6"
"stats":
  - !!int "8"
  - !!int "16"
  - !!int "14"
  - !!int "17"
  - !!int "12"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "6"
  - "intelligence": !!int "6"
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+6"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+9"
"senses": "passive Perception 14"
"languages": "Common, Thieves' cant"
"cr": "7"
"actions":
  - "desc": "The bandit makes three Dagger attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +6, reach 5 ft. or range 20/60 ft.\
      \ *Hit:* 8 (2d4 + 3) Piercing damage plus 10 (3d6) Poison damage."
    "name": "Dagger"
  - "desc": "*Constitution Saving Throw:* DC 14, each creature in a 10-foot-radius\
      \ [[sphere-area-of-effect-xphb|Sphere]] centered\
      \ on a point the bandit can see within 120 feet. *Failure:* 13 (3d6 + 3) Radiant\
      \ damage, and the target has the [[conditions#Blinded|Blinded]]\
      \ condition until the start of the bandit's next turn. *Success:* Half damage\
      \ only."
    "name": "Blinding Flash (Recharge 4-6)"
  - "desc": "The bandit casts one of the following spells, using Intelligence as the\
      \ spellcasting ability (spell save DC 14):\n\n**At will:** [[disguise-self-xphb|Disguise Self]],\
      \ [[mage-hand-xphb|Mage Hand]], [[minor-illusion-xphb|Minor Illusion]]\n\
      \n**1/day each:** [[hold-person-xphb|Hold Person]] (level\
      \ 4 version), [[mage-armor-xphb|Mage Armor]] (included in\
      \ AC), [[major-image-xphb|Major Image]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/bandit-deceiver-xmm.webp"
```
^statblock
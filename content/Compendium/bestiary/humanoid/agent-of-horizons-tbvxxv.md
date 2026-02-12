---
title: Agent of Horizons
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxv
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Agent of Horizons"]
---
# Agent of Horizons
*Source: Theros Bestiary TBVXXV*  

<blockquote><small>The light in the woods just before dawn reveals a glimmering network of branches, roots, and spiderwebs. The acolytes of Kruphix walk this lattice unseen.</small></blockquote>

![Agent of Horizons](Compendium/bestiary/humanoid/img/agent-of-horizons.webp#right)  

```statblock
"name": "Agent of Horizons (TBVXXV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "24"
"hit_dice": "6d8 + 0"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "16"
  - !!int "11"
  - !!int "13"
  - !!int "15"
  - !!int "17"
"speed": "30 ft."
"skillsaves":
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[Insight](Compendium/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Investigation](Compendium/rules/skills.md#Investigation)"
    "desc": "+5"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+6"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+5"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Common, Any two languages"
"cr": "1"
"traits":
  - "desc": "On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action."
    "name": "Cunning Action"
  - "desc": "The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 ft. of an ally of the spy that isn't incapacitated and the spy doesn't have disadvantage on the attack roll."
    "name": "Sneak Attack (1/Turn)"
  - "desc": "While the agent is in any of Theros's three realms, it can magically convey what it senses to Kruphix."
    "name": "Telepathic Bond"
"actions":
  - "desc": "The spy makes two melee attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
    "name": "Shortsword"
  - "desc": "Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
    "name": "Hand Crossbow"
"source":
  - "TBVXXV"
"image": "Compendium/bestiary/humanoid/token/agent-of-horizons-tbvxxv.webp"
```
^statblock
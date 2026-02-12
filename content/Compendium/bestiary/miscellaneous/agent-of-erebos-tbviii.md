---
title: Agent of Erebos
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviii
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Agent of Erebos"]
---
# Agent of Erebos
*Source: Theros Bestiary TBVIII*  

<blockquote><small>Erebos’s minions hunt the Returned and warn those who consider the same folly.</small></blockquote>
These zombies are sent into the mortal realm by Erebos to find the escaped Returned and send them back to Erebos. Their masks are kept as trophies.

![Agent of Erebos](Compendium/bestiary/miscellaneous/img/agent-of-erebos.webp#right|850)  

```statblock
"name": "Agent of Erebos (TBVIII)"
"size": "Medium"
"type": "4th-level transmutation undead"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"hp": !!int "72"
"hit_dice": "12d8 + 24"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "16"
  - !!int "14"
  - !!int "13"
  - !!int "11"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "6"
  - "intelligence": !!int "4"
"skillsaves":
  - "name": "[Acrobatics](Compendium/rules/skills.md#Acrobatics)"
    "desc": "+6"
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+3"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+9"
"damage_immunities": "poison"
"condition_immunities": "poisoned"
"senses": "passive Perception 10"
"languages": "Thieves' cant, Celestial, Common"
"cr": "8"
"traits":
  - "desc": "If the agent is aware of a Returned mask, it spends its turns trying to banish the person or monster carrying that mask."
    "name": "Bounty of Erebos"
  - "desc": "If the agent is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the agent instead takes no damage if it succeeds on the saving throw, and only half damage if it fails."
    "name": "Evasion"
  - "desc": "The agent's innate spellcasting ability is Charisma (spell save DC 11, +3 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _banishment_"
    "name": "Innate Spellcasting"
  - "desc": "The agent's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the agent is a 4th-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The agent glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "While the agent is in any of Theros's three realms, it can magically convey what it senses to Erebos."
    "name": "Telepathic Bond"
"actions":
  - "desc": "The agent banishes a creature wearing or holding a Returned mask to the Realm of the Dead using _banishment_. Any objects the creature was carrying or wearing fall to the ground. As a bonus action, the agent loots any Returned masks the target was wearing or carrying and strings them onto its cord."
    "name": "Banish Dead"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 bludgeoning damage. This is a magic weapon attack."
    "name": "Unarmed Strike"
"source":
  - "TBVIII"
"image": "Compendium/bestiary/miscellaneous/token/agent-of-erebos-tbviii.webp"
```
^statblock
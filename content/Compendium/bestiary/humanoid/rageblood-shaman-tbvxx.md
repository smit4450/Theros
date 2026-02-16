---
title: Rageblood Shaman
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxx
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Rageblood Shaman"]
---
# Rageblood Shaman
*Source: Theros Bestiary TBVXX*  

<blockquote><small>“I see a spark of pure rage. Soon that spark will spread from the depths of Kragma. Soon its fire will engulf the polis.”

—Hira, street oracle</small></blockquote>

![Rageblood Shaman](https://img.scryfall.com/cards/art_crop/front/f/f/ffaa31fd-5ba5-49d4-90b6-fafb9f1a8b3a.jpg?1562839783#right)  

```statblock
"name": "Rageblood Shaman (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "14"
"hit_dice": "2d8 + 6"
"modifier": !!int "2"
"stats":
  - !!int "12"
  - !!int "14"
  - !!int "16"
  - !!int "13"
  - !!int "15"
  - !!int "15"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "4"
  - "charisma": !!int "4"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+4"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+5"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+5"
"damage_immunities": "fire"
"senses": "passive Perception 10"
"languages": "Celestial, Common, Minotaur"
"cr": "4"
"traits":
  - "desc": "While the shaman is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the shaman with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just the shaman seeks insights from interpreting the divine, so too does Mogis occasionally seek to manipulate the world through the shaman. Sometimes Mogis might speak directly, be it with dramatic manifestations or direct possession of the shaman. Although Mogis's words might be steeped in metaphors, should he wish to make his intentions clear, he often finds dramatic ways to make his thoughts known."
    "name": "Divine Influence"
  - "desc": "Immediately after the shaman uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The shaman's innate spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _guidance_, [[light-xphb|Light]], [[thaumaturgy-xphb|Thaumaturgy]] 3/day: [[bless-xphb|Bless]], [[guiding-bolt-xphb|Guiding Bolt]], [[healing-word-xphb|Healing Word]], [[hold-person-xphb|Hold Person]] 1/day: [[augury-xphb|Augury]], [[scrying-xphb|Scrying]]"
    "name": "Innate Spellcasting"
  - "desc": "The shaman possesses unparalleled experience in divining Mogis's whims from cryptic visions and mundane forces."
    "name": "Interpreter of Signs"
  - "desc": "The minotaur starves itself prior to battle. If it kills a creature and has not eaten, there is a 50% chance it will stop fighting to eat the corpse. If the minotaur eats, each hostile creature that can see it must succeed on a DC 11 Wisdom saving throw or be [[conditions#Frightened|frightened]] of the minotaur until the end of the minotaur's next turn. If a hungry minotaur does not eat after a kill, it gets a +1 bonus to damage rolls until it eats."
    "name": "Ragegore Hunger"
  - "desc": "The shaman can move in and out of a Medium or smaller creature's space. If it would, it uses a bonus action to attack that creature with an unarmed strike. That creature must succeed on a DC 11 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, the shaman can't enter that space and must end its turn immediately. If the shaman stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until the shaman moves off it (escape DC 11)."
    "name": "Trample"
  - "desc": "Other minotaur creatures within 30 feet of the shaman that can hear its continuous rantings roll an additional die when determining damage they deal, and they have 4 temporary [[hit-points-xphb|Hit Points]]. They also have the Trample trait above. This effect ends for any creature that is no longer within this radius or that can no longer hear the shaman, or if the shaman is silenced."
    "name": "Word of Hope"
"actions":
  - "desc": "Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) force damage."
    "name": "Eldritch Touch"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 4 (1d6 + 1) piercing damage, and the shaman can use a bonus action to attempt to shove that target with its horns. The target must be within 5 feet of the shaman and no more than one size larger than it. Unless the target succeeds on a DC 11 Strength saving throw, the shaman pushes it up to 10 feet away from the shaman."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 3 (1d4 + 1) bludgeoning damage."
    "name": "Unarmed Strike"
"reactions":
  - "desc": "When the shaman or a creature it can see makes an attack roll, a saving throw, or an ability check, the shaman can cause the roll to be made with [[advantage-xphb|Advantage]] or [[disadvantage-xphb|Disadvantage]]."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/rageblood-shaman-tbvxx.webp"
```
^statblock
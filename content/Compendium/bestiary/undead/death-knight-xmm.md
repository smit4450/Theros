---
title: Death Knight
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/17
- monster/environment/any
- monster/size/small-or-medium
- monster/type/undead
statblock: inline
aliases: ["Death Knight"]
---
# Death Knight
*Source: Monster Manual (2024) p. 92, FRHoF*  

![](Compendium/bestiary/undead/img/death-knights.webp#right|850)  
Death knights are deadly combatants and domineering commanders with grim histories. Some strive to end the curses that doom them to undeath, though their selfish souls eternally shackle them to their fates. Others, like the infamous death knight Lord Soth, brood in dismal ruins for centuries, rousing themselves to action only when something reignites their deathless evil.

## Death Knights

*Haunted Commanders of Unliving Legions*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Champions of evil, death knights are armor-clad, skeletal warlords. Combining devastating martial prowess and blasphemous magic, these undying tyrants lead unholy legions against the living or brood in cursed citadels. Every death knight is haunted by a legacy of tragedy and dishonor that drives it to commit greater evils.
## Statblock

```statblock
"name": "Death Knight (XMM)"
"size": "Small or Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "20"
"hp": !!int "199"
"hit_dice": "21d8 + 105"
"modifier": !!int "12"
"stats":
  - !!int "20"
  - !!int "11"
  - !!int "20"
  - !!int "12"
  - !!int "16"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "6"
  - "wisdom": !!int "9"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 13"
"languages": "Abyssal, Common"
"cr": "17"
"traits":
  - "desc": "If the death knight fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "The death knight has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "Undead creatures of the death knight's choice (excluding itself) in a\
      \ 60-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from it have [[advantage-xphb|Advantage]]\
      \ on attack rolls and saving throws. It can't use this trait if it has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Marshal Undead"
  - "desc": "If the death knight is destroyed before it atones for its evil, it gains\
      \ a new body in 1d10 days, reviving with all its [[hit-points-xphb|Hit Points]].\
      \ The new body appears in a location significant to the death knight."
    "name": "Undead Restoration"
"actions":
  - "desc": "The death knight makes three Dread Blade attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +11, reach 5 ft. *Hit:* 12 (2d6 + 5) Slashing\
      \ damage plus 13 (3d8) Necrotic damage."
    "name": "Dread Blade"
  - "desc": "*Dexterity Saving Throw:* DC 18, each creature in a 20-foot-radius [[sphere-area-of-effect-xphb|Sphere]]\
      \ centered on a point the death knight can see within 120 feet. *Failure:* 35\
      \ (10d6) Fire damage plus 35 (10d6) Necrotic damage. *Success:* Half damage."
    "name": "Hellfire Orb (Recharge 5-6)"
  - "desc": "The death knight casts one of the following spells, requiring no Material\
      \ components and using Charisma as the spellcasting ability (spell save DC 18):\n\
      \n**At will:** [[command-xphb|Command]], [[phantom-steed-xphb|Phantom Steed]]\n\
      \n**2/day each:** [[destructive-wave-xphb|Destructive Wave]]\
      \ (Necrotic), [[dispel-magic-xphb|Dispel Magic]]"
    "name": "Spellcasting"
"reactions":
  - "desc": "Trigger: The death knight is hit by a melee attack roll while holding\
      \ a weapon. _Response:_ The death knight adds 6 to its AC against that attack,\
      \ possibly causing it to miss."
    "name": "Parry"
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, the death knight can expend a use to take one of the following actions.\
  \ The death knight regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "The death knight uses Spellcasting to cast [[command-xphb|Command]].\
      \ The death knight can't take this action again until the start of its next\
      \ turn."
    "name": "Dread Authority"
  - "desc": "*Constitution Saving Throw:* DC 18, one creature the death knight can\
      \ see within 120 feet. *Failure:* 17 (5d6) Necrotic damage, and the target's\
      \ [[hit-points-xphb|Hit Point]] maximum decreases\
      \ by an amount equal to the damage taken. *Failure or Success:* The death knight\
      \ can't take this action again until the start of its next turn."
    "name": "Fell Word"
  - "desc": "The death knight moves up to half its [[speed-xphb|Speed]],\
      \ and it makes one Dread Blade attack."
    "name": "Lunge"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/undead/token/death-knight-xmm.webp"
```
^statblock
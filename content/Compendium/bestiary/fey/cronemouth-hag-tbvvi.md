---
title: Cronemouth Hag
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Cronemouth Hag"]
---
# Cronemouth Hag
*Source: Theros Bestiary TBVVI*  

Cronemouth Cove in the midst of perpetual doldrums and holds a known gate to the Underworld. It is guarded by a coven of sea hags who share a single tongue that is perpetually trying to escape from their clutches, wriggling out of reach with a mind of its own.

```statblock
"name": "Cronemouth Hag (TBVVI)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "49"
"hit_dice": "7d8 + 21"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "13"
  - !!int "16"
  - !!int "12"
  - !!int "12"
  - !!int "13"
"speed": "30 ft., swim 40 ft."
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Understands Common, Giant, and Primordial but can't speak"
"cr": "2"
"traits":
  - "desc": "The hag can breathe air and water."
    "name": "Amphibious"
  - "desc": "Any humanoid that starts its turn within 30 feet of the hag and can see the hag's true form must make a DC 11 Wisdom saving throw. On a failed save, the creature is [frightened](Compendium/rules/conditions.md#Frightened) for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) if the hag is within line of sight, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the hag's Horrific Appearance for the next 24 hours. Unless the target is surprised or the revelation of the hag's true form is sudden, the target can avert its eyes and avoid making the initial saving throw. Until the start of its next turn, a creature that averts its eyes has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) on attack rolls against the hag."
    "name": "Horrific Appearance"
  - "desc": "When hags must work together, they form covens, in spite of their selfish natures. A coven is made up of hags of any type, all of whom are equals within the group. However, each of the hags continues to desire more personal power. A coven consists of three hags so that any arguments between two hags can be settled by the third. If more than three hags ever come together, as might happen if two covens come into conflict, the result is usually chaos."
    "name": "Hag Coven"
  - "desc": "While all three members of a hag coven are within 30 feet of one another, they can each cast the following spells from the wizard's spell list but must share the spell slots among themselves: • 1st level (4 slots): [Identify](Compendium/spells/identify-xphb.md), ray of sickness • 2nd level (3 slots): [Hold Person](Compendium/spells/hold-person-xphb.md), locate object • 3rd level (3 slots): [Bestow Curse](Compendium/spells/bestow-curse-xphb.md), [Counterspell](Compendium/spells/counterspell-xphb.md), lightning bolt • 4th level (3 slots): [Phantasmal Killer](Compendium/spells/phantasmal-killer-xphb.md), polymorph • 5th level (2 slots): contact other plane, scrying • 6th level (1 slot): eye bite For casting these spells, each hag is a 12th-level spellcaster that uses Intelligence as her spellcasting ability. The spell save DC is 12+the hag's Intelligence modifier, and the spell attack bonus is 4+the hag's Intelligence modifier."
    "name": "Shared Spellcasting (Coven Only)"
  - "desc": "A hag coven can craft a magic creature called a hag tongue (see the hag tongue stat block), which is made from a real tongue and has a life of its own. A hag in the coven can take an action to put the tongue in her mouth and let it speak what the tongue would say. If it is destroyed, each coven member takes 3d10 psychic damage. A hag coven can have only one hag tongue at a time, and creating a new one requires all three members of the coven to perform a ritual. The ritual takes 1 hour, and it includes an incantation that must be spoken by another creature. During the ritual, if the participants take any action other than performing the ritual, they must start over."
    "name": "Hag Tongue (Coven Only)"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."
    "name": "Claws"
  - "desc": "The hag targets one [frightened](Compendium/rules/conditions.md#Frightened) creature she can see within 30 ft. of her. If the target can see the hag, it must succeed on a DC 11 Wisdom saving throw against this magic or drop to 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Death Glare"
  - "desc": "The hag covers herself and anything she is wearing or carrying with a magical illusion that makes her look like an ugly creature of her general size and humanoid shape. The effect ends if the hag takes a bonus action to end it or if she dies. The changes wrought by this effect fail to hold up to physical inspection. For example, the hag could appear to have no claws, but someone touching her hand might feel the claws. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a DC 16 Intelligence (Investigation) check to discern that the hag is disguised."
    "name": "Illusory Appearance"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/fey/token/cronemouth-hag-tbvvi.webp"
```
^statblock
---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/4
- monster/environment/underdark
- monster/size/large
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Bone Naga"
---
# Bone Naga
*Source: Monster Manual (2024) p. 53*
![](/Compendium/books/monster-manual-2025/img/bone-naga.webp#right)

## Bone Naga

*Deathless Serpentine Mind Bender*

- **Habitat.** Underdark  
- **Treasure.** [Relics](/Compendium/tables/random-magic-items-relics.md)  

Nagas are immortal but not invincible, and powerful magic can end their lives. Bone nagas are skeletal terrors raised from the remains of magically slain nagas or nagas that were killed but that hadn't yet rejuvenated. They are granted unlife through rituals practiced by cultists, yuan-ti, and morbid spirit nagas. These Undead nagas possess magical abilities similar to those they had in life, along with an eerie gaze that can beguile other creatures.

Bone nagas typically obey those who resurrected them, serving their creators as tireless guards and sharing the lore they collected in life. Undeath disrupts the perfect memory bone nagas enjoyed while alive, leaving them with gaps in their memories or details scrambled into puzzle-like jumbles.

In rare cases, bone nagas continue to pursue the goals they had while alive instead of serving other creatures. Most free-willed bone nagas are evil beings raised from spirit naga remains, but in unusual instances, bone nagas created from guardian nagas continue good, albeit confused, existences.

```statblock
"name": "Bone Naga"
"size": "Large"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "65"
"hit_dice": "10d10 + 10"
"modifier": !!int "3"
"stats":
  - !!int "15"
  - !!int "16"
  - !!int "12"
  - !!int "16"
  - !!int "15"
  - !!int "15"
"speed": "40 ft."
"damage_immunities": "poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 12"
"languages": "Common plus one other language"
"cr": "4"
"actions":
  - "desc": "The naga makes two Bite attacks. It can replace any attack with a use\
      \ of Serpentine Gaze."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 10 ft. *Hit:* 10 (2d6 + 3) Piercing damage\
      \ plus 7 (2d6) Necrotic damage."
    "name": "Bite"
  - "desc": "*Wisdom Saving Throw:* DC 13, one creature the naga can see within 60\
      \ feet. *Failure:* 13 (3d6 + 3) Psychic damage, and the target has the [Charmed](/Compendium/rules/conditions.md#Charmed)\
      \ condition until the start of the naga's next turn."
    "name": "Serpentine Gaze"
  - "desc": "The naga casts one of the following spells, requiring no Material components\
      \ and using Intelligence as the spellcasting ability (spell save DC 13):\n\n\
      **At will:** [Mage Hand](/Compendium/spells/mage-hand-xphb.md), [Thaumaturgy](/Compendium/spells/thaumaturgy-xphb.md)\n\
      \n**1/day each:** [Command](/Compendium/spells/command-xphb.md), [Detect Thoughts](/Compendium/spells/detect-thoughts-xphb.md),\
      \ [Lightning Bolt](/Compendium/spells/lightning-bolt-xphb.md)"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "/Compendium/bestiary/undead/token/bone-naga-xmm.webp"
```
^statblock

## Environment

underdark
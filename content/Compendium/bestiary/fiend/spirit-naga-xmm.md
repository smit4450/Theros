---
title: Spirit Naga
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/8
- monster/environment/lower
- monster/environment/planar
- monster/environment/underdark
- monster/size/large
- monster/type/fiend
statblock: inline
aliases: ["Spirit Naga"]
---
# Spirit Naga
*Source: Monster Manual (2024) p. 297. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fiend/img/spirit-naga.webp#right|850)  
## Spirit Naga

*Spiteful Serpentine Grudge Keeper*

- **Habitat.** Planar (Lower Planes), Underdark  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Spirit nagas loathe the world and all creatures. Possessing perfect memories, these venomous, cobra-like creatures recall every slight committed against them during their immortal existences. In their dank, joyless lairs, they create vicious plots to avenge themselves against even petty offenses.

Spirit nagas seek to claim what they believe they deserve. Their schemes often involve poisons, vile spells, cursed objects, or magical compulsions, eventually making them wellsprings of diabolical knowledge and evil inspiration. Other villains often seek out spirit nagas as advisers and allies. Roll on or choose a result from the Spirit Naga Grievances table to inspire what motivates a spirit naga's schemes.

**Spirit Naga Grievances**

| dice: 1d6 | The Spirit Naga Believes... |
|-----------|-----------------------------|
| 1 | A character is to blame for its recent failures. |
| 2 | It has been evicted from its rightful home. |
| 3 | Locals have reneged on an age-old bargain. |
| 4 | Other creatures are mocking it. |
| 5 | A rival is spying on it. |
| 6 | Someone's treasure rightfully belongs to it. |
^spirit-naga-grievances
```statblock
"name": "Spirit Naga (XMM)"
"size": "Large"
"type": "fiend"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"hp": !!int "135"
"hit_dice": "18d10 + 36"
"modifier": !!int "3"
"stats":
  - !!int "18"
  - !!int "17"
  - !!int "14"
  - !!int "16"
  - !!int "15"
  - !!int "16"
"speed": "40 ft."
"saves":
  - "dexterity": !!int "6"
  - "constitution": !!int "5"
  - "wisdom": !!int "5"
  - "charisma": !!int "6"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 12"
"languages": "Abyssal, Common"
"cr": "8"
"traits":
  - "desc": "If it dies, the naga returns to life in 1d6 days and regains all its\
      \ [[hit-points-xphb|Hit Points]]. Only a [[wish-xphb|Wish]]\
      \ spell can prevent this trait from functioning."
    "name": "Fiendish Restoration"
"actions":
  - "desc": "The naga makes three attacks, using Bite or Necrotic Ray in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 7 (1d6 + 4) Piercing\
      \ damage plus 14 (4d6) Poison damage."
    "name": "Bite"
  - "desc": "*Ranged Attack Roll:* +6, range 60 ft. *Hit:* 21 (6d6) Necrotic damage."
    "name": "Necrotic Ray"
  - "desc": "The naga casts one of the following spells, requiring no Somatic or Material\
      \ components and using Intelligence as the spellcasting ability (spell save\
      \ DC 14):\n\n**At will:** [[detect-magic-xphb|Detect Magic]],\
      \ [[mage-hand-xphb|Mage Hand]], [[minor-illusion-xphb|Minor Illusion]],\
      \ [[water-breathing-xphb|Water Breathing]]\n\n**2/day each:**\
      \ [[detect-thoughts-xphb|Detect Thoughts]], [[dimension-door-xphb|Dimension Door]],\
      \ [[hold-person-xphb|Hold Person]] (level 3 version), [[lightning-bolt-xphb|Lightning\
      \ Bolt]] (level 4 version)"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/spirit-naga-xmm.webp"
```
^statblock
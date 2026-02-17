---
title: Rakshasa
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/13
- monster/environment/nine-hells
- monster/environment/planar
- monster/environment/urban
- monster/size/medium
- monster/type/fiend
statblock: inline
aliases: ["Rakshasa"]
---
# Rakshasa
*Source: Monster Manual (2024) p. 253. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/rakshasa.webp#right)  
## Rakshasa

*Deceiver Hungry for Power and Flesh*

- **Habitat.** Planar (Nine Hells), Urban  
- **Treasure.** [[random-magic-items-relics|Relics]]  

Masters of manipulation, rakshasas infiltrate communities to claim positions of power. While disguising their true natures, they kidnap victims and indulge their insatiable hunger for flesh.

Rakshasas can withstand some degree of magic, but legends tell of blessed warriors felling them with crossbow bolts, arrows, or similar weapons.

Rakshasas' appearances combine humanlike bodies with the features of animals and monsters. All rakshasas have a physical oddity that remains when they adopt magical disguises, such as palms where the backs of the hands would be on humans.
```statblock
"name": "Rakshasa (XMM)"
"size": "Medium"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "17"
"hp": !!int "221"
"hit_dice": "26d8 + 104"
"modifier": !!int "8"
"stats":
  - !!int "14"
  - !!int "17"
  - !!int "18"
  - !!int "13"
  - !!int "16"
  - !!int "20"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+10"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+8"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+8"
"damage_vulnerabilities": "piercing damage from weapons wielded by creatures under\
  \ the effect of a Bless spell"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]]"
"senses": "[[senses#Truesight|Truesight]] 60 ft., passive Perception\
  \ 18"
"languages": "Common, Infernal"
"cr": "13"
"traits":
  - "desc": "The rakshasa automatically succeeds on saving throws against spells and\
      \ other magical effects, and the attack rolls of spells automatically miss it.\
      \ Without the rakshasa's permission, no spell can observe the rakshasa remotely\
      \ or detect its thoughts, creature type, or alignment."
    "name": "Greater Magic Resistance"
  - "desc": "If the rakshasa dies outside the Nine Hells, its body turns to ichor,\
      \ and it gains a new body instantly, reviving with all its [[hit-points-xphb|Hit Points]]\
      \ somewhere in the Nine Hells."
    "name": "Fiendish Restoration"
"actions":
  - "desc": "The rakshasa makes three Cursed Touch attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 5 ft. *Hit:* 12 (2d6 + 5) Slashing\
      \ damage plus 19 (3d12) Necrotic damage. If the target is a creature, it is\
      \ cursed. While cursed, the target gains no benefit from finishing a [[short-rest-xphb|Short]]\
      \ or [[long-rest-xphb|Long Rest]]."
    "name": "Cursed Touch"
  - "desc": "*Wisdom Saving Throw:* DC 18, each enemy in a 30-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the rakshasa. *Failure:* 28 (8d6) Psychic damage, and the\
      \ target has the [[conditions#Frightened|Frightened]] and\
      \ [[conditions#Incapacitated|Incapacitated]] conditions until\
      \ the start of the rakshasa's next turn."
    "name": "Baleful Command (Recharge 5-6)"
  - "desc": "The rakshasa casts one of the following spells, requiring no Material\
      \ components and using Charisma as the spellcasting ability (spell save DC 18):\n\
      \n**At will:** [[detect-magic-xphb|Detect Magic]], [[detect-thoughts-xphb|Detect\
      \ Thoughts]], [[disguise-self-xphb|Disguise Self]],\
      \ [[mage-hand-xphb|Mage Hand]], [[minor-illusion-xphb|Minor Illusion]]\n\
      \n**1/day each:** [[fly-xphb|Fly]], [[invisibility-xphb|Invisibility]],\
      \ [[major-image-xphb|Major Image]], [[plane-shift-xphb|Plane Shift]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/rakshasa-xmm.webp"
```
^statblock
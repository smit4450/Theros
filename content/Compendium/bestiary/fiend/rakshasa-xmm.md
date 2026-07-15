---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/13
- monster/environment/nine-hells
- monster/environment/planar
- monster/environment/urban
- monster/size/medium
- monster/type/fiend
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Rakshasa"
---
# Rakshasa
*Source: Monster Manual (2024) p. 253. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/books/monster-manual-2025/img/rakshasa.webp#right)

## Rakshasa

*Deceiver Hungry for Power and Flesh*

- **Habitat.** Planar (Nine Hells), Urban  
- **Treasure.** [Relics](/Compendium/tables/random-magic-items-relics.md)  

Masters of manipulation, rakshasas infiltrate communities to claim positions of power. While disguising their true natures, they kidnap victims and indulge their insatiable hunger for flesh.

Rakshasas can withstand some degree of magic, but legends tell of blessed warriors felling them with crossbow bolts, arrows, or similar weapons.

Rakshasas' appearances combine humanlike bodies with the features of animals and monsters. All rakshasas have a physical oddity that remains when they adopt magical disguises, such as palms where the backs of the hands would be on humans.

```statblock
"name": "Rakshasa"
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
  - "name": "[Deception](/Compendium/rules/skills.md#Deception)"
    "desc": "+10"
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+8"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+8"
"damage_vulnerabilities": "piercing damage from weapons wielded by creatures under\
  \ the effect of a Bless spell"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [frightened](/Compendium/rules/conditions.md#Frightened)"
"senses": "[Truesight](/Compendium/rules/senses.md#Truesight) 60 ft., passive Perception\
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
      \ and it gains a new body instantly, reviving with all its [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ somewhere in the Nine Hells."
    "name": "Fiendish Restoration"
"actions":
  - "desc": "The rakshasa makes three Cursed Touch attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 5 ft. *Hit:* 12 (2d6 + 5) Slashing damage\
      \ plus 19 (3d12) Necrotic damage. If the target is a creature, it is cursed.\
      \ While cursed, the target gains no benefit from finishing a [Short](/Compendium/rules/variant-rules/short-rest-xphb.md)\
      \ or [Long Rest](/Compendium/rules/variant-rules/long-rest-xphb.md)."
    "name": "Cursed Touch"
  - "desc": "*Wisdom Saving Throw:* DC 18, each enemy in a 30-foot [Emanation](/Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
      \ originating from the rakshasa. *Failure:* 28 (8d6) Psychic damage, and the\
      \ target has the [Frightened](/Compendium/rules/conditions.md#Frightened) and\
      \ [Incapacitated](/Compendium/rules/conditions.md#Incapacitated) conditions\
      \ until the start of the rakshasa's next turn."
    "name": "Baleful Command (Recharge 5-6)"
  - "desc": "The rakshasa casts one of the following spells, requiring no Material\
      \ components and using Charisma as the spellcasting ability (spell save DC 18):\n\
      \n**At will:** [Detect Magic](/Compendium/spells/detect-magic-xphb.md), [Detect\
      \ Thoughts](/Compendium/spells/detect-thoughts-xphb.md), [Disguise Self](/Compendium/spells/disguise-self-xphb.md),\
      \ [Mage Hand](/Compendium/spells/mage-hand-xphb.md), [Minor Illusion](/Compendium/spells/minor-illusion-xphb.md)\n\
      \n**1/day each:** [Fly](/Compendium/spells/fly-xphb.md), [Invisibility](/Compendium/spells/invisibility-xphb.md),\
      \ [Major Image](/Compendium/spells/major-image-xphb.md), [Plane Shift](/Compendium/spells/plane-shift-xphb.md)"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "/Compendium/bestiary/fiend/token/rakshasa-xmm.webp"
```
^statblock

## Environment

planar, nine hells, urban
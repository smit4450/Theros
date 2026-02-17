---
title: Death Cultist
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/8
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid
statblock: inline
aliases: ["Death Cultist"]
---
# Death Cultist
*Source: Monster Manual (2024) p. 86*  

![](Compendium/bestiary/humanoid/img/cultists.webp#right|850)  
Death cultists revel in nihilistic forces, embracing them as paths to undeath, multiversal purity, or entropic inevitability. These cultists serve powerful undead beings, apocalyptic prophecies, or immortals with power over death, such as Acererak, Kyuss, Orcus, Vecna, or Wee Jas.

## Cultists

*Doomsayers and Fanatics*

- **Habitat.** Any  
- **Treasure.** Individual, [[random-magic-items-relics|Relics]]  

Cultists use magic and extreme measures to spread radical beliefs. Some privately pursue esoteric secrets, while others form shadowy cabals seeking to bring about terrifying ends. Cultists often follow obscure mystical traditions or obsess over interpretations of ancient prophecies. They might worship supernatural patrons—deities, otherworldly creatures, manipulative alien minds, or stranger forces. Roll on or choose a result from the Cultist Agendas table to inspire what a cultist seeks to achieve.

**Cultist Agendas**

| dice: 1d6 | The Cultist Strives To... |
|-----------|---------------------------|
| 1 | Bring about the end of a dominant order, an age, or the world. |
| 2 | Burn away the comfortable lies of reality, revealing forgotten or terrible truths. |
| 3 | Expand their faith though mind control or supernatural coercion. |
| 4 | Make global changes, like sinking the land or awakening volcanoes. |
| 5 | Remake life on a mass scale, altering other creatures' bodies or spiritual beings. |
| 6 | Summon their deity or its herald, weapon, or realm into their world. |
^cultist-agendas

### Occult Symbols

Cults often identify with symbols that exemplify their beliefs. Such symbols might mark objects important to the cult, as well as the dress and bodies of cultists themselves. These symbols might be broadly understandable, or they might have meaning only to cultists. Roll twice on or choose results from the Cult Symbols table to inspire a cult's icons.

**Cult Symbols**

| dice: 1d10 | The Symbol Is... | Depicted As... |
|------------|------------------|----------------|
| 1 | An alchemical sign | A calendar or map |
| 2 | An animal | A crest or as heraldry |
| 3 | A celestial body | An elaborate diagram |
| 4 | A deity's icon | A metaphorical image |
| 5 | An element | A mystical being |
| 6 | An eye | Part of an equation |
| 7 | A geometric shape | A repeating pattern |
| 8 | A letter or number | A series of scratches |
| 9 | Part of a monster | A simple pictogram |
| 10 | A skull | A weapon or tool |
^cult-symbols

### Cult Members

Cults often form hierarchies around a charismatic or domineering leader. While cult members might work independently, they take their orders from superiors with greater supernatural powers. 

### Types of Cultists

Cults can organize around any mystical tradition, but many serve supernatural beings. Cult members often have abilities tied to the forces they worship.

> [!quote] A quote from Rites of the Cult of Elemental Evil  
> 
> Dread Tharizdun, power of the Elder Elemental Eye and master of all destructive forces, I am the Champion of Elemental Evil and am ready to carry out your wishes.

## Statblock

```statblock
"name": "Death Cultist (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral Evil"
"ac": !!int "17"
"hp": !!int "127"
"hit_dice": "15d8 + 60"
"modifier": !!int "4"
"stats":
  - !!int "19"
  - !!int "12"
  - !!int "18"
  - !!int "12"
  - !!int "16"
  - !!int "14"
"speed": "30 ft."
"saves":
  - "constitution": !!int "7"
  - "wisdom": !!int "6"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+6"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+4"
"senses": "passive Perception 16"
"languages": "Common"
"cr": "8"
"actions":
  - "desc": "The cultist makes three attacks, using Dread Scythe or Deathly Ray in\
      \ any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 9 (1d10 + 4) Slashing\
      \ damage plus 11 (2d10) Necrotic damage, and the target can't regain [[hit-points-xphb|Hit\
      \ Points]] until the end of\
      \ its next turn."
    "name": "Dread Scythe"
  - "desc": "*Ranged Attack Roll:* +6, range 120 ft. *Hit:* 22 (4d10) Necrotic\
      \ damage."
    "name": "Deathly Ray"
  - "desc": "The cultist casts one of the following spells, using Wisdom as the spellcasting\
      \ ability (spell save DC 14):\n\n**At will:** [[speak-with-dead-xphb|Speak with Dead]],\
      \ [[thaumaturgy-xphb|Thaumaturgy]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "*Wisdom Saving Throw:* DC 14, each creature in a 20-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the cultist. *Failure:* 14 (4d6) Psychic damage, and the\
      \ target has the [[conditions#Frightened|Frightened]] condition\
      \ until the end of its next turn. *Success:* Half damage only."
    "name": "Spirit Wail (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/death-cultist-xmm.webp"
```
^statblock
---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/25
- monster/environment/any
- monster/size/gargantuan
- monster/type/construct/titan
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Colossus"
---
# Colossus
*Source: Monster Manual (2024) p. 76*
![](/Compendium/bestiary/construct/img/colossus.webp#right)

## Colossus

*Titanic Vessel of Divine Might*

- **Habitat.** Any  
- **Treasure.** [Relics](/Compendium/tables/random-magic-items-relics.md)  

Colossi are massive Constructs created by the devout to reflect the nature of a deity, which could be benevolent or wicked. Colossi thrum with incredible magic and work divine will on the land.

Droves of faithful artisans craft a colossus in a shape to honor their deity, then call on that god to infuse the statue with life. This arduous process might take decades and involve hundreds of workers. If the god favors the creation, the mighty crystal at the construct's heart pulses with divine power, and the colossus rises to protect the faithful or enact the god's will.

Most colossi were created in ages past and now lie dormant in secluded wilderness, awakening only when disturbed or called on to serve once more.

```statblock
"name": "Colossus"
"size": "Gargantuan"
"type": "construct"
"subtype": "titan"
"alignment": "Unaligned"
"ac": !!int "23"
"hp": !!int "553"
"hit_dice": "27d20 + 270"
"modifier": !!int "16"
"stats":
  - !!int "30"
  - !!int "11"
  - !!int "30"
  - !!int "3"
  - !!int "11"
  - !!int "8"
"speed": "60 ft."
"saves":
  - "dexterity": !!int "8"
  - "wisdom": !!int "8"
"damage_resistances": "necrotic, radiant"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](/Compendium/rules/conditions.md#Petrified), [poisoned](/Compendium/rules/conditions.md#Poisoned),\
  \ [stunned](/Compendium/rules/conditions.md#Stunned), [unconscious](/Compendium/rules/conditions.md#Unconscious)"
"senses": "[Truesight](/Compendium/rules/senses.md#Truesight) 300 ft., passive Perception\
  \ 10"
"languages": "understands Celestial and Common but can't speak"
"cr": "25"
"traits":
  - "desc": "The colossus can't shape-shift."
    "name": "Immutable Form"
  - "desc": "If the colossus fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (4/Day)"
  - "desc": "The colossus has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The colossus deals double damage to objects and structures."
    "name": "Siege Monster"
"actions":
  - "desc": "The colossus makes three attacks, using Slam or Radiant Ray in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +18, reach 20 ft. *Hit:* 32 (4d10 + 10) Bludgeoning\
      \ damage, and the colossus pushes the target up to 20 feet straight away from\
      \ itself."
    "name": "Slam"
  - "desc": "*Ranged Attack Roll:* +18, range 300 ft. *Hit:* 22 (4d10) Radiant damage.\
      \ If the target is a Large or smaller creature, it has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Radiant Ray"
  - "desc": "*Dexterity Saving Throw:* DC 26, each creature in a 300-foot-long, 10-foot-wide\
      \ [Line](/Compendium/rules/variant-rules/line-area-of-effect-xphb.md). *Failure:*\
      \ 65 (10d12) Radiant damage. *Success:* Half damage. *Failure or Success:* A\
      \ creature reduced to 0 [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ by this beam disintegrates into dust, leaving behind any magic items it was\
      \ wearing or carrying."
    "name": "Divine Beam (Recharge 5-6)"
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, the colossus can expend a use to take one of the following actions. The\
  \ colossus regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "The colossus makes one Radiant Ray attack."
    "name": "Smite"
  - "desc": "The colossus moves up to half its [Speed](/Compendium/rules/variant-rules/speed-xphb.md)\
      \ without provoking [Opportunity Attacks](/Compendium/rules/actions.md#Opportunity%20Attack),\
      \ and it can make one Slam attack at any point during that move."
    "name": "Stomp"
"source":
  - "XMM"
"image": "/Compendium/bestiary/construct/token/colossus-xmm.webp"
```
^statblock

## Environment

any
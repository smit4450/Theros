---
title: Salamander Inferno Master
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/15
- monster/environment/fire
- monster/environment/planar
- monster/environment/underdark
- monster/size/large
- monster/type/elemental
statblock: inline
aliases: ["Salamander Inferno Master"]
---
# Salamander Inferno Master
*Source: Monster Manual (2024) p. 267*  

![](Compendium/bestiary/elemental/img/salamander-inferno-master.webp#right|850)  
Salamander inferno masters are ancient connoisseurs of flames and often inhabit places with unique scorching properties. They gather communes of apprentices who learn fiery techniques while helping their mentors accomplish great works. Inferno masters have ambitious goals, such as causing massive volcanic eruptions, opening portals to burning planes, destroying Artifacts, or burning all instances of something from the multiverse.

## Salamanders

*Serpentine Artists of the Inferno*

- **Habitat.** Planar (Elemental Plane of Fire), Underdark  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Salamanders are serpentine denizens of the Elemental Plane of Fire. They believe that flames expose the purest forms of all things and delight in burning and melting things, seeing fleeting beauty and striking nuances in blazes consuming different fuels—ancient forests, artistic masterpieces, or living creatures. To salamanders, those that can't endure their flames are nothing but ashes in disguise. They harbor malice toward few creatures, but they consider creating remarkable flames more important than the pain and loss their fires cause.

Salamanders are typically content to dwell on the Elemental Plane of Fire, creating strange, temporary art amid the flames. Some travel to other planes of existence and worlds to experience the flames of other realms or create conflagrations of unprecedented scale.

> [!quote] A quote from Filiag Highthumbs  
> 
> The salamanders of the Elemental Plane of Fire delight in meeting visitors from other realms. For them, every stranger is a potential addition to their fiery artistry. Don't fall for their flattery, no matter how beautifully they say you'll burn.

![A salamander inferno maste...](Compendium/bestiary/elemental/img/salamanders.webp#center)  
## Statblock

```statblock
"name": "Salamander Inferno Master (XMM)"
"size": "Large"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "18"
"hp": !!int "256"
"hit_dice": "27d10 + 108"
"modifier": !!int "8"
"stats":
  - !!int "24"
  - !!int "16"
  - !!int "18"
  - !!int "14"
  - !!int "10"
  - !!int "20"
"speed": "40 ft., climb 40 ft."
"saves":
  - "dexterity": !!int "8"
  - "wisdom": !!int "5"
"damage_vulnerabilities": "cold"
"damage_immunities": "fire"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 10"
"languages": "Primordial (Ignan)"
"cr": "15"
"traits":
  - "desc": "At the end of each of the salamander's turns, each creature of the salamander's\
      \ choice in a 10-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the salamander takes 10 (3d6) Fire damage."
    "name": "Fire Aura"
  - "desc": "The salamander has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The salamander makes two Flame Trident attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +12, reach 5 ft. or range 30/90 ft.\
      \ *Hit:* 16 (2d8 + 7) Piercing damage plus 14 (4d6) Fire damage. *Hit or\
      \ Miss:* The trident magically returns to the salamander's hand immediately\
      \ after a ranged attack."
    "name": "Flame Trident"
  - "desc": "*Dexterity Saving Throw:* DC 18, each creature in a 30-foot-radius [[sphere-area-of-effect-xphb|Sphere]]\
      \ centered on a point the salamander can see within 120 feet. *Failure:* 35\
      \ (10d6) Fire damage, and the target starts [[burning-xphb|burning]],\
      \ taking 5 (1d10) Fire damage at the start of each of its turns instead of\
      \ the normal [[burning-xphb|burning]] damage. The\
      \ target gains 1 [[conditions#Exhaustion|Exhaustion]] level\
      \ whenever it takes this [[burning-xphb|burning]]\
      \ damage. *Success:* Half damage only."
    "name": "Inferno Blast (Recharge 5-6)"
"bonus_actions":
  - "desc": "The salamander moves up to its [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]].\
      \ During this movement, fire fills a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the salamander. When the [[emanation-area-of-effect-xphb|Emanation]]\
      \ enters a creature's space, that creature takes 7 (2d6) Fire damage. A creature\
      \ can take this damage only once per turn."
    "name": "Blazing Movement"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/salamander-inferno-master-xmm.webp"
```
^statblock
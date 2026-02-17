---
title: Sea Hag
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/coastal
- monster/environment/underwater
- monster/size/medium
- monster/type/fey
statblock: inline
aliases: ["Sea Hag"]
---
# Sea Hag
*Source: Monster Manual (2024) p. 271. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/sea-hag.webp#right)  
## Sea Hag

*Hag of Despair and the Dismal Deep*

- **Habitat.** Coastal, Underwater  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Sea hags loathe peace and beauty. Bitter, jealous creatures, they spread chaos and undermine joy however they can, undertaking elaborate deceptions to sow discord for its own sake. The hags' true forms are supernaturally vile, and their baleful gazes can strike down creatures [[conditions#Frightened|frightened]] by their appearance.

Sea hags cloak themselves in illusions to work their schemes. Roll on or choose a result from the Sea Hag Disguises table to inspire a sea hag's illusion and how they might use it to wreak chaos and destruction.

**Sea Hag Disguises**

| dice: 1d6 | The Sea Hag Takes the Form of A... |
|-----------|------------------------------------|
| 1 | Captive and claims nearby villagers bound them and left them to drown. |
| 2 | Castaway and shares a cursed item's location with would-be rescuers. |
| 3 | Healer and passes off poisons as medicine. |
| 4 | Panic-spreading prophesier of doom. |
| 5 | Ship captain and delivers passengers to the hag's pet sea monster. |
| 6 | Wounded sailor and claims their ship was destroyed by merfolk or other peaceful people. |
^sea-hag-disguises
```statblock
"name": "Sea Hag (XMM)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "52"
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
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 11"
"languages": "Common, Giant, Primordial (Aquan)"
"cr": "2"
"traits":
  - "desc": "While within 30 feet of at least two hag allies, the hag can cast one\
      \ of the following spells, requiring no Material components, using the spell's\
      \ normal casting time, and using Intelligence as the spellcasting ability (spell\
      \ save DC 11): [[augury-xphb|Augury]], [[find-familiar-xphb|Find Familiar]],\
      \ [[identify-xphb|Identify]], [[locate-object-xphb|Locate Object]],\
      \ [[scrying-xphb|Scrying]], or [[unseen-servant-xphb|Unseen Servant]].\
      \ The hag must finish a [[long-rest-xphb|Long Rest]]\
      \ before using this trait to cast that spell again.\n"
    "name": "Coven Magic"
  - "desc": "The hag can breathe air and water."
    "name": "Amphibious"
  - "desc": "*Wisdom Saving Throw:* DC 11, any Beast or Humanoid that starts its turn\
      \ within 30 feet of the hag and can see the hag's true form. *Failure:* The\
      \ target has the [[conditions#Frightened|Frightened]] condition\
      \ until the start of its next turn. *Success:* The target is immune to this\
      \ hag's Vile Appearance for 24 hours."
    "name": "Vile Appearance"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 10 (2d6 + 3) Slashing\
      \ damage."
    "name": "Claw"
  - "desc": "*Wisdom Saving Throw:* DC 11, one [[conditions#Frightened|Frightened]]\
      \ creature the hag can see within 30 feet. *Failure:* If the target has 20 [[hit-points-xphb|Hit\
      \ Points]] or fewer, it drops\
      \ to 0 [[hit-points-xphb|Hit Points]]. Otherwise,\
      \ the target takes 13 (3d8) Psychic damage."
    "name": "Death Glare (Recharge 5-6)"
  - "desc": "The hag casts [[disguise-self-xphb|Disguise Self]],\
      \ using Constitution as the spellcasting ability (spell save DC 13). The spell's\
      \ duration is 24 hours.\n"
    "name": "Illusory Appearance"
"source":
  - "XMM"
"image": "Compendium/bestiary/fey/token/sea-hag-xmm.webp"
```
^statblock
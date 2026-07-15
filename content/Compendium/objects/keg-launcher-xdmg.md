---
obsidianUIMode: preview
cssclasses:
- json5e-object
tags:
- compendium/src/5e/xdmg
- object/size/large
- object/type/siege-weapon
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Keg Launcher"
---
# Keg Launcher
*Source: Dungeon Master's Guide (2024) p. 96*

![](/Compendium/objects/img/keg-launcher.webp#right)

A back-mounted, wooden catapult flings small kegs of toxic gas. Loading a Keg Launcher requires the [Utilize](/Compendium/rules/actions.md#Utilize) action, and aiming it requires another [Utilize](/Compendium/rules/actions.md#Utilize) action. Then a crew member can take the Toxic Keg action.
```statblock
"name": "Keg Launcher"
"size": "Large"
"ac": !!int "15"
"hp": !!int "30"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Constitution Saving Throw: DC 15, each creature in a 20-foot-radius\
      \ [Sphere](/Compendium/rules/variant-rules/sphere-area-of-effect-xphb.md) centered\
      \ on a point 30 to 300 feet from the launcher. Failure: 14 (4d6) Poison damage.\
      \ Success: Half damage."
    "name": "Toxic Keg (Requires Load and Aim)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/keg-launcher-xdmg.webp"
```
^statblock
// @ts-ignore
import spellTableScript from "./scripts/spelltable.inline"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const SpellTable: QuartzComponent = (_props: QuartzComponentProps) => {
  return null
}

SpellTable.afterDOMLoaded = spellTableScript

export default (() => SpellTable) satisfies QuartzComponentConstructor

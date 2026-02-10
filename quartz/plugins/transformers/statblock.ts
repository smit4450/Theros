import { QuartzTransformerPlugin } from "../types"
import { Code } from "mdast"
import { Root as HtmlRoot, Element } from "hast"
import { SKIP, visit } from "unist-util-visit"
import { Root } from "mdast"

// @ts-ignore
import statblockScript from "../../components/scripts/statblock.inline"
import statblockStyle from "../../components/styles/statblock.inline.scss"

interface Options {
  /** The default layout to use when none is specified. Currently only "Basic 5e Layout" is supported. */
  defaultLayout: string
}

const defaultOptions: Options = {
  defaultLayout: "Basic 5e Layout",
}

export const FantasyStatblocks: QuartzTransformerPlugin<Partial<Options>> = (userOpts) => {
  const opts = { ...defaultOptions, ...userOpts }

  return {
    name: "FantasyStatblocks",
    markdownPlugins() {
      return [
        () => {
          return (tree: Root, file) => {
            visit(tree, "code", (node: Code) => {
              if (node.lang === "statblock") {
                file.data.hasStatblock = true
                // Store the raw YAML in a data attribute so the client-side
                // renderer can parse it. We also set a className to identify
                // these blocks after rehype conversion.
                node.data = {
                  hProperties: {
                    className: ["fantasy-statblock-data"],
                    "data-statblock-yaml": node.value,
                    "data-default-layout": opts.defaultLayout,
                  },
                }
              }
            })
          }
        },
      ]
    },
    htmlPlugins() {
      return [
        () => {
          return (tree: HtmlRoot) => {
            visit(tree, "element", (node: Element, index, parent) => {
              // After rehype, fenced code blocks become <pre><code>...</code></pre>.
              // We need to find <code> elements with our marker class and replace
              // the entire <pre> with a statblock container div.
              if (node.tagName === "code") {
                const classes = (node.properties?.className ?? []) as string[]
                if (classes.includes("fantasy-statblock-data")) {
                  const yaml = node.properties?.["dataStatblockYaml"] as string | undefined
                  const layout = node.properties?.["dataDefaultLayout"] as string | undefined

                  if (yaml && parent && typeof index === "number") {
                    // Replace the parent <pre> element (or the code element itself
                    // if there is no <pre> wrapper) with a container div
                    const parentIsElement = parent.type === "element" && "tagName" in parent
                    const parentIsPre = parentIsElement && (parent as Element).tagName === "pre"
                    const target = parentIsPre ? parent as Element : node
                    const targetParent = parentIsPre
                      ? findParent(tree, parent as Element)
                      : parent
                    const targetIndex = parentIsPre
                      ? findIndex(targetParent as (HtmlRoot | Element | null), target)
                      : index

                    if (targetParent && typeof targetIndex === "number") {
                      const replacement: Element = {
                        type: "element",
                        tagName: "div",
                        properties: {
                          className: ["fantasy-statblock-container"],
                          "data-statblock-yaml": yaml,
                          "data-default-layout": layout ?? opts.defaultLayout,
                        },
                        children: [
                          {
                            type: "element",
                            tagName: "noscript",
                            properties: {},
                            children: [
                              {
                                type: "element",
                                tagName: "pre",
                                properties: {},
                                children: [
                                  {
                                    type: "element",
                                    tagName: "code",
                                    properties: {},
                                    children: [{ type: "text", value: yaml }],
                                  },
                                ],
                              },
                            ],
                          },
                        ],
                      }

                      targetParent.children.splice(targetIndex, 1, replacement)
                      return SKIP
                    }
                  }
                }
              }
            })
          }
        },
      ]
    },
    externalResources() {
      return {
        js: [
          {
            script: statblockScript,
            loadTime: "afterDOMReady",
            contentType: "inline",
          },
        ],
        css: [
          {
            content: statblockStyle,
            inline: true,
          },
        ],
      }
    },
  }
}

/** Walk the tree to find the parent of a given node. */
function findParent(
  tree: HtmlRoot | Element,
  target: Element,
): (HtmlRoot | Element) | null {
  if ("children" in tree) {
    for (const child of tree.children) {
      if (child === target) return tree
      if ("children" in child) {
        const found = findParent(child as Element, target)
        if (found) return found
      }
    }
  }
  return null
}

/** Find the index of a child node in a parent. */
function findIndex(
  parent: HtmlRoot | Element | null,
  target: Element | HtmlRoot,
): number | null {
  if (!parent || !("children" in parent)) return null
  const idx = parent.children.indexOf(target as any)
  return idx >= 0 ? idx : null
}

declare module "vfile" {
  interface DataMap {
    hasStatblock: boolean | undefined
  }
}

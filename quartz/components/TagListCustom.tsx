import { FullSlug, resolveRelative } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

/**
 * Extracts the display name from a tag by taking only the last segment.
 * For example: "ttrpg-cli/spell/class/sorcerer" becomes "sorcerer"
 */
function getTagDisplayName(tag: string): string {
  const segments = tag.split("/")
  return segments[segments.length - 1]
}

const TagListCustom: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const tags = fileData.frontmatter?.tags
  if (tags && tags.length > 0) {
    return (
      <ul class={classNames(displayClass, "tags")}>
        {tags.map((tag) => {
          const linkDest = resolveRelative(fileData.slug!, `tags/${tag}` as FullSlug)
          const displayName = getTagDisplayName(tag)
          return (
            <li>
              <a href={linkDest} class="internal tag-link" title={tag}>
                {displayName}
              </a>
            </li>
          )
        })}
      </ul>
    )
  } else {
    return null
  }
}

TagListCustom.css = `
.tags {
  list-style: none;
  display: flex;
  padding-left: 0;
  gap: 0.4rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.section-li > .section > .tags {
  justify-content: flex-end;
}
  
.tags > li {
  display: inline-block;
  white-space: nowrap;
  margin: 0;
  overflow-wrap: normal;
}

a.internal.tag-link {
  border-radius: 8px;
  background-color: var(--highlight);
  padding: 0.2rem 0.4rem;
  margin: 0 0.1rem;
}
`

export default (() => TagListCustom) satisfies QuartzComponentConstructor

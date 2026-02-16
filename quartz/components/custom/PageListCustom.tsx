import { FullSlug, isFolderPath, resolveRelative } from "../../util/path"
import { QuartzPluginData } from "../../plugins/vfile"
import { Date, getDate } from "../Date"
import { QuartzComponent, QuartzComponentProps } from "../types"
import { GlobalConfiguration } from "../../cfg"

export type SortFn = (f1: QuartzPluginData, f2: QuartzPluginData) => number

/**
 * Extracts the display name from a tag by taking only the last segment.
 * For example: "ttrpg-cli/spell/class/sorcerer" becomes "sorcerer"
 */
export function getTagDisplayName(tag: string): string {
  const segments = tag.split("/")
  return segments[segments.length - 1]
}

export function byDateAndAlphabetical(cfg: GlobalConfiguration): SortFn {
  return (f1, f2) => {
    // Sort by date/alphabetical
    if (f1.dates && f2.dates) {
      // sort descending
      return getDate(cfg, f2)!.getTime() - getDate(cfg, f1)!.getTime()
    } else if (f1.dates && !f2.dates) {
      // prioritize files with dates
      return -1
    } else if (!f1.dates && f2.dates) {
      return 1
    }

    // otherwise, sort lexographically by title
    const f1Title = f1.frontmatter?.title.toLowerCase() ?? ""
    const f2Title = f2.frontmatter?.title.toLowerCase() ?? ""
    return f1Title.localeCompare(f2Title)
  }
}

export function byDateAndAlphabeticalFolderFirst(cfg: GlobalConfiguration): SortFn {
  return (f1, f2) => {
    // Sort folders first
    const f1IsFolder = isFolderPath(f1.slug ?? "")
    const f2IsFolder = isFolderPath(f2.slug ?? "")
    if (f1IsFolder && !f2IsFolder) return -1
    if (!f1IsFolder && f2IsFolder) return 1

    // If both are folders or both are files, sort by date/alphabetical
    if (f1.dates && f2.dates) {
      // sort descending
      return getDate(cfg, f2)!.getTime() - getDate(cfg, f1)!.getTime()
    } else if (f1.dates && !f2.dates) {
      // prioritize files with dates
      return -1
    } else if (!f1.dates && f2.dates) {
      return 1
    }

    // otherwise, sort lexographically by title
    const f1Title = f1.frontmatter?.title.toLowerCase() ?? ""
    const f2Title = f2.frontmatter?.title.toLowerCase() ?? ""
    return f1Title.localeCompare(f2Title)
  }
}

type Props = {
  limit?: number
  sort?: SortFn
} & QuartzComponentProps

export const PageListCustom: QuartzComponent = ({ cfg, fileData, allFiles, limit, sort }: Props) => {
  const sorter = sort ?? byDateAndAlphabeticalFolderFirst(cfg)
  let list = allFiles.sort(sorter)
  if (limit) {
    list = list.slice(0, limit)
  }

  return (
    <ul class="section-ul">
      {list.map((page) => {
        const title = page.frontmatter?.title
        const tags = page.frontmatter?.tags ?? []

        return (
          <li class="section-li">
            <div class="section">
              <p class="meta">
                {page.dates && <Date date={getDate(cfg, page)!} locale={cfg.locale} />}
              </p>
              <div class="desc">
                <h3>
                  <a href={resolveRelative(fileData.slug!, page.slug!)} class="internal">
                    {title}
                  </a>
                </h3>
                <ul class="tags">
                  {tags.map((tag) => {
                    const displayName = getTagDisplayName(tag)
                    return (
                      <li>
                        <a
                          class="internal tag-link"
                          href={resolveRelative(fileData.slug!, `tags/${tag}` as FullSlug)}
                          title={tag}
                        >
                          {displayName}
                        </a>
                      </li>
                    )
                  })}
                </ul>
              </div>
            </div>
          </li>
        )
      })}
    </ul>
  )
}

PageListCustom.css = `
.section h3 {
  margin: 0;
  display: inline;
}

.section .desc {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.5rem;
}

.section .desc .tags {
  display: inline-flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.section .desc .tags li {
  display: inline-block;
  margin: 0;
}

@media (max-width: 800px) {
  li.section-li > .section {
    grid-template-columns: fit-content(8em) 1fr;
  }

  .section .desc .tags {
    display: none;
  }
}
`

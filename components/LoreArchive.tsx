// ⚔️ LoreArchive: Static-build lore conjuration with hydration-safe output.
// Generates deterministic HTML at build/export time and reuses it verbatim client-side
// to avoid hydration mismatches (no client FS access or recomputation).
let fs: any = null
let path: any = null
try {
  if (typeof window === 'undefined') {
    fs = require('fs')
    path = require('path')
  }
} catch {
  /* ignore in client bundle */
}
import matter from 'gray-matter'
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkGfm from 'remark-gfm'
import remarkRehype from 'remark-rehype'
import rehypeStringify from 'rehype-stringify'

interface LoreFileMeta {
  index: number
  filename: string
  title: string
  content: string // original markdown
  html: string // rendered HTML
  tags?: string[]
  draft?: boolean
  order?: number
}

const LORE_DIR =
  typeof window === 'undefined' && path ? path.join(process.cwd(), '_LORE_') : '_LORE_'
const FILE_PATTERN = /^(\d+)[-_].*\.(md|MD|mdx)$/

function renderMarkdown(md: string): string {
  const file = unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkRehype)
    .use(rehypeStringify)
    .processSync(md)
  return String(file)
}

let CACHE: LoreFileMeta[] | null = null

function slugify(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .slice(0, 80)
}

function loadLoreFiles(): LoreFileMeta[] {
  if (CACHE) return CACHE
  if (!fs || !path) {
    CACHE = []
    return CACHE
  }
  if (!fs.existsSync(LORE_DIR)) {
    CACHE = []
    return CACHE
  }
  const entries = fs.readdirSync(LORE_DIR, { withFileTypes: true })
  const lore: LoreFileMeta[] = []
  for (const ent of entries) {
    if (!ent.isFile()) continue
    const match = FILE_PATTERN.exec(ent.name)
    if (!match) continue
    const index = parseInt(match[1], 10)
    const fullPath = path.join(LORE_DIR, ent.name)
    const raw = fs.readFileSync(fullPath, 'utf-8')
    const parsed = matter(raw)
    const body = parsed.content.trim()
    const firstHeading = body
      .split(/\r?\n/)
      .find((l: string) => l.trim().startsWith('#'))
      ?.replace(/^#+\s*/, '')
      .trim()
    const metaTitle = (parsed.data.title as string) || firstHeading || ent.name
    const order = typeof parsed.data.order === 'number' ? parsed.data.order : undefined
    const draft = parsed.data.draft === true
    let tags: string[] | undefined
    if (Array.isArray(parsed.data.tags)) {
      tags = (parsed.data.tags as any[]).map((t: any) => String(t))
    }
    if (draft) continue
    const html = renderMarkdown(body)
    lore.push({
      index,
      filename: ent.name,
      title: metaTitle,
      content: body,
      html,
      tags,
      draft,
      order,
    })
  }
  CACHE = lore.sort((a, b) => {
    if (a.order != null && b.order != null) return a.order - b.order
    if (a.order != null) return -1
    if (b.order != null) return 1
    return a.index - b.index
  })
  return CACHE
}

// Inline styles retained for portability.
const containerStyle: React.CSSProperties = { marginTop: '3rem' }
const tocStyle: React.CSSProperties = {
  listStyle: 'none',
  padding: 0,
  margin: '0.5rem 0 1.5rem',
  display: 'grid',
  gap: '0.25rem',
  fontSize: '0.9rem',
}
const detailsStyle: React.CSSProperties = {
  border: '1px solid #9333ea',
  borderRadius: '10px',
  padding: '0.75rem 1rem',
  marginBottom: '1rem',
  background: 'rgba(0,0,0,0.45)',
}
const summaryStyle: React.CSSProperties = {
  cursor: 'pointer',
  fontWeight: 600,
  color: '#fbbf24',
  display: 'flex',
  gap: '0.5rem',
  alignItems: 'center',
}
const metaStyle: React.CSSProperties = {
  fontSize: '0.65rem',
  color: '#c084fc',
  margin: '0.4rem 0 0.8rem',
}

function buildStaticHTML(): string {
  const lore = loadLoreFiles()
  if (!lore.length) {
    return '<p><em>No lore fragments discovered. Add files to <code>_LORE_</code>.</em></p>'
  }
  const slugs = lore.map((l) => ({ ...l, slug: slugify(l.title) }))
  const toc =
    `<nav aria-label="Lore index"><strong style="font-size:0.85rem;letter-spacing:.5px">Lore Index</strong><ul style="${inlineStyle(tocStyle)}">` +
    slugs
      .map(
        (item) =>
          `<li><a href="#${item.slug}" style="text-decoration:none;color:#d946ef">${String(item.index).padStart(2, '0')} · ${escapeHtml(item.title)}</a></li>`
      )
      .join('') +
    '</ul></nav>'
  const body = slugs
    .map((item) => {
      const tags =
        item.tags && item.tags.length
          ? ` <span style=\"margin-left:.5rem\">• ${item.tags.map(escapeHtml).join(', ')}<\/span>`
          : ''
      return `<details id="${item.slug}" style="${inlineStyle(detailsStyle)}"><summary style="${inlineStyle(summaryStyle)}"><span>🗂️ ${String(item.index).padStart(2, '0')}</span><span>${escapeHtml(item.title)}</span></summary><div style="${inlineStyle(metaStyle)}"><code>${escapeHtml(item.filename)}</code>${tags}</div><div class="lore-fragment">${item.html}</div></details>`
    })
    .join('')
  const footer =
    '<footer style="margin-top:1rem;font-size:0.6rem;text-align:right;opacity:.75">⚔️ Static lore conjured at build export • Safe word: <code>fiction</code></footer>'
  return `<h2>📜 Appended Lore Archive: Voidlight Chronicles</h2>${toc}${body}${footer}`
}

function escapeHtml(s: string): string {
  return s.replace(
    /[&<>"']/g,
    (c) =>
      ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
      })[c] as string
  )
}
function inlineStyle(obj: Record<string, any>): string {
  return Object.entries(obj)
    .map(([k, v]) => `${k.replace(/[A-Z]/g, (m) => '-' + m.toLowerCase())}:${String(v)}`)
    .join(';')
}

// Precompute static HTML once at module init (server). In client bundle this will be the already serialized string.
const STATIC_HTML = buildStaticHTML()

export function LoreArchive() {
  return (
    <section style={containerStyle} id="voidlight-lore-archive" suppressHydrationWarning>
      <div dangerouslySetInnerHTML={{ __html: STATIC_HTML }} />
    </section>
  )
}

export default LoreArchive

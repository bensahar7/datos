# Datos Health — Design System

Extracted from datos-health.com homepage and brand assets (May 2026).

---

## Colors

### Primary Palette (from logo SVG)
| Token | Hex | Usage |
|-------|-----|-------|
| `purple-primary` | `#6D60F3` | Logo center overlap, primary brand accent |
| `purple-light` | `#A07AFC` | Logo left mark, CTA hover states |
| `blue-lavender` | `#B6BDFF` | Logo right mark, secondary accent |

### UI Colors (from website)
| Token | Hex | Usage |
|-------|-----|-------|
| `cta-purple` | `#6D2D90` | Primary CTA buttons ("Request Demo"), deep purple |
| `text-dark` | `#333333` | Body text, headings (confirmed from SVG fills) |
| `text-heading` | `#2D1A4E` | Hero headline — very dark purple-black |
| `bg-white` | `#FFFFFF` | Page background |
| `bg-light` | `#F7F5FF` | Light purple tint sections |
| `border-light` | `#E5E0F0` | Card borders, dividers |

### Status / Accent
| Token | Hex | Usage |
|-------|-----|-------|
| `success-green` | `#34A853` | Positive indicators |
| `gold` | `#D4A843` | Nav top highlight bar (from screenshot) |

---

## Typography

| Element | Font | Weight | Size (approx) |
|---------|------|--------|----------------|
| Nav links | Sans-serif (likely Inter or Proxima Nova) | 500 | 15px |
| Hero headline | Sans-serif, same family | 700 (bold) | 42–48px |
| Hero subheadline | Sans-serif | 400 | 18–20px |
| Body text | Sans-serif | 400 | 16px |
| CTA button text | Sans-serif | 600 | 16px |

- Line heights are generous (~1.5 for body, ~1.2 for headings)
- Letter-spacing on headings is tight/normal, not wide

---

## Buttons

### Primary CTA
```css
.btn-primary {
  background: #6D2D90;
  color: #FFFFFF;
  padding: 14px 32px;
  border-radius: 30px;       /* fully rounded pill shape */
  font-weight: 600;
  font-size: 16px;
  border: none;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #5A2278;
}
```

### Secondary / Ghost
- White background, purple border, purple text
- Same pill shape and padding

---

## Layout & Spacing

| Property | Value |
|----------|-------|
| Max content width | ~1200px |
| Section padding (vertical) | 64–80px |
| Grid gutter | 24–32px |
| Card border-radius | 12–16px |
| Nav height | ~72px |

---

## Navigation

- **Style**: Clean horizontal nav bar, white background
- **Logo**: Left-aligned, "H" icon + "Datos Health" wordmark
- **Links**: Center-aligned, some with dropdown carets (ReadyCare, OpenCare, Resources)
- **CTA**: Right-aligned purple pill button ("Request Demo")
- **Sticky**: Nav appears fixed on scroll

---

## Hero Section Pattern

- **Layout**: Split — text left (~50%), image right (~50%)
- **Image**: Full-bleed photograph of clinician at laptop, slight gradient overlay at left edge
- **Headline**: Bold, dark, 3-line stacked statement ("Reduce Costs. / Improve Outcomes. / Increase Care Access.")
- **Subheadline**: Single line, lighter weight, beneath headline
- **CTA**: Purple pill button below subheadline
- **No decorative shapes** — photography-forward, clean and clinical

---

## Visual Identity Notes

- **Tone**: Professional, clinical, trustworthy — not playful
- **Photography**: Real people (clinicians), warm lighting, blurred backgrounds
- **Iconography**: Minimal, line-style where used
- **Whitespace**: Generous — the design breathes
- **Overall feel**: Enterprise healthcare SaaS — closer to Teladoc/Amwell than consumer health apps
- **No gradients** on UI surfaces; gradients only in the logo mark itself

---

## Logo Usage

The SVG logo mark is a stylized "H" composed of three overlapping shapes:
- Left arm: `#A07AFC` (purple)
- Right arm: `#B6BDFF` (lavender-blue)
- Center overlap: `#6D60F3` (deep purple)
- Wordmark: `#333333` (dark gray)

Minimum clear space: approximately the width of the "D" in "Datos" on all sides.

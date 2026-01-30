# Diff Summary — dark-mode-theme

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `css/styles.css` | Modified | +90 lines: dark mode media query, .dark-mode class, .theme-toggle button |
| `index.html` | Modified | Added theme toggle button in nav + JS |
| `about.html` | Modified | Added theme toggle button in nav + JS |
| `projects.html` | Modified | Added theme toggle button in nav + JS |
| `images/` | Unchanged | — |

## Visual Impact
- **MASSIVE**: Every visible surface changes color
- Background: white → near-black (#0d1117)
- Text: dark gray → light gray (#c9d1d9)
- Cards: light gray → dark (#161b22)
- Headings: navy → white (#f0f6fc)
- Accent: red → brighter pink (#ff6b81)
- Hero gradient: dark navy → darker navy
- All placeholders: light gray → dark gray

## Code vs. Visual Size Mismatch
- **Code diff**: ~90 lines of CSS (mostly re-declaring custom properties with new hex values)
- **Visual diff**: EVERY PIXEL on EVERY PAGE changes color
- **Ratio**: Most extreme mismatch of any branch. A reviewer reading the CSS diff would see `--color-bg: #0d1117` and have zero ability to judge whether it looks good.

## Visual Evidence
See `samples/branch3-dark-mode/`:
- `light-mode.jpg` — Index page in light mode (with toggle button)
- `dark-mode-index.jpg` — Index page in dark mode
- `dark-mode-about.jpg` — About page in dark mode

## This is the central finding of experiment 03
CSS-only changes with huge visual impact are **the worst case for text-based diffing.** The prompt needs a way to require/include visual before/after comparisons for style changes.

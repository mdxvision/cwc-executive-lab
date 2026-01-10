# CLAUDE.md - CWC Executive Leadership Lab

This file provides context for Claude Code sessions working on this project.

## Project Overview

CWC Executive Leadership Lab is a 10-month leadership development curriculum for Women of Color (WOC). It consists of interactive HTML slide decks and fillable worksheets delivered through GitHub Pages.

**Live Site:** https://mdxvision.github.io/cwc-executive-lab/

## Design System

### Typography
- **Headings:** Source Serif 4 (Google Fonts)
- **Body:** Inter (Google Fonts)

### Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Primary (Charcoal) | #1A1A1A | Text, backgrounds |
| Teal | #2A7B8C | Accents, buttons |
| Warm Gold | #D4A574 | Highlights, calls-to-action |
| Cream | #FAF8F5 | Backgrounds |

### Aesthetic
- Executive, minimal, professional
- Apple/enterprise design influence
- Clean whitespace, subtle shadows
- Mobile-responsive

## Content Structure

### Slide Decks
Interactive HTML presentations with:
- Click-to-advance navigation (arrow buttons)
- Keyboard navigation (← →)
- Touch/swipe support for mobile
- Progress bar indicator
- 15-25 slides per module

### Worksheets
Fillable HTML forms with:
- Auto-save to localStorage
- Print-friendly layouts
- Auto-calculations where applicable
- Clear/reset functionality

## Module Inventory

### Module 1: Break Through Career Plateaus (January)
**Slide Deck:** `index.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `career-growth-roadmap.html` | 7-section strategic planning worksheet |
| `plateau-diagnostic.html` | Self-assessment checklist (6 categories) |
| `stuck-loop.html` | Identify patterns and design new choices |
| `momentum-planner.html` | 14-day action tracking with reflection |
| `relationship-map.html` | Network mapping and relationship building |

### Module 2: Master Your Executive Presence (February)
**Slide Deck:** `module-2-presence.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `presence-audit.html` | Self-assessment of current presence |
| `presence-strategy.html` | Strategic presence development plan |
| `presence-practice-tracker.html` | Track presence practice sessions |

### Module 3: Build Your Strategic Brand (March)
**Slide Deck:** `module-3-brand.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `brand-discovery.html` | Values and strengths discovery |
| `brand-statement.html` | Personal brand statement builder |
| `visibility-planner.html` | Strategic visibility action plan |

### Module 4: Navigate Bias and Lead Through It (April)
**Slide Deck:** `module-4-bias.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `bias-log.html` | Document and analyze bias incidents |
| `energy-protection.html` | Energy management and boundary setting |

### Module 5: Amplify Your Voice (May)
**Slide Deck:** `module-5-voice.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `voice-assessment.html` | Voice impact self-assessment |
| `voice-practice.html` | Voice practice planner with meeting templates |

### Module 6: Build Your Board of Advisors (June)
**Slide Deck:** `module-6-advisors.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `board-audit.html` | Current advisory network audit |
| `outreach-planner.html` | Relationship outreach planning |

### Module 7: Lead and Develop Teams (July)
**Slide Deck:** `module-7-teams.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `team-development-planner.html` | Team assessment and development planning |

### Module 8: Lead Difficult Conversations (August)
**Slide Deck:** `module-8-conversations.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `conversation-prep.html` | PREP framework conversation planner |

### Module 9: Get Promoted (September)
**Slide Deck:** `module-9-promoted.html`
**Worksheets:**
| File | Purpose |
|------|---------|
| `promotion-planner.html` | Promotion readiness with STAR accomplishments |

### Module 10: Set the Table for Your Future (October)
**Slide Deck:** `module-10-future.html` (Capstone)
**Worksheets:**
| File | Purpose |
|------|---------|
| `future-vision.html` | Future vision and career planning |

## File Structure

```
cwc-executive-lab/
├── index.html                    # Module 1 slide deck (landing page)
├── module-2-presence.html        # Module 2 slide deck
├── module-3-brand.html           # Module 3 slide deck
├── module-4-bias.html            # Module 4 slide deck
├── module-5-voice.html           # Module 5 slide deck
├── module-6-advisors.html        # Module 6 slide deck
├── module-7-teams.html           # Module 7 slide deck
├── module-8-conversations.html   # Module 8 slide deck
├── module-9-promoted.html        # Module 9 slide deck
├── module-10-future.html         # Module 10 slide deck (Capstone)
├── career-growth-roadmap.html    # M1 worksheet
├── plateau-diagnostic.html       # M1 worksheet
├── stuck-loop.html               # M1 worksheet
├── momentum-planner.html         # M1 worksheet
├── relationship-map.html         # M1 worksheet
├── presence-audit.html           # M2 worksheet
├── presence-strategy.html        # M2 worksheet
├── presence-practice-tracker.html # M2 worksheet
├── brand-discovery.html          # M3 worksheet
├── brand-statement.html          # M3 worksheet
├── visibility-planner.html       # M3 worksheet
├── bias-log.html                 # M4 worksheet
├── energy-protection.html        # M4 worksheet
├── voice-assessment.html         # M5 worksheet
├── voice-practice.html           # M5 worksheet
├── board-audit.html              # M6 worksheet
├── outreach-planner.html         # M6 worksheet
├── team-development-planner.html # M7 worksheet
├── conversation-prep.html        # M8 worksheet
├── promotion-planner.html        # M9 worksheet
├── future-vision.html            # M10 worksheet
├── README.md                     # Project documentation
├── CLAUDE.md                     # This file
├── DESIGN-RESEARCH.md            # Design research notes
├── images/                       # Image assets
├── skool-assets/                 # Skool platform assets
│   └── SKOOL-LESSON-STRUCTURE.md
├── export-slides.js              # Export utility
└── export-worksheets.js          # Export utility
```

## Local Development

```bash
# Clone
git clone https://github.com/mdxvision/cwc-executive-lab.git
cd cwc-executive-lab

# Open any HTML file directly in browser
open index.html
open module-2-presence.html

# Or use a local server
python -m http.server 8000
# Then visit http://localhost:8000
```

## Adding New Content

### New Slide Deck
1. Copy existing module file as template
2. Update slide content in `<section class="slide">` elements
3. Update title and metadata
4. Add to README.md and CLAUDE.md

### New Worksheet
1. Copy existing worksheet as template
2. Update form fields and sections
3. Update localStorage keys for auto-save
4. Add to README.md and CLAUDE.md

## Deployment

Hosted on GitHub Pages. Changes pushed to `main` branch auto-deploy.

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

## Part Of

CWC Platform - Unified business automation for [Coaching Women of Color](https://coachingwomenofcolor.com/)

---

*Last Updated: January 2026*

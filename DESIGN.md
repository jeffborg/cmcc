---
name: Cessnock Motor Cycle Club
description: Visual system capturing the club's public website (colors, type, components)
colors:
  bg: "#111827"
  panel: "#ffffff"
  text: "#1f2937"
  brand: "#b91c1c"
  brand-dark: "#7f1d1d"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "clamp(2.2rem, 6vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.08
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  md: "18px"
components:
  button-primary:
    backgroundColor: "{colors.brand}"
    textColor: "{colors.panel}"
    rounded: "{rounded.md}"
    padding: "0.75rem 1rem"
---

# Design System: Cessnock Motor Cycle Club

## 1. Overview

Creative North Star: "The Community Noticeboard" — a friendly, legible public presence that prioritises clear information over flashy presentation. The site preserves legacy assets and should feel welcoming and approachable to members and families while remaining easy for committee editors to update.

Key Characteristics:
- Content-first: event and membership information are prominent and scannable.
- Photographic: authentic club photos carry tone and trust.
- Low-friction: simple components and clear affordances for non-technical editors.

## 2. Colors

The palette is restrained: a single warm red brand accent balanced against neutral surfaces and readable text.

### Primary
- **Club Red** (#b91c1c): primary accent used for primary buttons, call-to-action links, and subtle emphasis.

### Neutrals
- **Background** (#111827): used for the dark hero and header surfaces.
- **Panel** (#ffffff): primary card and page surface.
- **Text** (#1f2937): default body text color for high legibility.

Named Rule: The brand accent is used sparingly — reserve it for primary actions and key emphasis.

## 3. Typography

Display Font: system UI stack (used for hero H1 via a clamp scale)
Body Font: same system UI stack for consistent legibility in content and nav

Character: straightforward, utilitarian, and highly readable; hierarchy is driven by size and weight rather than decorative typefaces.

Hierarchy:
- Display (H1): 700, clamp(2.2rem, 6vw, 4rem) — hero and major headings.
- Body: 400, 1rem, line-height 1.6 — paragraphs and long-form content. Aim for 65–75ch measure in prose containers.

## 4. Elevation

The system uses subtle shadows for lifted panels and cards (ambient shadow) and otherwise relies on tonal contrast between `--panel` and page backgrounds.

Shadow vocabulary:
- **Panel**: `0 20px 45px rgba(15, 23, 42, 0.08)` — use sparingly for featured cards and media tiles.

Named Rule: Flat by default; use shadow only to indicate surfaced/featured content.

## 5. Components

Buttons — character: confident, clear primary actions.
- Shape: rounded corners 18px.
- Primary: background `{colors.brand}`, text `{colors.panel}`, padding 0.75rem 1rem.
- Secondary: dark background for secondary affordance (see `.button-secondary` styling in CSS).

Cards / Containers — character: soft, content-first.
- Corner Style: 18px radius.
- Background: `{colors.panel}` with 1px subtle border and optional panel shadow for featured tiles.
- Internal Padding: 1.5rem typical; reduce on small screens.

Navigation — character: compact, transparent header with elevated sticky surface in dark mode. Nav links use pill-like hit targets and clear active states.

Hero — character: photographic and media-forward. Large clamp-scaled H1 with supporting intro copy.

## 6. Do's and Don'ts

Do:
- Do prioritise clear, scannable event and membership information over decorative layouts.
- Do use real club photos and preserve legacy media to convey trust and history.
- Do ensure WCAG AA contrast and clear focus states for keyboard users.

Don't:
- Don't use gradient text or background-clip:text treatments.
- Don't use large colored side-stripe borders as the primary affordance.
- Don't adopt glassmorphism, neon-on-black, or SaaS hero-metric templates that conflict with the club's approachable tone.


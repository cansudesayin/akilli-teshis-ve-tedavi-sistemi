---
name: MediAI Clinical Interface
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#414755'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc1'
  primary: '#0058bc'
  on-primary: '#ffffff'
  primary-container: '#0070eb'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#535f74'
  on-secondary: '#ffffff'
  secondary-container: '#d4e0f9'
  on-secondary-container: '#586378'
  tertiary: '#9e3d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#c64f00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#d7e3fc'
  secondary-fixed-dim: '#bbc7df'
  on-secondary-fixed: '#101c2e'
  on-secondary-fixed-variant: '#3c475b'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb595'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  button:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 24px
  margin: 40px
---

## Brand & Style

The design system is engineered for high-stakes clinical environments where cognitive load must be minimized. It adopts a **Minimalist Corporate** style with a "sterile" medical-grade aesthetic. The personality is authoritative, precise, and reassuring, prioritizing functional clarity over decorative flair. 

The visual language utilizes generous white space to reduce "data noise," ensuring that doctors can process patient information and AI insights without distraction. The atmosphere is professional and high-trust, achieved through a structured grid and a disciplined color application.

## Colors

The palette is anchored by **Hospital Blue**, a color associated with medical precision and digital reliability, used exclusively for primary actions and critical focus states. **Dark Navy** provides a heavy visual anchor for structural elements like sidebars and navigation, creating a clear mental model of "the application container" versus "the clinical content."

Greys are segmented into "Clinical Greys"—cool-toned neutrals used for borders, secondary text, and disabled states to maintain a clean, wash-out-free appearance under varying hospital lighting conditions.

- **Primary:** #007AFF (Actions/Links)
- **High-Contrast:** #0A1628 (Sidebars/Headlines)
- **Background:** #FFFFFF (Workspaces/Forms)
- **Secondary Text:** #64748B (Subtitles/Captions)
- **Dividers:** #E2E8F0 (Subtle separations)

## Typography

This design system utilizes **Inter** for its exceptional legibility in small sizes and technical contexts. The typographic hierarchy is strictly enforced to guide the practitioner's eye through complex diagnostic data.

Headlines use the Dark Navy color to establish authority. Body text utilizes a slightly softened black (#1E293B) to improve long-form reading comfort. Labels and "overlines" use an uppercase style with increased tracking to differentiate metadata from actionable clinical data.

## Layout & Spacing

The design system employs a **Fixed Grid** philosophy for desktop interfaces to ensure data density remains predictable across different monitors. A 12-column system is used for main dashboard layouts, while a centered 8-column column layout is preferred for focused form entry.

Rhythm is based on a 4px baseline grid. Large 40px outer margins provide a "frame" that keeps the interface feeling airy and organized, preventing the clinical information from feeling cramped or overwhelming.

## Elevation & Depth

To maintain a "sterile" and flat look while still indicating hierarchy, this design system uses **Ambient Shadows** and **Tonal Layers**. 

1. **Base:** The primary workspace is flat white (#FFFFFF).
2. **Cards:** Use a very soft, highly diffused shadow (0px 4px 20px rgba(10, 22, 40, 0.05)) to lift patient records or diagnostic modules from the background.
3. **Sidebar:** Uses the Dark Navy background with no shadow, relying on color contrast for separation.
4. **Modals:** Use a heavier shadow and a 40% opacity navy backdrop to isolate the task.

## Shapes

The design system uses **Soft (0.25rem)** roundedness. This subtle rounding removes the "aggression" of sharp corners—making the software feel modern and accessible—without appearing overly "bubbly" or consumer-grade. Buttons and input fields share this 4px radius, while larger containers like Cards use **rounded-lg (8px)** to emphasize their role as distinct modules.

## Components

- **Buttons:** Primary buttons are Hospital Blue with white text, using a "bold" 600 weight. Secondary buttons use a subtle grey border (#E2E8F0) and Dark Navy text.
- **Card-Based Selectors:** Used for medical specializations. These feature an icon, a bold title, and a 1px border that thickens and changes to Hospital Blue upon selection.
- **Input Fields:** Pure white background with a 1px #E2E8F0 border. Labels are always positioned above the input in Dark Navy, using the `label-caps` style for clarity.
- **Chips:** Used for patient tags or symptoms. These use a light blue tint (#EFF6FF) with blue text (#007AFF) and no border, ensuring they are visible but subordinate to primary actions.
- **Data Tables:** Row-based with subtle 1px horizontal dividers. No vertical lines. Hover states use a very pale blue (#F0F7FF) to assist row tracking.
- **AI Insights:** Modules containing AI-generated text use a very subtle gradient border or a left-hand accent bar in Hospital Blue to indicate the "machine-generated" nature of the content.
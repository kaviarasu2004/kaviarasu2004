"""
Generates dark.svg and light.svg for the GitHub profile README banner.
Portrait is a PLACEHOLDER until a real photo is provided and run through the
dithering/segmentation pipeline described in the master prompt -- swap the
<!-- PORTRAIT PLACEHOLDER --> block for the real dot-portrait <g> once that's built.
"""

PALETTE = {
    "portrait_dark": "#A78BFA",
    "portrait_light": "#7C3AED",
    "chrome": "#22D3EE",
    "chrome_dim": "#0891B2",
    "accent": "#10B981",
    "bg_dark": "#0A101F",
    "bg_light": "#F8FAFC",
    "text_light_mode": "#1E293B",
}

INFO = {
    "Subject": "Kaviarasu",
    "Role": "Full-Stack Developer",
    "Origin": "Tamil Nadu, India",
    "Education": "B.Tech in IT",
    "Status": "Building + Learning + Shipping",
    "ToolChain": "VS Code, Git, MySQL Workbench",
}

CORE = {
    "Core.Lang": "Java, Python",
    "Core.Frontend": "React.js",
    "Core.Backend": "Spring Boot, Flask",
    "Core.Database": "MySQL",
    "Core.Infra": "Git, GitHub",
}

GRID = {
    "Grid.Mail": "your-email@gmail.com",  # EDIT ME
    "Grid.Portfolio": "coming soon",
    "Grid.LinkedIn": "kaviarasu001",
    "Grid.GitHub": "kaviarasu2004",
}

HANDLE_PILL = "kaviarasu2004"
TERMINAL_TITLE = "your-email@gmail.com - % ./profile.sh --live"  # EDIT ME

WIDTH, HEIGHT = 1180, 610
PANEL_X = 470
PANEL_RIGHT = 1120
LABEL_W = 190
VALUE_W = 340
ROW_H = 23
FONT = "SFMono-Regular, Menlo, Consolas, monospace"


def row(label, value, y, c):
    dots_start = PANEL_X + LABEL_W + 8
    dots_end = (PANEL_RIGHT - VALUE_W) - 8
    dots_len = max(dots_end - dots_start, 10)
    return f'''
  <text x="{PANEL_X}" y="{y}" font-family="{FONT}" font-size="14"
        textLength="{LABEL_W}" lengthAdjust="spacingAndGlyphs"
        fill="{c['chrome']}">{label}</text>
  <text x="{dots_start}" y="{y}" font-family="{FONT}" font-size="14"
        textLength="{dots_len}" lengthAdjust="spacingAndGlyphs"
        fill="{c['dot_leader']}" opacity="0.5">{'.' * 60}</text>
  <text x="{PANEL_RIGHT}" y="{y}" font-family="{FONT}" font-size="14"
        text-anchor="end" textLength="{VALUE_W}" lengthAdjust="spacingAndGlyphs"
        fill="{c['value']}">{value}</text>'''


def build_svg(mode: str) -> str:
    is_dark = mode == "dark"
    c = {
        "bg": PALETTE["bg_dark"] if is_dark else PALETTE["bg_light"],
        "chrome": PALETTE["chrome"],
        "accent": PALETTE["accent"],
        "portrait": PALETTE["portrait_dark"] if is_dark else PALETTE["portrait_light"],
        "value": "#E5E7EB" if is_dark else PALETTE["text_light_mode"],
        "dot_leader": "#94A3B8" if is_dark else "#64748B",
    }

    y = 190
    rows = []
    for label, value in INFO.items():
        rows.append(row(label, value, y, c))
        y += ROW_H
    y += 10  # section gap
    rows.append(f'<line x1="{PANEL_X}" y1="{y-14}" x2="{PANEL_RIGHT}" y2="{y-14}" stroke="{c["chrome"]}" opacity="0.25"/>')
    for label, value in CORE.items():
        rows.append(row(label, value, y, c))
        y += ROW_H
    y += 10
    rows.append(f'<line x1="{PANEL_X}" y1="{y-14}" x2="{PANEL_RIGHT}" y2="{y-14}" stroke="{c["chrome"]}" opacity="0.25"/>')
    for label, value in GRID.items():
        rows.append(row(label, value, y, c))
        y += ROW_H

    rows_svg = "\n".join(rows)

    svg = f'''<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}"
     xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.3; }}
      }}
      .live-dot {{ animation: pulse 1.6s ease-in-out infinite; }}
    </style>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" rx="14" fill="{c['bg']}"/>
  <rect x="1.5" y="1.5" width="{WIDTH-3}" height="{HEIGHT-3}" rx="13"
        fill="none" stroke="{c['chrome']}" stroke-opacity="0.35"/>

  <!-- terminal chrome -->
  <circle cx="30" cy="32" r="6" fill="#EF4444"/>
  <circle cx="52" cy="32" r="6" fill="#F59E0B"/>
  <circle cx="74" cy="32" r="6" fill="#10B981"/>
  <text x="{WIDTH/2}" y="37" text-anchor="middle" font-family="{FONT}"
        font-size="13" fill="{c['dot_leader']}">{TERMINAL_TITLE}</text>
  <line x1="0" y1="56" x2="{WIDTH}" y2="56" stroke="{c['chrome']}" stroke-opacity="0.2"/>

  <!-- VISUAL.MAP portrait frame -->
  <text x="56" y="92" font-family="{FONT}" font-size="12" letter-spacing="2"
        fill="{c['dot_leader']}">VISUAL.MAP</text>
  <rect x="56" y="106" width="360" height="440" rx="8" fill="none"
        stroke="{c['chrome']}" stroke-opacity="0.5" stroke-width="1.5"/>

  <!-- PORTRAIT PLACEHOLDER: replace this g element with the generated dot-portrait -->
  <g opacity="0.6">
    <text x="236" y="310" text-anchor="middle" font-family="{FONT}" font-size="13"
          fill="{c['portrait']}">[ PHOTO NOT YET PROVIDED ]</text>
    <text x="236" y="332" text-anchor="middle" font-family="{FONT}" font-size="11"
          fill="{c['dot_leader']}">dot-portrait renders here</text>
  </g>
  <!-- END PORTRAIT PLACEHOLDER -->

  <!-- SYSTEM.INFO header -->
  <text x="{PANEL_X}" y="92" font-family="{FONT}" font-size="13" letter-spacing="2"
        fill="{c['chrome']}">SYSTEM.INFO</text>
  <line x1="{PANEL_X}" y1="100" x2="{PANEL_RIGHT}" y2="100" stroke="{c['chrome']}" stroke-opacity="0.3"/>
  <circle class="live-dot" cx="{PANEL_RIGHT-46}" cy="87" r="4" fill="#EF4444"/>
  <text x="{PANEL_RIGHT-38}" y="91" font-family="{FONT}" font-size="12"
        fill="#EF4444">LIVE</text>

  <!-- handle pill -->
  <rect x="{PANEL_X}" y="110" width="230" height="26" rx="4" fill="{c['accent']}" opacity="0.15"/>
  <rect x="{PANEL_X}" y="110" width="230" height="26" rx="4" fill="none" stroke="{c['accent']}"/>
  <text x="{PANEL_X+12}" y="127" font-family="{FONT}" font-size="14" fill="{c['accent']}">{HANDLE_PILL}</text>

  {rows_svg}
</svg>'''
    return svg


if __name__ == "__main__":
    with open("dark.svg", "w") as f:
        f.write(build_svg("dark"))
    with open("light.svg", "w") as f:
        f.write(build_svg("light"))
    print("wrote dark.svg and light.svg")
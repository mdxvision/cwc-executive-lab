#!/usr/bin/env python3
"""
Generate Fillable PDF Worksheets for Executive Leadership Lab Module 1
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfform
from reportlab.lib.utils import simpleSplit

# Colors
CHARCOAL = HexColor('#1A1A1A')
TEAL = HexColor('#2A7B8C')
WARM_GOLD = HexColor('#D4A574')
CREAM = HexColor('#FAF8F5')
TEXT_LIGHT = HexColor('#666666')
BORDER = HexColor('#E5E0D8')

WIDTH, HEIGHT = letter

def draw_header(c, title, subtitle):
    """Draw worksheet header"""
    # Header line
    c.setStrokeColor(CHARCOAL)
    c.setLineWidth(2)
    c.line(0.75*inch, HEIGHT - 1.1*inch, WIDTH - 0.75*inch, HEIGHT - 1.1*inch)

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(CHARCOAL)
    c.drawString(0.75*inch, HEIGHT - 0.9*inch, title)

    # Subtitle
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(0.75*inch, HEIGHT - 1.3*inch, subtitle)

def draw_section_header(c, y, number, title):
    """Draw a section header with number"""
    # Number circle
    c.setFillColor(WARM_GOLD)
    c.circle(1*inch, y + 0.15*inch, 0.18*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(1*inch, y + 0.08*inch, str(number))

    # Title
    c.setFillColor(CHARCOAL)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1.4*inch, y + 0.05*inch, title)

    return y - 0.4*inch

def draw_text_field(c, x, y, width, height, name, placeholder=""):
    """Draw a fillable text field"""
    c.setStrokeColor(BORDER)
    c.setFillColor(HexColor('#FFFFFF'))
    c.rect(x, y, width, height, fill=1, stroke=1)

    # Add form field
    c.acroForm.textfield(
        name=name,
        x=x + 4, y=y + 2,
        width=width - 8, height=height - 4,
        borderWidth=0,
        fontSize=10,
        fillColor=HexColor('#FFFFFF'),
        textColor=CHARCOAL,
        forceBorder=False
    )

def draw_textarea(c, x, y, width, height, name, label=None):
    """Draw a larger text area with optional label"""
    if label:
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(CHARCOAL)
        c.drawString(x, y + height + 0.1*inch, label)

    c.setStrokeColor(BORDER)
    c.setFillColor(HexColor('#FFFFFF'))
    c.rect(x, y, width, height, fill=1, stroke=1)

    c.acroForm.textfield(
        name=name,
        x=x + 4, y=y + 2,
        width=width - 8, height=height - 4,
        borderWidth=0,
        fontSize=10,
        fillColor=HexColor('#FFFFFF'),
        textColor=CHARCOAL,
        forceBorder=False,
        fieldFlags='multiline'
    )

def draw_label(c, x, y, text, bold=False):
    """Draw a label"""
    if bold:
        c.setFont("Helvetica-Bold", 10)
    else:
        c.setFont("Helvetica", 10)
    c.setFillColor(CHARCOAL)
    c.drawString(x, y, text)

def draw_hint(c, x, y, text):
    """Draw hint text"""
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(x, y, text)

def draw_footer(c, text):
    """Draw footer"""
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_LIGHT)
    c.drawCentredString(WIDTH/2, 0.5*inch, text)


# ============================================
# WORKSHEET 1: Career Growth Roadmap
# ============================================
def create_career_growth_roadmap():
    filename = "/Users/wendyperdomo/Downloads/GitHub/cwc-executive-lab/worksheets-pdf/Career-Growth-Roadmap.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    # Page 1
    draw_header(c, "Career Growth Roadmap", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    # Intro
    c.setFillColor(HexColor('#F5F2ED'))
    c.rect(0.75*inch, y - 0.6*inch, WIDTH - 1.5*inch, 0.7*inch, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.line(0.75*inch, y - 0.6*inch, 0.75*inch, y + 0.1*inch)
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(0.95*inch, y - 0.15*inch, "Purpose: A strategic planning document to move from where you are to where you want to be.")
    c.drawString(0.95*inch, y - 0.4*inch, "This becomes your personal north star for the year ahead.")

    y -= 1.1*inch

    # Section 1: North Star
    y = draw_section_header(c, y, 1, "Your North Star")
    draw_label(c, 0.75*inch, y, "What is your 'next best role'? (Be specific about title, scope, or type of work)")
    y -= 0.15*inch
    draw_textarea(c, 0.75*inch, y - 0.7*inch, WIDTH - 1.5*inch, 0.7*inch, "north_star_role")
    y -= 0.95*inch

    draw_label(c, 0.75*inch, y, "What does success look like in 12 months?")
    y -= 0.15*inch
    draw_textarea(c, 0.75*inch, y - 0.7*inch, WIDTH - 1.5*inch, 0.7*inch, "north_star_success")
    y -= 1.1*inch

    # Section 2: Current Reality
    y = draw_section_header(c, y, 2, "Current Reality")
    draw_label(c, 0.75*inch, y, "Where are you right now? (Role, level, key responsibilities)")
    y -= 0.15*inch
    draw_textarea(c, 0.75*inch, y - 0.6*inch, WIDTH - 1.5*inch, 0.6*inch, "current_role")
    y -= 0.85*inch

    draw_label(c, 0.75*inch, y, "What's blocking your progress?")
    y -= 0.15*inch
    draw_textarea(c, 0.75*inch, y - 0.6*inch, WIDTH - 1.5*inch, 0.6*inch, "current_blocks")
    y -= 1*inch

    # Section 3: Strengths & Gaps
    y = draw_section_header(c, y, 3, "Strengths & Gaps")

    # Two columns
    col_width = (WIDTH - 1.7*inch) / 2

    draw_label(c, 0.75*inch, y, "Top 3 Strengths to Leverage:")
    draw_label(c, 0.75*inch + col_width + 0.2*inch, y, "Top 2 Gaps to Close:")
    y -= 0.2*inch

    for i in range(3):
        draw_text_field(c, 0.75*inch, y - 0.35*inch, col_width, 0.3*inch, f"strength_{i+1}")
        if i < 2:
            draw_text_field(c, 0.75*inch + col_width + 0.2*inch, y - 0.35*inch, col_width, 0.3*inch, f"gap_{i+1}")
        y -= 0.4*inch

    draw_footer(c, "Career Growth Roadmap | Executive Leadership Lab | Coaching Women of Color | Page 1 of 2")

    # Page 2
    c.showPage()
    draw_header(c, "Career Growth Roadmap", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    # Section 4: Constraints + Realities
    y = draw_section_header(c, y, 4, "Constraints + Realities")

    col_width = (WIDTH - 1.7*inch) / 2
    draw_label(c, 0.75*inch, y, "What constraints are you working with?")
    draw_label(c, 0.75*inch + col_width + 0.2*inch, y, "What support do you need?")
    y -= 0.15*inch
    draw_hint(c, 0.75*inch, y, "Time, energy, caregiving, politics, budget")
    draw_hint(c, 0.75*inch + col_width + 0.2*inch, y, "Resources, people, flexibility")
    y -= 0.2*inch
    draw_textarea(c, 0.75*inch, y - 0.7*inch, col_width, 0.7*inch, "constraints")
    draw_textarea(c, 0.75*inch + col_width + 0.2*inch, y - 0.7*inch, col_width, 0.7*inch, "support_needed")
    y -= 1.1*inch

    # Section 5: 90-Day Goals
    y = draw_section_header(c, y, 5, "90-Day Goals")

    goals = [
        ("Goal 1: What will you accomplish in 30 days?", "goal_30"),
        ("Goal 2: What will you accomplish in 60 days?", "goal_60"),
        ("Goal 3: What will you accomplish in 90 days?", "goal_90")
    ]

    for i, (label, name) in enumerate(goals):
        draw_label(c, 0.75*inch, y, label)
        y -= 0.15*inch
        draw_text_field(c, 0.75*inch, y - 0.3*inch, WIDTH - 1.5*inch, 0.3*inch, name)
        y -= 0.35*inch
        draw_hint(c, 0.75*inch, y, "How will you measure success?")
        y -= 0.15*inch
        draw_text_field(c, 0.75*inch, y - 0.3*inch, WIDTH - 1.5*inch, 0.3*inch, f"{name}_measure")
        y -= 0.5*inch

    # Section 6: First Moves
    y = draw_section_header(c, y, 6, "First Moves (Next 14 Days)")
    draw_label(c, 0.75*inch, y, "3 actions that create immediate momentum:")
    y -= 0.2*inch

    for i in range(3):
        c.setFillColor(WARM_GOLD)
        c.circle(0.9*inch, y - 0.1*inch, 0.12*inch, fill=1, stroke=0)
        c.setFillColor(HexColor('#FFFFFF'))
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(0.9*inch, y - 0.14*inch, str(i+1))
        draw_text_field(c, 1.15*inch, y - 0.25*inch, WIDTH - 1.9*inch, 0.3*inch, f"first_move_{i+1}")
        y -= 0.4*inch

    # Section 7: Accountability
    y -= 0.2*inch
    y = draw_section_header(c, y, 7, "Accountability")
    draw_label(c, 0.75*inch, y, "Who will hold you accountable?")
    draw_text_field(c, 3.5*inch, y - 0.05*inch, 3*inch, 0.3*inch, "accountability_who")
    y -= 0.4*inch
    draw_label(c, 0.75*inch, y, "How often will you check in?")
    draw_text_field(c, 3.5*inch, y - 0.05*inch, 3*inch, 0.3*inch, "accountability_frequency")

    draw_footer(c, "Career Growth Roadmap | Executive Leadership Lab | Coaching Women of Color | Page 2 of 2")

    c.save()
    print(f"Created: {filename}")


# ============================================
# WORKSHEET 2: Plateau Diagnostic
# ============================================
def create_plateau_diagnostic():
    filename = "/Users/wendyperdomo/Downloads/GitHub/cwc-executive-lab/worksheets-pdf/Plateau-Diagnostic.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    draw_header(c, "Plateau Diagnostic", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    # Intro
    c.setFillColor(HexColor('#F5F2ED'))
    c.rect(0.75*inch, y - 0.5*inch, WIDTH - 1.5*inch, 0.6*inch, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.line(0.75*inch, y - 0.5*inch, 0.75*inch, y + 0.1*inch)
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(0.95*inch, y - 0.15*inch, "Purpose: Identify your primary plateau type. Check all statements that feel true right now.")
    c.drawString(0.95*inch, y - 0.35*inch, "Be honest—this is for your eyes only.")

    y -= 0.9*inch

    plateaus = [
        ("Skill Plateau", [
            "I'm known as 'the expert' but keep getting passed over for leadership",
            "My strengths feel outdated or too narrow for where I want to go",
            "I lack exposure to strategic or cross-functional work",
            "My comfort zone has become my ceiling",
            "I need new skills or credentials to reach the next level"
        ]),
        ("Role Plateau", [
            "My manager has nowhere to go either",
            "The organization is flat or constantly restructuring",
            "Budget constraints are limiting new positions",
            "I've outgrown my scope but can't expand within this role",
            "There's no clear path to promotion in my current position"
        ]),
        ("Identity Plateau", [
            "I experience imposter syndrome despite my track record",
            "Perfectionism often delays my action",
            "I fear visibility or being seen as self-promoting",
            "I find myself shrinking to fit instead of standing out",
            "I avoid risks or difficult conversations that could advance my career"
        ])
    ]

    for plateau_name, items in plateaus:
        # Section header
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(CHARCOAL)
        c.drawString(0.75*inch, y, plateau_name)
        c.setStrokeColor(CHARCOAL)
        c.setLineWidth(1)
        c.line(0.75*inch, y - 0.08*inch, 2.5*inch, y - 0.08*inch)
        y -= 0.35*inch

        for item in items:
            # Checkbox
            c.acroForm.checkbox(
                name=f"check_{plateau_name}_{items.index(item)}",
                x=0.75*inch,
                y=y - 0.05*inch,
                size=12,
                borderColor=BORDER,
                fillColor=HexColor('#FFFFFF'),
                textColor=CHARCOAL,
                forceBorder=True
            )
            # Label
            c.setFont("Helvetica", 9)
            c.setFillColor(TEXT_LIGHT)
            # Wrap text if needed
            lines = simpleSplit(item, "Helvetica", 9, WIDTH - 2*inch)
            for line in lines:
                c.drawString(1.1*inch, y, line)
                y -= 0.18*inch
            y -= 0.05*inch

        y -= 0.25*inch

    # Results section
    y -= 0.1*inch
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(CHARCOAL)
    c.drawString(0.75*inch, y, "Your Primary Plateau:")
    y -= 0.25*inch
    draw_text_field(c, 0.75*inch, y - 0.35*inch, WIDTH - 1.5*inch, 0.35*inch, "primary_plateau")
    y -= 0.6*inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75*inch, y, "Key Insight:")
    y -= 0.25*inch
    draw_textarea(c, 0.75*inch, y - 0.6*inch, WIDTH - 1.5*inch, 0.6*inch, "key_insight")

    draw_footer(c, "Plateau Diagnostic | Executive Leadership Lab | Coaching Women of Color")

    c.save()
    print(f"Created: {filename}")


# ============================================
# WORKSHEET 3: Stuck Loop
# ============================================
def create_stuck_loop():
    filename = "/Users/wendyperdomo/Downloads/GitHub/cwc-executive-lab/worksheets-pdf/Stuck-Loop.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    draw_header(c, "Stuck Loop Worksheet", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    # Intro
    c.setFillColor(HexColor('#F5F2ED'))
    c.rect(0.75*inch, y - 0.5*inch, WIDTH - 1.5*inch, 0.6*inch, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.line(0.75*inch, y - 0.5*inch, 0.75*inch, y + 0.1*inch)
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(0.95*inch, y - 0.15*inch, "Purpose: Identify the pattern that keeps you stuck, then design a new choice to break the cycle.")
    c.drawString(0.95*inch, y - 0.35*inch, "Most plateaus follow a predictable loop until we consciously interrupt it.")

    y -= 1*inch

    # Part 1: Your Stuck Loop
    y = draw_section_header(c, y, 1, "Map Your Stuck Loop")

    loop_items = [
        ("Trigger", "What situation or event starts the pattern?", "trigger"),
        ("Thought", "What do you tell yourself when this happens?", "thought"),
        ("Emotion", "What feeling arises from that thought?", "emotion"),
        ("Behavior", "What do you do (or avoid) as a result?", "behavior"),
        ("Outcome", "What happens? How does this reinforce the pattern?", "outcome")
    ]

    for label, hint, name in loop_items:
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(CHARCOAL)
        c.drawString(0.75*inch, y, label + ":")
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColor(TEXT_LIGHT)
        c.drawString(2*inch, y, hint)
        y -= 0.2*inch
        draw_text_field(c, 0.75*inch, y - 0.4*inch, WIDTH - 1.5*inch, 0.4*inch, name)
        y -= 0.6*inch

    # Arrow loop visual
    c.setFont("Helvetica", 10)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(WIDTH/2, y, "↻ This loop repeats until interrupted ↻")
    y -= 0.5*inch

    # Part 2: Design Your New Choice
    y = draw_section_header(c, y, 2, "Design Your New Choice")

    draw_label(c, 0.75*inch, y, "Where in the loop can you make a different choice?")
    y -= 0.2*inch
    draw_textarea(c, 0.75*inch, y - 0.5*inch, WIDTH - 1.5*inch, 0.5*inch, "new_choice_where")
    y -= 0.7*inch

    draw_label(c, 0.75*inch, y, "What new thought or behavior will you try instead?")
    y -= 0.2*inch
    draw_textarea(c, 0.75*inch, y - 0.5*inch, WIDTH - 1.5*inch, 0.5*inch, "new_choice_what")
    y -= 0.85*inch

    # Part 3: Support
    y = draw_section_header(c, y, 3, "Name Your Support")

    draw_label(c, 0.75*inch, y, "What reminder, tool, or accountability will help you make this different choice?")
    y -= 0.2*inch
    draw_textarea(c, 0.75*inch, y - 0.6*inch, WIDTH - 1.5*inch, 0.6*inch, "support")

    draw_footer(c, "Stuck Loop Worksheet | Executive Leadership Lab | Coaching Women of Color")

    c.save()
    print(f"Created: {filename}")


# ============================================
# WORKSHEET 4: 14-Day Momentum Planner
# ============================================
def create_momentum_planner():
    filename = "/Users/wendyperdomo/Downloads/GitHub/cwc-executive-lab/worksheets-pdf/14-Day-Momentum-Planner.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    draw_header(c, "14-Day Momentum Planner", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    # Intro
    c.setFillColor(HexColor('#F5F2ED'))
    c.rect(0.75*inch, y - 0.4*inch, WIDTH - 1.5*inch, 0.5*inch, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.line(0.75*inch, y - 0.4*inch, 0.75*inch, y + 0.1*inch)
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(0.95*inch, y - 0.2*inch, "Purpose: Schedule your first moves and track progress over 14 days. Momentum starts with action.")

    y -= 0.7*inch

    # Date range
    draw_label(c, 0.75*inch, y, "Start Date:")
    draw_text_field(c, 1.7*inch, y - 0.05*inch, 1.5*inch, 0.3*inch, "start_date")
    draw_label(c, 3.5*inch, y, "End Date:")
    draw_text_field(c, 4.4*inch, y - 0.05*inch, 1.5*inch, 0.3*inch, "end_date")

    y -= 0.5*inch

    # Table header
    c.setFillColor(CHARCOAL)
    c.rect(0.75*inch, y - 0.35*inch, WIDTH - 1.5*inch, 0.35*inch, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(HexColor('#FFFFFF'))

    col_widths = [0.8, 2.2, 1.2, 1.5, 1.3]  # Date, Action, Who, Evidence, Status
    col_x = 0.75*inch
    headers = ["Date", "Action / Task", "Who", "Evidence / Win", "Status"]

    for i, (header, width) in enumerate(zip(headers, col_widths)):
        c.drawString(col_x + 0.05*inch, y - 0.25*inch, header)
        col_x += width * inch

    y -= 0.4*inch

    # Table rows (14 rows)
    for row in range(14):
        col_x = 0.75*inch
        row_y = y - 0.35*inch

        # Row background alternating
        if row % 2 == 1:
            c.setFillColor(HexColor('#FAFAFA'))
            c.rect(0.75*inch, row_y, WIDTH - 1.5*inch, 0.35*inch, fill=1, stroke=0)

        # Border
        c.setStrokeColor(BORDER)
        c.rect(0.75*inch, row_y, WIDTH - 1.5*inch, 0.35*inch, fill=0, stroke=1)

        # Fields
        for i, width in enumerate(col_widths):
            field_width = width * inch - 0.1*inch
            c.acroForm.textfield(
                name=f"row{row+1}_col{i+1}",
                x=col_x + 0.05*inch,
                y=row_y + 0.05*inch,
                width=field_width,
                height=0.25*inch,
                borderWidth=0,
                fontSize=8,
                fillColor=HexColor('#FFFFFF') if row % 2 == 0 else HexColor('#FAFAFA'),
                textColor=CHARCOAL,
                forceBorder=False
            )
            col_x += width * inch

        y -= 0.35*inch

    draw_footer(c, "14-Day Momentum Planner | Executive Leadership Lab | Coaching Women of Color | Page 1 of 2")

    # Page 2: Reflection
    c.showPage()
    draw_header(c, "14-Day Momentum Planner", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    y = draw_section_header(c, y, "", "14-Day Reflection")
    y += 0.2*inch

    reflections = [
        ("Key Wins This Period:", "What did you accomplish? What moved forward?", "wins"),
        ("What Got in the Way:", "What obstacles did you encounter?", "obstacles"),
        ("What I Learned:", "What insight or lesson emerged?", "learned"),
        ("Next 14-Day Focus:", "What will you prioritize in the next two weeks?", "next_focus")
    ]

    for label, hint, name in reflections:
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(CHARCOAL)
        c.drawString(0.75*inch, y, label)
        y -= 0.2*inch
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColor(TEXT_LIGHT)
        c.drawString(0.75*inch, y, hint)
        y -= 0.25*inch
        draw_textarea(c, 0.75*inch, y - 1*inch, WIDTH - 1.5*inch, 1*inch, name)
        y -= 1.3*inch

    draw_footer(c, "14-Day Momentum Planner | Executive Leadership Lab | Coaching Women of Color | Page 2 of 2")

    c.save()
    print(f"Created: {filename}")


# ============================================
# WORKSHEET 5: Relationship Baseline Map
# ============================================
def create_relationship_map():
    filename = "/Users/wendyperdomo/Downloads/GitHub/cwc-executive-lab/worksheets-pdf/Relationship-Baseline-Map.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    draw_header(c, "Relationship Baseline Map", "Executive Leadership Lab | Module 1 | January")

    y = HEIGHT - 1.8*inch

    # Intro
    c.setFillColor(HexColor('#F5F2ED'))
    c.rect(0.75*inch, y - 0.5*inch, WIDTH - 1.5*inch, 0.6*inch, fill=1, stroke=0)
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.line(0.75*inch, y - 0.5*inch, 0.75*inch, y + 0.1*inch)
    c.setFont("Helvetica", 10)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(0.95*inch, y - 0.15*inch, "Purpose: Take stock of who currently influences your growth. This baseline will help you")
    c.drawString(0.95*inch, y - 0.35*inch, "identify gaps and opportunities in your network.")

    y -= 0.9*inch

    # Relationship cards (2 columns)
    relationships = [
        ("Manager / Direct Leader", "Who directly influences your development?", ["Name:", "Role:"], ["mgr_name", "mgr_role"]),
        ("Key Stakeholders", "2-3 people whose opinion shapes your reputation", ["Name 1:", "Name 2:", "Name 3:"], ["stakeholder_1", "stakeholder_2", "stakeholder_3"]),
        ("Potential Sponsors", "Who has power and might advocate for you?", ["Name 1:", "Name 2:"], ["sponsor_1", "sponsor_2"]),
        ("Mentors", "Who provides guidance or career advice?", ["Name 1:", "Name 2:"], ["mentor_1", "mentor_2"]),
        ("Peer Allies", "Trusted peers you collaborate with", ["Name 1:", "Name 2:"], ["peer_1", "peer_2"]),
        ("External Community", "Networks or groups outside your org", ["Group 1:", "Group 2:"], ["community_1", "community_2"])
    ]

    col_width = (WIDTH - 1.7*inch) / 2

    for i, (title, hint, labels, names) in enumerate(relationships):
        col = i % 2
        row = i // 2

        x = 0.75*inch + col * (col_width + 0.2*inch)
        card_y = y - row * 1.6*inch

        # Card box
        c.setStrokeColor(BORDER)
        c.setFillColor(HexColor('#FFFFFF'))
        c.rect(x, card_y - 1.4*inch, col_width, 1.4*inch, fill=1, stroke=1)

        # Card header
        c.setFillColor(CHARCOAL)
        c.rect(x, card_y - 0.3*inch, col_width, 0.3*inch, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(HexColor('#FFFFFF'))
        c.drawString(x + 0.1*inch, card_y - 0.22*inch, title)

        # Hint
        c.setFont("Helvetica-Oblique", 8)
        c.setFillColor(TEXT_LIGHT)
        c.drawString(x + 0.1*inch, card_y - 0.5*inch, hint)

        # Fields
        field_y = card_y - 0.7*inch
        for label, name in zip(labels, names):
            c.setFont("Helvetica", 9)
            c.setFillColor(CHARCOAL)
            c.drawString(x + 0.1*inch, field_y, label)
            c.acroForm.textfield(
                name=name,
                x=x + 0.6*inch,
                y=field_y - 0.05*inch,
                width=col_width - 0.8*inch,
                height=0.22*inch,
                borderWidth=1,
                borderColor=BORDER,
                fontSize=9,
                fillColor=HexColor('#FFFFFF'),
                textColor=CHARCOAL
            )
            field_y -= 0.28*inch

    y -= 4.9*inch

    # 3 Relationships to Deepen
    c.setStrokeColor(CHARCOAL)
    c.setLineWidth(2)
    c.rect(0.75*inch, y - 1.8*inch, WIDTH - 1.5*inch, 2*inch, fill=0, stroke=1)
    c.setStrokeColor(WARM_GOLD)
    c.setLineWidth(4)
    c.line(0.75*inch, y - 1.8*inch, 0.75*inch, y + 0.2*inch)

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(CHARCOAL)
    c.drawString(0.95*inch, y, "3 Relationships to Deepen This Year")

    y -= 0.35*inch
    third_width = (WIDTH - 2*inch) / 3

    for i in range(3):
        x = 0.95*inch + i * (third_width + 0.15*inch)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(CHARCOAL)
        c.drawString(x, y, f"Person {i+1}:")
        c.acroForm.textfield(
            name=f"deepen_person_{i+1}",
            x=x,
            y=y - 0.4*inch,
            width=third_width - 0.1*inch,
            height=0.25*inch,
            borderWidth=1,
            borderColor=BORDER,
            fontSize=9,
            fillColor=HexColor('#FFFFFF'),
            textColor=CHARCOAL
        )
        c.setFont("Helvetica", 8)
        c.setFillColor(TEXT_LIGHT)
        c.drawString(x, y - 0.6*inch, "What I want to be known for:")
        c.acroForm.textfield(
            name=f"deepen_goal_{i+1}",
            x=x,
            y=y - 1.25*inch,
            width=third_width - 0.1*inch,
            height=0.5*inch,
            borderWidth=1,
            borderColor=BORDER,
            fontSize=8,
            fillColor=HexColor('#FFFFFF'),
            textColor=CHARCOAL,
            fieldFlags='multiline'
        )

    draw_footer(c, "Relationship Baseline Map | Executive Leadership Lab | Coaching Women of Color")

    c.save()
    print(f"Created: {filename}")


# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    import os

    # Create output directory
    output_dir = "/Users/wendyperdomo/Downloads/GitHub/cwc-executive-lab/worksheets-pdf"
    os.makedirs(output_dir, exist_ok=True)

    print("Creating fillable PDF worksheets...")
    print("-" * 40)

    create_career_growth_roadmap()
    create_plateau_diagnostic()
    create_stuck_loop()
    create_momentum_planner()
    create_relationship_map()

    print("-" * 40)
    print("All worksheets created successfully!")
    print(f"Location: {output_dir}")

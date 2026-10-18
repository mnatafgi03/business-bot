from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

GREEN = colors.HexColor("#1F6F50")
ss = getSampleStyleSheet()
title = ParagraphStyle("T", parent=ss["Title"], textColor=GREEN, fontSize=26, spaceAfter=4)
tag = ParagraphStyle("Tag", parent=ss["Normal"], alignment=1, textColor=colors.grey, fontSize=11, spaceAfter=18)
h1 = ParagraphStyle("H1", parent=ss["Heading1"], textColor=GREEN, fontSize=16, spaceBefore=14, spaceAfter=6)
body = ParagraphStyle("B", parent=ss["Normal"], fontSize=10.5, leading=15, spaceAfter=6)
cell = ParagraphStyle("C", parent=body, fontSize=9.5, leading=13, spaceAfter=0)
cellb = ParagraphStyle("CB", parent=cell, fontName="Helvetica-Bold", textColor=colors.white)

def P(t, s=body): return Paragraph(t, s)
def table(rows, widths):
    data = [[P(c, cellb if i == 0 else cell) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EEF5F1")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B8CCC2")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t

s = []
s += [P("Cedar Flow Automation", title), P("Automation that ships in weeks, not quarters", tag)]

s += [P("1. Company Overview", h1),
 P("Cedar Flow Automation is a consultancy based in Beirut, Lebanon, founded in 2024. We help small and "
   "mid-sized businesses in the Levant and the Gulf replace spreadsheets, manual follow-ups and disconnected "
   "tools with practical automation, ERP systems and AI agents that their teams actually adopt. "
   "We work remotely and on-site, in Arabic, English and French."),
 P("2. Mission", h1),
 P("To make small businesses run like well-oiled machines. We believe automation should come with a fixed "
   "price, deliver visible results quickly, and be simple enough that the people doing the daily work are "
   "happy to use it.")]

s += [P("3. Services and Pricing", h1),
 table([
   ["Service", "What you get", "Price and timeline"],
   ["Workflow Audit", "One-week review of how your business really runs: process mapping, interviews, and a "
                      "prioritized automation roadmap.", "$1,500 fixed. 1 week."],
   ["ERP Implementation (Odoo)", "Setup of sales, inventory, purchasing and invoicing; data migration; staff onboarding.",
                      "Starter package from $6,000. Typically 4 to 6 weeks."],
   ["AI Agent Development", "Custom agents for customer support, invoice and purchase-order checking, and order intake.",
                      "Pilot from $4,000. Typically 3 to 4 weeks."],
   ["Training & Support", "Hands-on team training and an ongoing support retainer (up to 8 hours of work per month).",
                      "Retainer $400 per month."],
 ], [4.0*cm, 8.2*cm, 4.6*cm]),
 Spacer(1, 6),
 P("All prices are in US dollars. Prices marked \"from\" depend on scope, which is confirmed in writing before "
   "work begins.")]

s += [PageBreak(), P("4. Team", h1),
 table([
   ["Name", "Role", "Background"],
   ["Layla Haddad", "Co-founder and CEO", "Former operations consultant with 10 years of experience helping "
                    "distribution and retail companies streamline operations."],
   ["Omar Nasr", "Co-founder and CTO", "Software and machine-learning engineer; leads AI agent development and integrations."],
   ["Rima Khoury", "Head of Delivery", "Odoo specialist; runs ERP implementations and team training."],
 ], [3.4*cm, 4.0*cm, 9.4*cm])]

s += [P("5. Unique Value Proposition", h1),
 P("<b>Fixed prices.</b> No surprise invoices: scope and price are agreed before work starts."),
 P("<b>Results within 30 days.</b> You see working results within 30 days of project kickoff."),
 P("<b>Audit credit.</b> The Workflow Audit fee is credited toward any implementation project booked within "
   "60 days of the audit."),
 P("<b>Built for adoption.</b> We train your team and design around how they already work.")]

s += [P("6. How We Work", h1),
 P("<b>Step 1 - Discover.</b> A free 30-minute intro call to understand your goals."),
 P("<b>Step 2 - Audit.</b> The one-week Workflow Audit produces a roadmap ranked by impact and effort."),
 P("<b>Step 3 - Build.</b> We implement the highest-value items, in an ERP, an AI agent, or both."),
 P("<b>Step 4 - Train and support.</b> We onboard your team and offer an optional monthly support retainer.")]

s += [P("7. Who We Serve", h1),
 P("Retail, distribution, clinics, light manufacturing and professional-services firms with roughly 5 to 100 "
   "employees.")]

s += [P("8. Contact", h1),
 P("Email: hello@cedarflow.example<br/>Office hours: Monday to Friday, 9:00 to 17:00 Beirut time<br/>"
   "We typically reply within one business day.")]

SimpleDocTemplate("me/about_business.pdf", pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                  topMargin=2*cm, bottomMargin=2*cm, title="About Cedar Flow Automation",
                  author="Cedar Flow Automation").build(s)

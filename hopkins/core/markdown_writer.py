def write_markdown(data, filename="executive_summary.md"):
    lines = []
    lines.append("# Executive Summary\n")

    # ✅ Company Overview
    co = data["company_overview"]
    lines.append("## Business Overview\n")
    lines.append(f"**Name:** {co['name']}\n")
    lines.append(f"**Sector:** {co['sector']}\n")
    lines.append(f"**Headquarters:** {co['headquarters']}\n")
    lines.append(f"{co['business_model']}\n")

    # ✅ Key Financials
    kf = data["key_financials"]
    lines.append("## Key Financials\n")
    lines.append(f"- **Revenue (Actual):** {kf['revenue_actual']}")
    lines.append(f"- **Revenue (Forecast):** {kf['revenue_forecast']}")
    lines.append(f"- **EBITDA (Actual):** {kf['ebitda_actual']}")
    lines.append(f"- **EBITDA (Forecast):** {kf['ebitda_forecast']}")
    lines.append(f"- **Recent CAGR:** {kf['recent_cagr']}\n")

    # ✅ Investment Highlights
    lines.append("## Investment Highlights\n")
    for item in data["investment_highlights"]:
        lines.append(f"- {item}")

    # ✅ Risks
    lines.append("\n## Risks\n")
    for item in data["risks"]:
        lines.append(f"- {item}")

    # ✅ Write to file
    with open(filename, "w") as f:
        f.write("\n".join(lines))

    print(f"✅ Markdown saved: {filename}")

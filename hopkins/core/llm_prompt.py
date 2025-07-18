PROMPT = '''\
Given any CIM text, extract:
1. The company’s **name**, **sector**, **headquarters**, and **business_model**.
2. The company’s latest **full-year actual Net Revenue** (in USD millions). *Include the exact currency and units as shown — for example, if the CIM says "$429.7 million", your value must be "$429.7 million".*
3. The current or next **full-year forecast Net Revenue** if available, same rule: *keep units and currency as written*.
4. The latest **full-year actual EBITDA** (in USD millions). *Keep units.*
5. The current or next **full-year forecast EBITDA** if available.
6. The CAGR of Revenue and EBITDA for the last 3–5 years if available.
7. 3–5 investment highlights as bullet points.
8. 2–3 key risks as bullet points.

**When multiple figures exist**, follow this order of preference:
1️⃣ Take *pro forma* if it represents the whole company, not a single property.  
2️⃣ If not available, take *actual reported* figures.  
3️⃣ If only a range is given, pick the midpoint and show it with units.  
4️⃣ If only a table is available, use summary-level totals, not line items.

**Important:** Use exactly the same units and currency notation as the CIM text.

Return ONLY valid JSON matching this shape:

{{
  "company_overview": {{
    "name": "...",
    "sector": "...",
    "headquarters": "...",
    "business_model": "..."
  }},
  "key_financials": {{
    "revenue_actual": "...",
    "revenue_forecast": "...",
    "ebitda_actual": "...",
    "ebitda_forecast": "...",
    "recent_cagr": "..."
  }},
  "investment_highlights": [
    "...",
    "..."
  ],
  "risks": [
    "...",
    "..."
  ]
}}

CIM:
"""
{cim_text}
"""
'''

JSON_SCHEMA = {
    "name": "investment_summary",
    "schema": {
        "type": "object",
        "properties": {
            "company_overview": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "sector": {"type": "string"},
                    "headquarters": {"type": "string"},
                    "business_model": {"type": "string"}
                },
                "required": ["name", "sector", "headquarters", "business_model"]
            },
            "key_financials": {
                "type": "object",
                "properties": {
                    "revenue_actual": {"type": "string"},
                    "revenue_forecast": {"type": "string"},
                    "ebitda_actual": {"type": "string"},
                    "ebitda_forecast": {"type": "string"},
                    "recent_cagr": {"type": "string"}
                },
                "required": [
                    "revenue_actual",
                    "revenue_forecast",
                    "ebitda_actual",
                    "ebitda_forecast",
                    "recent_cagr"
                ]
            },
            "investment_highlights": {
                "type": "array",
                "items": {"type": "string"}
            },
            "risks": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": [
            "company_overview",
            "key_financials",
            "investment_highlights",
            "risks"
        ]
    }
} 
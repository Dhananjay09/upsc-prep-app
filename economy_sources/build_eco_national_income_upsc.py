import json

upsc = []

# ==================================================================
# NEW UPSC TIER: NATIONAL INCOME ACCOUNTING (Ramesh Singh Ch.1 remainder)
# Avoiding overlap with existing GDP/GNP/NDP/NNP mechanics already covered
# ==================================================================

upsc.append({"q":"Which economist, a Nobel Prize-winning American economist, is credited with first conceiving the idea of GDP, in 1934?","o":["Simon Kuznets","Angus Maddison","Amartya Sen","Paul Samuelson"],"a":0,"e":"Simon Kuznets, a Nobel Prize-winning US economist, first conceived the idea of GDP in 1934 — a concept later refined into the modern system of national accounts used worldwide."})

upsc.append({"q":"Consider the following statements about India's 'Income from Abroad' component (used to derive GNP from GDP):\n1. It includes private remittances, interest on external loans, and external grants.\n2. India has historically been a net gainer on the private remittances front.\n3. India's overall 'Income from Abroad' balance has typically been negative, making India's GNP lower than its GDP.\nWhich of the statements given above is/are correct?","o":["1, 2 and 3","1 and 2 only","2 and 3 only","1 and 3 only"],"a":0,"e":"All three statements are correct — private remittances, interest on external loans and external grants together form 'Income from Abroad'; India gains on remittances but loses more on interest payments/trade deficits, making the net figure negative and India's GNP lower than its GDP."})

upsc.append({"q":"As per World Bank data cited for 2015, India's position among the world's private remittance-receiving countries was:","o":["The highest recipient of private remittances in the world, ahead of China","Second highest, behind China","Third highest, behind China and Mexico","Not among the top ten recipient countries"],"a":0,"e":"India was the world's highest recipient of private remittances in 2015 (around $72 billion, per World Bank projections), with China a distant second (around $64 billion)."})

upsc.append({"q":"Which one of the following changes was NOT part of the CSO's January 2015 revision of the base year and methodology for India's National Accounts?","o":["Adoption of a fixed, permanent base year that would never require revision again","Measuring headline GDP growth at constant market prices instead of factor cost","Comprehensive coverage of the corporate sector using MCA21 (Ministry of Corporate Affairs) e-governance data","Comprehensive coverage of the financial sector using data from regulators such as SEBI, PFRDA and IRDA"],"a":0,"e":"This is incorrect — the base year is meant to be revised periodically (the National Statistical Commission recommended revising it every five years), not fixed permanently. The other three changes (constant market price GDP, MCA21-based corporate coverage, and SEBI/PFRDA/IRDA-based financial sector coverage) were genuine features of the January 2015 revision."})

upsc.append({"q":"Which one of the following correctly distinguishes 'production taxes/subsidies' from 'product taxes/subsidies' in India's revised (2015) national accounting methodology?","o":["Production taxes/subsidies (e.g., land revenue, stamp duty, input subsidies to farmers) are paid/received independent of output volume, whereas product taxes/subsidies (e.g., excise, sales tax, import/export duties) are paid/received per unit of the product","Production taxes are levied per unit of output while product taxes are independent of output volume","Both production and product taxes are levied strictly per unit of output with no distinction between them","Product subsidies apply only to exported goods, while production subsidies apply only to imported goods"],"a":0,"e":"The 2015 methodology explicitly distinguishes production taxes/subsidies (independent of production volume — e.g., land revenue, stamp/registration fees, input subsidies) from product taxes/subsidies (levied per unit of the product — e.g., excise, sales tax, customs duties) — not the reverse or an import/export-based distinction."})

upsc.append({"q":"Which one of the following is the correct relationship between Gross Value Added (GVA) at basic prices, GVA at factor cost, and GDP, as per India's revised national accounting framework?","o":["GDP = GVA at basic prices + product taxes − product subsidies; and GVA at factor cost = GVA at basic prices − production taxes + production subsidies","GDP = GVA at factor cost + production taxes − production subsidies, with no role for basic prices in the framework","GVA at basic prices = GDP + product taxes, with factor cost playing no part in the calculation","GVA at factor cost is always numerically higher than GVA at basic prices"],"a":0,"e":"The correct identities are: GDP = GVA at basic prices + product taxes − product subsidies, and GVA at factor cost = GVA at basic prices − production taxes (less production subsidies) — meaning GVA at factor cost is typically LOWER than (not higher than) GVA at basic prices, contrary to the last option."})

upsc.append({"q":"Which one of the following statements about India's GDP and GVA growth estimates for 2017-18 (as per Economic Survey 2017-18) is correct?","o":["GDP at constant market prices grew at 6.5 per cent (down from 7.1 per cent in 2016-17), while GVA at constant basic prices grew at 6.1 per cent (down from 6.6 per cent)","GDP growth accelerated from 6.5 per cent in 2016-17 to 7.1 per cent in 2017-18","GVA growth exceeded GDP growth in both 2016-17 and 2017-18","Per Capita Income at current prices declined in 2017-18 compared to 2016-17"],"a":0,"e":"As per the cited Economic Survey 2017-18 estimates, both GDP (6.5%, down from 7.1%) and GVA (6.1%, down from 6.6%) growth rates decelerated in 2017-18, and Per Capita Income at current prices actually rose (from Rs. 1,03,219 to Rs. 1,11,782), not declined."})

# ==================================================================
# ASSEMBLY & VALIDATION
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, q["q"]
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == 4, ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_national_income_upsc.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

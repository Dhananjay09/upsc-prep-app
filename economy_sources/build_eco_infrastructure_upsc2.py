import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_infrastructure (Ramesh Singh Ch.9, Indian Infrastructure)
# Definition of infrastructure, Eleventh/Twelfth Plan investment targets,
# public-private complementarity, UDAY scheme mechanics
# ==================================================================

upsc.append({"q":"As per the framework discussed in the context of Indian infrastructure, which three sectors are considered infrastructure 'universally around the world'?","o":["Power, transportation and communication","Power, housing and sewerage","Transportation, water supply and urban amenities","Communication, housing and water supply"],"a":0,"e":"Power, transportation and communication are identified as the three sectors universally recognised as infrastructure worldwide, even though a broader country-specific list may also include water supply, sewerage, housing and urban amenities."})

upsc.append({"q":"Consider the following statements about public and private investment in India's infrastructure sector:\n1. Public and private investment in infrastructure are considered complementary rather than alternative to each other, given the very high investment requirement.\n2. Public investment capacity depends on the ability to raise resources, which in turn depends on collecting adequate user charges from consumers.\n3. Complete reliance on private production without appropriate regulation is considered likely to produce optimal outcomes.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — the text explicitly states that complete reliance on private production WITHOUT appropriate regulation is NOT likely to produce optimal outcomes, just as exclusive government dependence also creates difficulties."})

upsc.append({"q":"Which one of the following was NOT among the three factors identified as extremely important for enabling greater public investment in Indian infrastructure through better resource-raising capacity?","o":["Nationalisation of all private infrastructure companies","Reform of the power sector","Introduction of road user charges (tolls or a cess on petrol/diesel)","Rationalisation of railway fares"],"a":0,"e":"The three identified factors were power sector reform, road user charges, and railway fare rationalisation — nationalisation of private infrastructure companies was never proposed as part of this framework, which instead emphasised complementary public-private investment."})

upsc.append({"q":"With reference to infrastructure investment targets set during India's Five Year Plans, consider the following statements:\n1. The Eleventh Plan proposed an infrastructure investment of about US$500 billion, targeting private-sector contribution to exceed 30 per cent of total investment for the first time.\n2. The Twelfth Plan approach paper projected an investment of over Rs. 45 lakh crore, with at least 50 per cent expected to come from the private sector.\n3. Actual private-sector contribution during the Eleventh Plan was anticipated at around 36 per cent.\nHow many of the statements given above are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements are correct: the Eleventh Plan targeted over 30% private contribution (with ~36% actually anticipated) out of a US$500 billion infrastructure investment, while the Twelfth Plan approach paper raised the bar further to over Rs. 45 lakh crore with at least 50% expected from private sources."})

upsc.append({"q":"The UDAY (Ujwal DISCOM Assurance Yojana) scheme, launched by the Government of India in November 2015, was primarily aimed at addressing financial and operational distress in which one of the following?","o":["State electricity Distribution Companies (DISCOMs)","Public sector steel manufacturing units","Regional Rural Banks","Urban Co-operative Banks"],"a":0,"e":"UDAY specifically targeted the financial and operational turnaround of state-level electricity Distribution Companies (DISCOMs), whose outstanding debt (Rs. 4.3 lakh crore by 2014-15) and high AT&C losses (~22%) threatened both power-sector reform and banking-sector stability."})

upsc.append({"q":"Consider the following statements about the salient features of the UDAY scheme:\n1. Participating states were to take over 75 per cent of DISCOM debt, in a 50:25 split across 2015-16 and 2016-17.\n2. The debt taken over by states under UDAY would be included in the calculation of states' fiscal deficit for those years.\n3. States could issue non-SLR instruments, including State Development Loan (SDL) bonds, to fund the takeover.\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 is false — the Government of India explicitly excluded the state-assumed DISCOM debt from the calculation of state fiscal deficits for 2015-16 and 2016-17, an accounting relaxation designed to ease the transition."})

upsc.append({"q":"UDAY sought to reduce DISCOMs' Aggregate Transmission & Technical (AT&C) losses from around 22 per cent to what target level, while also eliminating the gap between ARR (Average Revenue Realised) and ACS (Average Cost of Supply) by 2018-19?","o":["15 per cent","10 per cent","18 per cent","5 per cent"],"a":0,"e":"UDAY targeted bringing AT&C losses down from ~22% to 15% through measures like compulsory smart metering, transformer/meter upgrades, and energy-efficient appliances (LED bulbs, efficient pumps/fans/ACs), alongside closing the ARR-ACS gap by 2018-19."})

upsc.append({"q":"Which one of the following measures was cited under UDAY as a means to reduce DISCOMs' cost of power?","o":["Increased supply of cheaper domestic coal, coal linkage rationalisation, and coal swaps from inefficient to efficient plants","Complete privatisation of all coal mining operations","Elimination of all coal-based power generation in favour of renewables","Direct government subsidy payments to DISCOM shareholders"],"a":0,"e":"UDAY's cost-reduction measures for power included cheaper domestic coal supply, coal linkage rationalisation, swapping coal from inefficient to efficient plants, GCV-based coal price rationalisation, and faster transmission line completion — with NTPC alone expected to pass on savings of Rs. 0.35/unit through such measures."})

upsc.append({"q":"Assertion (A): Under UDAY, states taking over DISCOM debt saw their effective interest cost on that debt fall significantly.\nReason (R): States could raise funds at lower rates (around 8-9 per cent) compared to the 14-15 per cent DISCOMs were paying, by issuing state bonds/borrowing directly.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both are true and R explains A: because states could borrow at 8-9% (versus the 14-15% DISCOMs were paying on their debt), the state takeover of 75% of DISCOM debt directly reduced the effective interest burden — one of UDAY's core financial-restructuring mechanisms."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_infrastructure_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

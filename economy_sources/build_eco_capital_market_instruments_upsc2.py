import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_capital_market_instruments (Ramesh Singh Ch.11)
# State Level Finance Institutions (SFCs/SIDCs), India's financial regulatory
# architecture, FSDC, FSLRC (Justice B.N. Srikrishna Commission) recommendations
# ==================================================================

upsc.append({"q":"Consider the following statements about State Level Finance Institutions (SLFIs) in India:\n1. State Finance Corporations (SFCs) were first set up in Punjab in 1955.\n2. State Industrial Development Corporations (SIDCs) were first set up in Andhra Pradesh and Bihar in 1960.\n3. Most SFCs and SIDCs are currently running profitably and have no restructuring needs.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — almost all SFCs and SIDCs are described as running in huge losses, potentially needing restructuring along AIFI lines, though there is a lack of will from both states and private financiers to take them over."})

upsc.append({"q":"Which one of the following statements about India's financial sector regulatory architecture is correct?","o":["It follows a predominantly 'product-wise' regulatory design, with RBI regulating credit/savings/remittances, SEBI regulating investment products, IRDA regulating insurance, and PFRDA regulating pension products","It follows a single unified regulator model where one agency oversees all financial products","Cooperative banks are regulated in the same manner and by the same body as scheduled commercial banks","The Forward Markets Commission (FMC) continues to function as an independent regulator, separate from SEBI"],"a":0,"e":"India's regulatory architecture is product-wise (RBI-credit/savings, SEBI-investment, IRDA-insurance, PFRDA-pension), though this creates complications for entities offering multiple product types (e.g., insurance companies), making some regulation effectively entity-based instead; cooperative banks are regulated differently (via Registrar of Cooperatives) from mainstream banks, and the FMC was merged into SEBI by September 2015, no longer functioning independently."})

upsc.append({"q":"Which one of the following bodies regulates housing finance companies as a 'quasi-regulatory agency' in India's financial system?","o":["National Housing Bank (NHB)","Reserve Bank of India (RBI) directly","Ministry of Urban Development","Insurance Regulatory and Development Authority (IRDA)"],"a":0,"e":"The National Housing Bank (NHB) functions as a quasi-regulatory agency specifically regulating housing finance companies, alongside NABARD (supervising RRBs and cooperative banks) and SIDBI (regulating State Finance Corporations)."})

upsc.append({"q":"The Financial Sector Development Council (FSDC), which replaced the High Level Committee on Capital Markets, is best described as:","o":["A council of regulators, convened by the Ministry of Finance with the Finance Minister as chairman, having no statutory authority but a permanent secretariat","A statutory body with independent enforcement powers superior to SEBI and RBI","An agency exclusively responsible for setting monetary policy","A judicial tribunal for resolving disputes between banks and their customers"],"a":0,"e":"The FSDC is structured as a non-statutory council of regulators chaired by the Finance Minister, with a permanent secretariat, tasked with resolving inter-agency disputes, overseeing financial conglomerates spanning multiple regulators, and handling multi-product wealth management issues — it lacks independent statutory enforcement authority."})

upsc.append({"q":"The Financial Sector Legislative Reforms Commission (FSLRC), which submitted its report in early 2013, was headed by which one of the following?","o":["Justice B.N. Srikrishna","Y.V. Reddy","Raghuram Rajan","Bimal Jalan"],"a":0,"e":"The FSLRC was headed by Justice B.N. Srikrishna and tasked with examining India's financial regulatory structure and laws, ultimately recommending a shift from an 'area-based' to a 'task-based' division of regulatory responsibility."})

upsc.append({"q":"Consider the following statements about the FSLRC's major recommendations:\n1. It recommended a 'horizontal structure' with a Unified Financial Agency (UFA) replacing multiple area-specific regulators like SEBI and IRDA, to eliminate regulatory overlap.\n2. It recommended setting up a Financial Redressal Agency (FRA) to handle consumer complaints across the entire financial sector, taking this function away from individual regulators.\n3. It recommended a Financial Sector Appellate Tribunal (FSAT) to hear appeals across the entire financial sector.\nHow many of the statements given above are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements are correct: the FSLRC's headline recommendations included a Unified Financial Agency for horizontal, task-based regulation (addressing overlaps like the SEBI-IRDA ULIP controversy), a cross-sector Financial Redressal Agency, and a Financial Sector Appellate Tribunal."})

upsc.append({"q":"The 'ULIP controversy' that motivated the FSLRC's call for a Unified Financial Agency arose from a regulatory overlap between which two regulators?","o":["SEBI and IRDA","RBI and SEBI","IRDA and PFRDA","RBI and NABARD"],"a":0,"e":"The ULIP (Unit Linked Insurance Plan) controversy stemmed from overlapping jurisdiction between SEBI (which viewed ULIPs as investment products) and IRDA (which viewed them as insurance products) — a textbook case of product-wise regulatory ambiguity that the FSLRC's proposed Unified Financial Agency aimed to resolve."})

upsc.append({"q":"Assertion (A): Certain key financial institutions like SBI, Public Sector Banks, LIC and GIC continue to enjoy special statutory status distinct from ordinary company law.\nReason (R): Similar special statutes that once governed IFCI, UTI and IDBI have since been repealed.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are factually true, though R is not strictly an explanation of A — rather, both illustrate a broader trend: while SBI, PSBs, LIC and GIC retain special statutory status, comparable earlier special statutes for IFCI, UTI and IDBI were repealed as those institutions were restructured/converted (e.g., via reverse mergers) during financial sector reforms."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_capital_market_instruments_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

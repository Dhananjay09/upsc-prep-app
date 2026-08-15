import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_banking (Ramesh Singh Ch.12, NBFC section)
# NBFC classification (NBFC-D/ND, AFC/IC/LC), RBI umbrella definition, exempted
# categories, new P2P/Account Aggregator categories, sector stats, DRR norms
# ==================================================================

upsc.append({"q":"Consider the following statements about the RBI's classification of Non-Banking Financial Companies (NBFCs):\n1. Based on liability structure, NBFCs are broadly classified into deposit-taking (NBFC-D) and non-deposit-taking (NBFC-ND) categories.\n2. A deposit-taking NBFC must be incorporated under the Companies Act and hold a minimum Net Owned Fund (NOF) of Rs. 2 crore to register with the RBI.\n3. NBFCs are permitted to accept demand deposits such as savings and current accounts.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — NBFCs are explicitly barred from accepting demand deposits (savings/current accounts); they may only accept/renew public deposits with tenures between 12 and 60 months."})

upsc.append({"q":"Which one of the following categories of NBFC-type entities is regulated by SEBI rather than the RBI, to avoid dual regulation?","o":["Venture capital funds, merchant banks and stock broking firms","Housing finance companies","Nidhi companies","Chit fund companies"],"a":0,"e":"Venture capital funds, merchant banks and stock broking firms are registered and regulated by SEBI; housing finance companies fall under the National Housing Bank, nidhi companies under the Ministry of Corporate Affairs, and chit fund companies under respective state governments (Chit Funds Act, 1982) — each exempted from RBI's NBFC regulatory ambit to avoid overlap."})

upsc.append({"q":"Match List-I (older NBFC business-type classification) with List-II (current reclassified category) and select the correct answer using the code below.\nList-I:\nA. Equipment leasing company\nB. Hire-purchase company\nC. Loan company\nD. Investment company\nList-II:\n1. Loan Company (LC)\n2. Investment Company (IC)\n3. Asset Finance Company (AFC)\n4. Asset Finance Company (AFC)\nCodes:","o":["A-3, B-4, C-1, D-2","A-1, B-2, C-3, D-4","A-3, B-1, C-4, D-2","A-2, B-3, C-1, D-4"],"a":0,"e":"Equipment leasing and Hire-purchase companies (A, B) — both financing physical assets — were merged into the Asset Finance Company (AFC) category; Loan companies (C) remained Loan Company (LC); Investment companies (D) remained Investment Company (IC), completing the three-way AFC/IC/LC reclassification."})

upsc.append({"q":"Which one of the following statements about the Asset Finance Company (AFC) category of NBFCs is correct?","o":["An AFC's principal business is financing physical assets that support productive and economic activities, and such NBFCs play a vital role in financing infrastructure projects","AFCs are exclusively engaged in trading government securities","AFCs are prohibited from financing any physical assets","AFCs are regulated exclusively by SEBI, not the RBI"],"a":0,"e":"AFCs specifically finance physical assets supporting productive/economic activities and were highlighted by the Government of India as playing a vital infrastructure-financing role in 2016-17 — they remain under RBI's NBFC regulatory ambit, not SEBI's."})

upsc.append({"q":"During 2017-18, the RBI introduced two new NBFC categories aimed at promoting financial inclusion through direct interaction between small lenders and borrowers, alongside addressing consumer protection. What are these two categories?","o":["Peer-to-Peer (P2P) lending platforms and Account Aggregators (AAs)","Asset Finance Companies and Investment Companies","Housing Finance Companies and Chit Fund Companies","Merchant Banks and Venture Capital Funds"],"a":0,"e":"The RBI introduced Peer-to-Peer (P2P) lending platform and Account Aggregator (AA) as two new NBFC categories in 2017-18, aimed at facilitating direct small-lender-to-small-borrower interaction and improved consumer data/protection management respectively."})

upsc.append({"q":"Consider the following statements about India's NBFC sector, based on data cited from around 2016-17:\n1. The NBFC sector accounted for about 17 per cent of bank assets and had a balance sheet size of around Rs. 20.7 lakh crore.\n2. By end-September, the sector's gross NPA ratio stood higher than its Capital to Risk Weighted Assets Ratio (CRAR).\n3. The sector depends significantly on public funds, including via non-convertible debentures (NCDs).\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 is false — the sector's CRAR (22.5%) was substantially HIGHER than its gross NPA ratio (5.5%), indicating reasonably healthy capital buffers relative to bad-loan levels, not the reverse."})

upsc.append({"q":"Following the Companies Act, 2013 (effective 1 April 2014), NBFCs raising capital through debentures are required to maintain which one of the following?","o":["A Debenture Redemption Reserve (DRR) account, under stricter norms than before","A Cash Reserve Ratio (CRR) account identical to that of scheduled commercial banks","A Statutory Liquidity Ratio (SLR) account with the RBI","No reserve requirement at all, as debentures are unregulated instruments"],"a":0,"e":"Under the Companies Act, 2013, NBFCs raising capital via debentures must maintain a Debenture Redemption Reserve (DRR) account under stricter norms than previously applied, distinct from the CRR/SLR requirements that apply specifically to banks."})

upsc.append({"q":"Which one of the following best captures the RBI's 'umbrella definition' of a Non-Banking Financial Company (NBFC)?","o":["A financial institution formed as a company, involved in receiving deposits or lending in any manner","Any company engaged primarily in agricultural or industrial activity","Any institution licensed to accept demand deposits like a commercial bank","A company exclusively engaged in the sale or purchase of immovable property"],"a":0,"e":"The RBI's deliberately broad 'umbrella' definition covers any company-form financial institution receiving deposits or lending in any manner — NBFCs are explicitly barred from having agriculture, industry, or immovable property sale/purchase/construction as their PRINCIPAL business, which is what distinguishes them from those other entity types."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_banking_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

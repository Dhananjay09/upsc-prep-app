import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_financial_markets (Ramesh Singh Ch.11)
# DFHI history (Chore Committee, Vaghul Committee, 2004 SBI transfer), Mutual Fund
# structure (AMC/trustees, NAV, open/closed/ETF schemes, SEBI's 2017 5-category system)
# ==================================================================

upsc.append({"q":"Which committee first recommended, as early as 1978, the establishment of a discount house to address liquidity imbalances in the Indian banking system — an idea later realised through the Discount and Finance House of India (DFHI) in 1988?","o":["The Chore Committee","The Vaghul Committee","The Narasimham Committee","The Tandon Committee"],"a":0,"e":"The Chore Committee (1978) first recommended a discount house to level liquidity imbalances; it was the later Vaghul Committee (Working Group on Money Market, 1987) that concretely suggested a discount finance institution dealing in short-term money market instruments on a 'commercial basis', a recommendation accepted by the government in setting up DFHI in 1988."})

upsc.append({"q":"Consider the following statements about the Discount and Finance House of India Limited (DFHI):\n1. It was set up in April 1988 by the RBI jointly with public sector banks and financial institutions such as LIC, GIC and UTI.\n2. In 2004, the RBI transferred its entire holding in DFHI to SBI's arm, SBI Gilts Limited, renaming it SBI DFHI.\n3. It operates only as a lender in the money market, with no borrowing role.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — DFHI/SBI DFHI operates in 'two-way' mode, functioning as both a lender AND a borrower, and deals in all money market instruments without an upper ceiling as the biggest 'primary dealer' in the economy."})

upsc.append({"q":"Which one of the following statements about the Asset Management Company (AMC) and trustee structure governing Indian mutual funds is correct?","o":["Both the AMC and the trustees have a fiduciary responsibility as they manage investors' money on their behalf","Only the trustees have fiduciary responsibility; the AMC operates purely as a commercial entity with no such duty","The AMC is regulated only by the RBI, while trustees are regulated only by SEBI","Mutual funds require no registration with any regulator, as they are self-regulated"],"a":0,"e":"Both the AMC (which runs day-to-day fund operations) and the trustees (who oversee the AMC) bear fiduciary responsibility, since they manage the hard-earned money of investors who may not understand fund management themselves; mutual funds are compulsorily registered with SEBI, which acts as the 'first wall of defence' for investors."})

upsc.append({"q":"Match List-I (type of mutual fund scheme) with List-II (its defining characteristic) and select the correct answer using the code below.\nList-I:\nA. Open-ended Scheme\nB. Closed-ended Scheme\nC. Exchange-Traded Fund (ETF)\nList-II:\n1. Units issued only once via a New Fund Offer (NFO), then listed and traded on stock exchanges for a limited tenure\n2. Available for purchase/sale on an ongoing basis directly from the fund at NAV-based price\n3. Listed and traded on exchanges like a closed-ended fund, but priced very close to NAV/underlying assets\nCodes:","o":["A-2, B-1, C-3","A-1, B-2, C-3","A-2, B-3, C-1","A-3, B-1, C-2"],"a":0,"e":"Open-ended schemes (A) allow ongoing buy/sell at NAV-based prices (2); Closed-ended schemes (B) issue units only once via an NFO, later trading on exchanges for a fixed tenure (1); ETFs (C) blend both features — exchange-listed like closed-ended funds but priced close to NAV like open-ended funds (3)."})

upsc.append({"q":"Consider the following statements about closed-ended mutual fund scheme units listed on stock exchanges:\n1. They typically trade at a discount to their Net Asset Value (NAV) for most of their tenure.\n2. This discount to NAV typically widens as the scheme's closure date approaches.\n3. On the day of the scheme's closure, the discount to NAV effectively vanishes.\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 reverses the actual pattern — the discount to NAV NARROWS (not widens) as the closure date nears, vanishing entirely on the day of closure."})

upsc.append({"q":"By when did SEBI classify mutual fund schemes into five broad categories — Debt, Equity, Hybrid, Solution-oriented, and Other schemes — to reduce clutter and ease comparison for investors, and into how many total sub-categories?","o":["October 2017; 36 sub-categories","January 2015; 24 sub-categories","March 2020; 50 sub-categories","October 2017; 20 sub-categories"],"a":0,"e":"SEBI's October 2017 classification created five broad categories further sub-divided into 36 total scheme categories (e.g., Dividend Yield Equity Fund, Banking and PSU Debt Fund), with a rule limiting each fund house to only one scheme per category to avoid duplication."})

upsc.append({"q":"Which one of the following statements about the investor choice options within Indian mutual fund schemes investing across loan and share markets is correct?","o":["Investors can typically choose among 'Loan' (100% loan market), 'Share' (100% share market), or 'Balance' (typically 60% loan, 40% share, subject to change) options","Mutual funds in India are legally barred from investing in the loan/debt market","The 'Balance' option always maintains a fixed, unchangeable 50:50 split between loan and share markets","Only institutional investors, not retail investors, can choose among these investment options"],"a":0,"e":"MF investors can choose 'Loan' (fully debt-market), 'Share' (fully equity-market), or 'Balance' (typically ~60% loan/40% share, though the split can change based on market conditions as announced by the fund) — investing across both loan and share markets is standard practice, not barred, and retail investors do have access to these choices."})

upsc.append({"q":"Assertion (A): The Discount and Finance House of India (DFHI) was established with a dual mandate.\nReason (R): Its twin objectives were to bring equilibrium of liquidity in the Indian banking system and to impart liquidity to money market instruments prevalent in the economy.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R correctly explains A — DFHI's establishment (1988) was driven precisely by these two long-standing needs: banking system liquidity equilibrium and money market instrument liquidity, addressed through its commercial 'two-way' (lender and borrower) operations."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_financial_markets_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

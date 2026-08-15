import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_national_income (Ramesh Singh Ch.1,
# National Income Accounting section) - GNP/NNP formulas, Income from Abroad
# components, factor cost vs market cost, base year revision, constant vs current price
# ==================================================================

upsc.append({"q":"Which one of the following correctly lists the three components of the 'Income from Abroad' segment used to derive a country's GNP from its GDP?","o":["Private remittances, interest on external loans, and external grants","Foreign direct investment, portfolio investment, and external commercial borrowings","Export earnings, import payments, and exchange rate fluctuations","Tourism receipts, software exports, and remittances only"],"a":0,"e":"The 'Income from Abroad' segment comprises three components: net private remittances, net interest on external loans, and net external grants — their combined balance (positive or negative) is added to GDP to arrive at GNP."})

upsc.append({"q":"Consider the following statements about India's 'Income from Abroad' components:\n1. India has consistently been a net recipient on the private remittances front, being the world's highest recipient of private remittances as of 2015.\n2. India has consistently been a net gainer on the interest-on-external-loans front, since it lends more abroad than it borrows.\n3. India offers more external grants to other countries than it receives.\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 is false — India has always been a net LOSER on interest on external loans, since it is a 'net borrower' from world economies, not a net lender, resulting in a negative balance on this component."})

upsc.append({"q":"Assertion (A): India's GNP is always lower than its GDP.\nReason (R): India's overall 'Income from Abroad' balance has consistently been negative, due to heavy outflows from trade deficits and interest payments on foreign loans.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R explains A — since India's GNP formula effectively becomes GDP minus (rather than plus) Income from Abroad, owing to the persistently negative balance in that segment, India's GNP is always lower than its GDP."})

upsc.append({"q":"Which one of the following statements about India's remittance and economic ranking data (as cited from IMF/World Bank figures around 2015-16) is correct?","o":["India was projected as the world's highest recipient of private remittances (around $72 billion in 2015), ahead of China (around $64 billion)","China received higher private remittances than India in 2015","India ranks as the world's largest economy by GDP at Purchasing Power Parity (PPP), ahead of both China and the USA","India's GNP-based PPP ranking and nominal exchange rate-based ranking were identical in April 2016"],"a":0,"e":"India topped the world in private remittances received (~$72 billion, 2015) ahead of China (~$64 billion). India ranked 3rd (not 1st) by PPP-based national income (after China and the USA), while its nominal-exchange-rate ranking was different still — 7th largest as of April 2016 — showing the two rankings are NOT identical."})

upsc.append({"q":"Which one of the following correctly gives the formula for Net National Product (NNP)?","o":["NNP = GNP - Depreciation, equivalently GDP + Income from Abroad - Depreciation","NNP = GDP + Depreciation","NNP = GNP + Income from Abroad","NNP = GDP - Income from Abroad + Depreciation"],"a":0,"e":"NNP is derived by subtracting depreciation from GNP (NNP = GNP - Depreciation), which expands to GDP + Income from Abroad - Depreciation — NNP represents the 'purest' form of a nation's income and, divided by population, yields Per Capita Income."})

upsc.append({"q":"Consider the following statements about depreciation rates and their effect on Per Capita Income (PCI) calculations:\n1. Higher rates of depreciation lead to a lower PCI for a nation, regardless of whether the depreciation rate is set on logical or policy-driven (artificial) grounds.\n2. India's depreciation rate for heavy vehicles was reduced from 40 per cent to 20 per cent after February 2000 to discourage their sales.\n3. Differences in depreciation rates across nations can affect international comparisons of national income by bodies like the IMF and World Bank.\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 reverses the actual change — India's depreciation rate for heavy vehicles (6-wheelers and above) was actually RAISED from 20% to 40% after February 2000, specifically to BOOST (not discourage) their sales, illustrating depreciation's use as a policy tool."})

upsc.append({"q":"Which one of the following statements about 'factor cost' versus 'market cost' (market price) in national income accounting is correct?","o":["Factor cost represents the producer's input cost (capital, raw materials, labour, rent, power), while market cost is derived by adding indirect taxes to the factor cost","Market cost is always lower than factor cost since taxes are subtracted from it","Factor cost includes indirect taxes while market cost excludes them","India has always calculated its national income exclusively at market cost since Independence"],"a":0,"e":"Factor cost is the producer-side input cost, while market cost (market price) is factor cost PLUS indirect taxes — making market cost generally higher, not lower. India officially switched from calculating national income at factor cost to market price only from January 2015, not since Independence."})

upsc.append({"q":"As part of the Central Statistics Office's January 2015 revision of methodology for National Accounts, the base year for calculating India's national income was revised from which year to which year?","o":["2004-05 to 2011-12","1999-2000 to 2004-05","2011-12 to 2017-18","1993-94 to 2004-05"],"a":0,"e":"The CSO revised the national accounts base year from 2004-05 to 2011-12 in January 2015, alongside switching the calculation basis from factor cost to market price, aligning India more closely with international statistical practice."})

upsc.append({"q":"Consider the following statements about the distinction between 'constant price' and 'current price' national income calculations:\n1. Constant price calculations hold inflation fixed at the level of a designated base year.\n2. Current price essentially reflects present-day inflation, analogous to the Maximum Retail Price (MRP) seen on goods.\n3. India, like most developed economies, calculates its national income primarily at current prices.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — India, like other DEVELOPING economies, calculates its national income primarily at CONSTANT prices, while it is the DEVELOPED nations that calculate primarily at current prices; India's CSO does release current-price data too, but only for statistical/supplementary purposes."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_national_income_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

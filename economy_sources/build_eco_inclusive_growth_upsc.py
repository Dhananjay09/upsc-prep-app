import json

upsc = []

# ==================================================================
# NEW UPSC TIER: eco_inclusive_growth (Ramesh Singh Ch.20/Ch.12) —
# PMJDY, JAM trinity/DBT, MUDRA Bank/PMMY, minority empowerment schemes
# ==================================================================

upsc.append({"q":"With reference to the Pradhan Mantri Jan Dhan Yojana (PMJDY), launched in August 2014, which one of the following is correct?","o":["It is complemented by the RuPay Card, together aiming at achieving financial inclusion, insurance penetration, and digitalisation","It is a scheme exclusively for providing agricultural credit to farmers, unrelated to bank account access","It was launched prior to 1991 as part of the initial banking sector reforms","It replaced the MUDRA Bank scheme upon its launch"],"a":0,"e":"PMJDY (August 2014) and the complementary RuPay Card jointly target multiple objectives — financial inclusion, insurance penetration, and digitalisation — rather than being an agricultural credit scheme; it long predates neither MUDRA (2015) which it complements, not replaces, nor does it relate to pre-1991 reforms."})

upsc.append({"q":"Consider the following statements about the MUDRA Bank (Micro Units Development and Refinance Agency Bank), launched in April 2015 as the Pradhan Mantri Mudra Yojana (PMMY):\n1. It provides refinance-route loans of up to Rs. 10 lakh to micro units through public/private banks, NBFCs, MFIs, RRBs, and district banks.\n2. Its loan products are categorised into three buckets — Shishu (up to Rs. 50,000), Kishor (Rs. 50,000 to Rs. 5 lakh), and Tarun (Rs. 5 lakh to Rs. 10 lakh).\n3. MUDRA loans carry a fixed, government-subsidised interest rate applicable uniformly across all borrowers.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is incorrect — MUDRA loans do NOT carry a fixed or uniformly subsidised interest rate; rates vary by lender and enterprise risk (Base Rate plus roughly 1% to 7% per annum as per the government's own data), with no general interest subsidy unless linked to another government scheme."})

upsc.append({"q":"Which one of the following sectors is explicitly excluded from refinancing under the MUDRA Bank scheme, despite the scheme covering traders of fruits and vegetables?","o":["Agriculture", "Handicrafts", "Food processing", "Retail trade"],"a":0,"e":"While MUDRA covers general trading activities including fruit and vegetable trade, it explicitly does NOT refinance the agriculture sector itself, which is served through other dedicated credit channels (like Kisan Credit Cards and agricultural term loans from banks/NABARD)."})

upsc.append({"q":"With reference to the rationale behind the MUDRA Bank initiative, consider the following statements:\n1. Large industries in India were estimated to employ only around 1.25 crore people, whereas micro units were estimated to employ around 12 crore people.\n2. Self-employed owners of micro units were found to rely heavily on funds from local money lenders due to a lack of access to formal credit.\n3. The average per-unit debt among these micro entrepreneurs was estimated to be in excess of Rs. 10 lakh.\nHow many of the statements given above are correct?","o":["Only two","All three","Only one","None"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is incorrect — the average per-unit debt among these 5.75 crore self-employed micro-unit owners was estimated at merely about Rs. 17,000, not in excess of Rs. 10 lakh — precisely illustrating the severe under-capitalisation MUDRA was designed to address."})

upsc.append({"q":"Which one of the following correctly describes the 'JAM trinity' and its connection to Direct Benefit Transfer (DBT) reform in India?","o":["JAM (Jan Dhan-Aadhaar-Mobile) is a technology platform intended to improve DBT delivery by enabling better targeting, reducing fake/duplicate beneficiaries, and preventing leakages and corruption in subsidy disbursal","JAM refers to a joint monitoring mechanism between the Centre and states for GST collection","JAM is an acronym for a scheme providing microfinance exclusively to women self-help groups","JAM was primarily designed to digitise land records across Indian states"],"a":0,"e":"The JAM trinity (Jan Dhan bank accounts, Aadhaar identity, Mobile numbers) underpins the technology-enabled DBT reform agenda — aimed at better targeting/inclusion of genuine beneficiaries, excluding fake accounts, and curbing leakages/corruption — and is unrelated to GST monitoring, women's microfinance schemes specifically, or land record digitisation."})

upsc.append({"q":"Consider the following schemes aimed at the socio-economic empowerment of minority communities in India:\n1. 'Nai Roshni' — for leadership development of minority women\n2. 'Padho Pardesh' — an interest subsidy scheme on educational loans for overseas studies for minority students\n3. 'USTTAD' — for upgrading skill and training in traditional arts/crafts among minorities\nHow many of the above are genuine government schemes for minority empowerment?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three are genuine schemes cited in the context of minority socio-economic empowerment — 'Nai Roshni' for women's leadership development, 'Padho Pardesh' for overseas education loan interest subsidy, and USTTAD (Upgrading Skill and Training in Traditional Arts/Crafts for Development) — alongside others like 'Seekho Aur Kamao' (Learn and Earn) and 'Nai Manzil'."})

upsc.append({"q":"Assertion (A): The disbursement of government welfare benefits requires a systematic financial channel for effective social and financial inclusion.\nReason (R): Schemes like PMJDY and the RuPay Card make monitoring easier and local bodies more accountable, thereby strengthening financial empowerment.\nWhich one of the following is correct?","o":["Both A and R are true, and R is a correct explanation of A","Both A and R are true, but R is not a correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both statements are true and R explains A — the need for a systematic disbursement channel (A) is directly addressed by PMJDY/RuPay's role in improving monitoring and local accountability (R), making the reasoning a correct explanation rather than a merely coincidental true statement."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_inclusive_growth_upsc.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

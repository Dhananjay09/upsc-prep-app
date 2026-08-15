import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_industry_policy (Ramesh Singh Ch.9)
# Industrial Policy Resolution 1956 Schedule A/B/C classification, Industrial
# Policy Statement 1969 (MRTP Act/limit history), 4 licensing-review committees,
# Industrial Policy Statement 1973 (core industries)
# ==================================================================

upsc.append({"q":"Under the Industrial Policy Resolution, 1956's classification of industries into Schedules A, B and C, which one of the following statements is correct?","o":["Schedule A gave the Central government complete monopoly over 17 industrial areas, later expanding to 254 PSUs by 1991 through nationalisation drives","Schedule B gave the states complete monopoly with no role for private enterprise","Schedule C industries were entirely free from licensing requirements","Schedule A industries were reserved exclusively for joint ventures between state and private capital"],"a":0,"e":"Schedule A conferred Central government monopoly over 17 industrial areas (the original CPSUs/PSUs), which grew to 254 PSUs by 1991 partly through 1960s-80s nationalisation drives; Schedule B allowed state initiative WITHOUT monopoly (private sector could also participate), and Schedule C (residual industries) still fell under IDR Act licensing, not exemption from it."})

upsc.append({"q":"Which one of the following statements about Schedule B industries under the Industrial Policy Resolution, 1956 is correct?","o":["State governments were expected to take the initiative, with private sector expected to follow, and neither states nor private firms held exclusive monopoly","State governments held complete monopoly, identical to the Schedule A arrangement for the Centre","Schedule B industries were entirely exempt from compulsory licensing","Schedule B consisted of only foreign-owned enterprises"],"a":0,"e":"Schedule B (12 industrial areas) envisaged state government initiative with private-sector follow-up, but unlike Schedule A, neither states nor private enterprises held monopoly — it also carried compulsory licensing provisions, unlike the incorrect exemption claim."})

upsc.append({"q":"Which one of the following famous descriptions did Pandit Jawaharlal Nehru use for Public Sector Undertakings (PSUs) under the Industrial Policy Resolution, 1956 — a phrase repeated in the Second Five Year Plan?","o":["'Temples of modern India'","'Engines of growth'","'Pillars of self-reliance'","'Instruments of socialism'"],"a":0,"e":"Nehru famously termed PSUs the 'temples of modern India', a description echoed in the Second Five Year Plan (1956-61), symbolically underscoring their centrality to the post-Independence industrialisation vision."})

upsc.append({"q":"Consider the following statements about the licensing regime established under the Industrial Policy Resolution, 1956:\n1. It came to be popularly known as the 'Licence-Quota-Permit' regime (raj).\n2. Only Schedule C industries were subject to compulsory licensing, while Schedule B industries were exempt.\n3. By 1988-89, rapid PSU expansion accounted for more than half of the country's GDP.\nWhich of the statements given above is/are correct?","o":["1 and 3 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 3 are correct. Statement 2 reverses the facts — ALL Schedule B industries and a number of Schedule C industries were brought under compulsory licensing, giving rise to the Licence-Quota-Permit regime, not the other way around."})

upsc.append({"q":"Match List-I (committee on industrial licensing policy review) with List-II (year of establishment) and select the correct answer using the code below.\nList-I:\nA. Swaminathan Committee\nB. Mahalanobis Committee\nC. R.K. Hazari Committee\nD. S. Dutt Committee\nList-II:\n1. 1964\n2. 1967\n3. 1969\n4. 1964\nCodes:","o":["A-1, B-4, C-2, D-3","A-4, B-1, C-2, D-3","A-1, B-4, C-3, D-2","A-2, B-3, C-1, D-4"],"a":0,"e":"Both the Swaminathan Committee (A) and Mahalanobis Committee (B) were set up in 1964, the R.K. Hazari Committee (C) in 1967, and the S. Dutt Committee (D) in 1969 — four separate committees that reviewed India's industrial licensing policy shortcomings, ultimately informing the 1969 policy changes."})

upsc.append({"q":"Consider the following statements about the Monopolistic and Restrictive Trade Practices (MRTP) Act, introduced via the Industrial Policy Statement of 1969:\n1. Firms with assets of Rs. 25 crore or more originally required government permission before expansion, greenfield ventures, or takeovers, and came to be called 'MRTP Companies'.\n2. The MRTP asset threshold was revised upward to Rs. 50 crore in 1980 and further to Rs. 100 crore in 1985.\n3. An MRTP Commission was established for redressal of prohibited and restricted trade practices.\nHow many of the statements given above are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements are correct: the original Rs. 25 crore threshold for 'MRTP Companies' was raised to Rs. 50 crore (1980) and then Rs. 100 crore (1985) — logical revisions since the low threshold was hindering these firms' organic growth and technological upgrading — and a dedicated MRTP Commission handled trade-practice redressal."})

upsc.append({"q":"Which one of the following statements about the stated objectives of the 1956-1969 industrial licensing policy is correct?","o":["It aimed at exploiting resources for balanced development, checking concentration of economic power, controlling prices of licensed industries' goods, and channelising investment per planning priorities — though in practice powerful industrial houses continued to secure fresh licences at the expense of new entrepreneurs","It succeeded fully in preventing established industrial houses from creating hurdles for new entrants","It had no connection to checking concentration of economic power","It was designed exclusively to benefit foreign multinational corporations"],"a":0,"e":"The licensing policy's stated goals (resource exploitation for development, price control, checking concentration of economic power, planned investment channelling) were undermined in practice — powerful industrial houses continued cornering fresh licences, and established firms used various trade practices to force newer entrants into sell-outs and takeovers."})

upsc.append({"q":"The Industrial Policy Statement of 1973 introduced which new classificatory term for industries deemed fundamental to industrial development, later also referred to as 'basic' or 'infrastructure' industries?","o":["Core industries","Sunrise industries","Strategic industries","Frontier industries"],"a":0,"e":"The 1973 Statement introduced the 'core industries' classification for fundamentally important sectors like iron and steel, cement, coal, crude oil, oil refining and electricity — later also termed basic/infrastructure industries."})

upsc.append({"q":"Consider the following statements about the six 'core industries' identified under the Industrial Policy Statement, 1973:\n1. They included iron and steel, cement, coal, crude oil, oil refining and electricity.\n2. Private firms could apply for licences in core industries not falling under Schedule A of the 1956 policy, provided their total assets were Rs. 20 crore or more.\n3. All six core industries were placed under complete Central government monopoly with no private sector role permitted.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — private firms with assets of Rs. 20 crore or more COULD apply for licences in core industries outside Schedule A, meaning the sector was not under complete, exclusive Central monopoly."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_industry_policy_upsc2.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

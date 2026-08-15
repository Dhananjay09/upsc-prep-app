import json

upsc = []

# ==================================================================
# EXTRA UPSC BATCH (no dedup check): eco_planning_niti (Ramesh Singh Ch.4,
# types-of-planning classification) - systems vs normative planning, sectoral vs
# spatial planning, NITI Aayog's normative shift, behavioural-nudge policymaking
# ==================================================================

upsc.append({"q":"Which one of the following correctly distinguishes 'systems planning' from 'normative planning'?","o":["Systems planning gives less emphasis to social and institutional dimensions (caste, religion, region, language, etc.), while normative planning gives due importance to such socio-institutional factors","Systems planning is only used in developing countries, while normative planning is only used in developed countries","Normative planning is a purely technical, values-free approach, while systems planning incorporates social values","Systems planning and normative planning are simply two names for the same planning approach"],"a":0,"e":"Systems planning pursues established goals with minimal regard for social/institutional factors, whereas normative planning explicitly factors in socio-institutional dimensions like customs, traditions and ethos — the text further notes that a purely normative approach is 'naturally not fit for Indian conditions' due to India's high social diversity, requiring adaptation."})

upsc.append({"q":"Which Economic Survey is identified as probably the first Government of India document to advocate a normative approach to planning in India?","o":["Economic Survey 2010-11","Economic Survey 1991-92","Economic Survey 2004-05","Economic Survey 1999-2000"],"a":0,"e":"The Economic Survey 2010-11 is credited as probably the first official document advocating that Indian planning connect with the customs, traditions and ethos of the population to improve programme acceptability — a precursor to NITI Aayog's later normative orientation."})

upsc.append({"q":"Consider the following statements about NITI Aayog's approach to planning, as replacing the Planning Commission in January 2015:\n1. It signalled India's official shift towards a more normative approach to planning.\n2. It has been guided by a development model described as 'all round, all pervasive, all inclusive and holistic'.\n3. It has been tasked with drawing on the vitality of the country's ethos, culture and sustenance.\nHow many of the statements given above are correct?","o":["All three","Only two","Only one","None"],"a":0,"e":"All three statements correctly describe NITI Aayog's stated orientation — moving from the largely systems-based planning of the Commission era towards a normative, culturally-grounded, holistic development model."})

upsc.append({"q":"Which one of the following examples of behavioural/social-norm-influencing policymaking was highlighted in the Economic Survey 2015-16 as part of India's move towards normative policymaking?","o":["Persuading the rich to voluntarily give up subsidies they do not need","Setting up new public sector banks","Announcing a new industrial licensing policy","Revising the CRR and SLR ratios"],"a":0,"e":"The Economic Survey 2015-16 cited examples including persuading affluent citizens to voluntarily give up unneeded subsidies, reducing social prejudice against girls, educating on open-defecation health externalities, and encouraging citizens to keep public spaces clean — all illustrating behavioural, normative policy interventions, distinct from purely institutional/monetary measures."})

upsc.append({"q":"Which global report, cited alongside the Economic Survey 2015-16, also highlighted the importance of studying behavioural change for effective policymaking?","o":["World Development Report 2015 (World Bank)","Human Development Report 2015 (UNDP)","Global Competitiveness Report 2015 (WEF)","World Economic Outlook 2015 (IMF)"],"a":0,"e":"The World Bank's World Development Report 2015 specifically emphasised the importance of behavioural change in policymaking, reinforcing the same normative-planning direction highlighted in India's Economic Survey 2015-16."})

upsc.append({"q":"Which one of the following correctly distinguishes 'sectoral planning' from 'spatial planning' as further classifications of economic planning?","o":["Sectoral planning emphasises specific economic sectors like agriculture, industry, or services, while spatial planning views development within a geographical/spatial framework","Sectoral planning is concerned only with geography, while spatial planning is concerned only with specific economic sectors","Sectoral and spatial planning are identical concepts used interchangeably","Sectoral planning applies only at the national level, while spatial planning applies only at the international level"],"a":0,"e":"Sectoral planning focuses on specific economic sectors (agriculture, industry, services), while spatial planning frames development in terms of geographical/spatial dimensions shaped by national economic development pressures and requirements — Indian planning has been described as essentially single-level with greater reliance on the sectoral approach."})

upsc.append({"q":"Consider the following statements about the various classifications of economic planning based on different points of view:\n1. From a territorial point of view, planning can be regional or national.\n2. From a participatory point of view, planning can be categorised as centralised or decentralised.\n3. From a temporal point of view, planning is always necessarily long-term, never short-term.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1, 2 and 3","2 and 3 only","1 only"],"a":0,"e":"Statements 1 and 2 are correct. Statement 3 is false — from a temporal point of view, planning can be EITHER long-term or short-term (in a relative sense), not necessarily always long-term."})

upsc.append({"q":"Which one of the following statements about the evolution of Indian planning's approach since the early 1990s is correct?","o":["While Indian planning has essentially remained single-level with greater reliance on the sectoral approach, multi-level regional and normative dimensions have been increasingly emphasised since the early 1990s","Indian planning abandoned the sectoral approach entirely in favour of purely spatial planning after 1991","India adopted a fully normative planning model immediately after Independence in 1947","Regional planning dimensions were emphasised only before 1991 and have since been discontinued"],"a":0,"e":"Indian planning has retained its essentially single-level, sectoral character, but has increasingly incorporated multi-level regional and normative dimensions since the early 1990s — not a wholesale abandonment of sectoral planning nor an immediate post-Independence embrace of normative planning."})

# ==================================================================
# ASSEMBLY & VALIDATION (structural only)
# ==================================================================

texts = [q["q"] for q in upsc]
print("Total:", len(upsc), "| unique:", len(set(texts)))
for q in upsc:
    assert len(q["o"]) == 4, ("option count", q["q"], len(q["o"]))
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == len(q["o"]), ("duplicate option text!", q["q"])

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/eco_planning_niti_upsc3.json", "w") as f:
    json.dump(upsc, f, indent=2, ensure_ascii=False)

print("Saved.")

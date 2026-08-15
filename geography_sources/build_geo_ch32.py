import json

upsc = []

# ==================================================================
# CHAPTER: INDIA - LOCATION (NCERT XI Part 2, Ch.1) - standalone NCERT-only chapter
# ==================================================================

upsc.append({"q":"Consider the following statements about India's latitudinal and longitudinal extent, per NCERT:\n1. India's mainland extends from Kashmir in the north to Kanniyakumari in the south, and from Gujarat in the west to Arunachal Pradesh in the east.\n2. The southern boundary of India extends up to 6°45' N latitude in the Bay of Bengal.\n3. The actual north-south distance (3,214 km) is greater than the actual east-west distance (2,933 km), even though both the latitudinal and longitudinal extents are roughly equal at about 30 degrees.\nWhich of the statements given above is/are correct?","o":["1, 2 and 3","1 and 2 only","2 and 3 only","1 and 3 only"],"a":0,"e":"All three statements are correct. NCERT explains that although the latitudinal and longitudinal extents are both roughly 30 degrees, the actual north-south distance measured is greater than the east-west distance, because the distance between two longitudes decreases towards the poles while the distance between two latitudes remains constant."})

upsc.append({"q":"Which one of the following statements about India's standard meridian and time, per NCERT, is NOT correct?","o":["India requires multiple standard time zones because its longitudinal extent causes a time difference of nearly two hours between its easternmost and westernmost parts","82°30' E has been selected as India's 'standard meridian' because there is a general international understanding to select standard meridians in multiples of 7°30' of longitude","Indian Standard Time (IST) is ahead of Greenwich Mean Time by 5 hours and 30 minutes","The USA, due to its vast east-to-west extent, has seven time zones, unlike India which uses a single standard time"],"a":0,"e":"This statement is incorrect — despite the roughly two-hour natural time difference between India's east and west, NCERT explains India uses only ONE standard time (IST) based on the 82°30' E meridian, not multiple time zones. The other three statements are correct."})

upsc.append({"q":"Consider the following statements about India's size and boundaries, per NCERT:\n1. India, with an area of 3.28 million sq. km, accounts for about 2.4% of the world's land surface area and is the seventh largest country in the world.\n2. India's territorial limit extends into the sea up to 12 nautical miles (about 21.9 km) from the coast.\n3. India's coastline measures 6,100 km for the mainland alone, and 7,517 km when the entire geographical coast of the mainland plus the Andaman-Nicobar and Lakshadweep island groups is included.\nWhich of the statements given above is/are correct?","o":["1, 2 and 3","1 and 2 only","2 and 3 only","1 and 3 only"],"a":0,"e":"All three statements are correct, matching NCERT's figures for India's global area share/rank, its 12-nautical-mile territorial sea limit, and its mainland versus total (including island groups) coastline lengths."})

upsc.append({"q":"Match List-I (Physical Barrier/Feature, per NCERT's account of India and its neighbours) with List-II (Associated Description) and select the correct answer using the code below.\nList-I:\nA. The Himalayas (with Hindukush and Sulaiman ranges)\nB. Mountain passes (Khyber, Bolan, Shipkila, Nathula, Bomdila)\nC. Gulf of Mannar and Palk Strait\nD. Indian subcontinent (as a geographic entity)\nList-II:\n1. Separates Sri Lanka from India\n2. Includes Pakistan, Nepal, Bhutan, Bangladesh and India, bounded by the Himalayas and the Indian Ocean\n3. Points where it was comparatively easier to cross the otherwise formidable mountain barrier\n4. Formidable physical barrier that historically contributed to a unique regional identity\nCodes:","o":["A-4, B-3, C-1, D-2","A-3, B-4, C-1, D-2","A-4, B-3, C-2, D-1","A-4, B-1, C-3, D-2"],"a":0,"e":"The correct match is A-4, B-3, C-1, D-2: the Himalayas formed a formidable barrier shaping a unique regional identity; specific mountain passes were the exceptions allowing crossing; the Gulf of Mannar and Palk Strait separate Sri Lanka from India; and the Indian subcontinent comprises the five countries bounded by the Himalayas and the Indian Ocean."})

upsc.append({"q":"Assertion (A): Peninsular India's maritime location has provided it with links to neighbouring regions through sea and air routes.\nReason (R): India is located in the south-central part of the continent of Asia, bordering the Indian Ocean and its two arms extending as the Bay of Bengal and the Arabian Sea.\nWhich one of the following is correct in respect of the above Assertion (A) and Reason (R)?","o":["Both A and R are true, and R is the correct explanation of A","Both A and R are true, but R is NOT the correct explanation of A","A is true, but R is false","A is false, but R is true"],"a":0,"e":"Both are true and R explains A — NCERT explicitly attributes Peninsular India's maritime links with neighbouring regions to its location in south-central Asia, bordered by the Indian Ocean's two arms (Bay of Bengal and Arabian Sea), which together provide the geographic basis for its sea and air connectivity."})

upsc.append({"q":"Which one of the following countries does NOT share a land frontier with India, per NCERT's account of India's neighbours?","o":["Sri Lanka","Pakistan","Bangladesh","Myanmar"],"a":0,"e":"Sri Lanka is explicitly described by NCERT as an island country in the Indian Ocean, separated from India by the Gulf of Mannar and Palk Strait, and thus has no land frontier with India — unlike Pakistan, Bangladesh and Myanmar, which are land neighbours."})

upsc.append({"q":"Consider the following statements about the physical diversity of India arising from its size, per NCERT:\n1. India's great size has endowed it with lofty mountains in the north, large rivers such as the Ganga, Brahmaputra, Mahanadi, Krishna, Godavari and Kaveri, and the vast sandy expanse of the Marusthali desert.\n2. Green forested hills occur in northeast and south India as part of this same physical diversity.\n3. This diversity is attributed by NCERT solely to India's longitudinal extent, with latitudinal extent playing no role.\nWhich of the statements given above is/are correct?","o":["1 and 2 only","1 and 3 only","2 and 3 only","1, 2 and 3"],"a":0,"e":"Statement 3 is incorrect — NCERT attributes India's large variations in landforms, climate, soil types and natural vegetation to its LATITUDINAL location (spanning tropical to sub-tropical/warm temperate zones), not solely to longitudinal extent. Statements 1 and 2 are correct."})

# ==================================================================
# ASSEMBLY & VALIDATION
# ==================================================================

data = {"basic": [], "intermediate": [], "advanced": [], "upsc": upsc}

all_q = upsc
texts = [q["q"] for q in all_q]
print("counts:", {k: len(v) for k, v in data.items()})
print("total:", len(all_q))
print("unique:", len(set(texts)))
for q in all_q:
    assert len(q["o"]) == 4, q["q"]
    assert 0 <= q["a"] <= 3, q["q"]
    assert len(set(q["o"])) == 4, ("duplicate option text!", q["q"])
multi = sum(1 for q in all_q if "\n" in q["q"] or "List-" in q["q"] or "Assertion" in q["q"])
print("multi-format %:", round(100*multi/len(all_q), 1))

chapter = {
    "id": "india_location",
    "title": "India - Location",
    "desc": "Indian physical geography (from NCERT XI Part 2 'India: Physical Environment', Ch.1 'India - Location'): India's latitudinal/longitudinal extent and its implications; the standard meridian and Indian Standard Time; India's size, area rank and coastline; the Indian subcontinent as a geographic entity bounded by the Himalayas and the Indian Ocean; India's neighbouring countries and physical barriers. A standalone NCERT-only chapter, since Goh Cheng Leong's world-geography textbook does not treat India's specific location and boundaries in this depth.",
    "questions": data
}

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/geo_ch32_location_v2.json", "w") as f:
    json.dump(chapter, f, indent=2, ensure_ascii=False)

print("Saved.")

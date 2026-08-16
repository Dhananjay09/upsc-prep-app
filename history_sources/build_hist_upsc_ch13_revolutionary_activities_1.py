import json

qs = []

qs.append({"q":"The first phase of revolutionary activities (1907-1917) is described in the chapter as primarily a fallout of:","o":["The Swadeshi and Boycott Movement","The Non-Cooperation Movement","The Quit India Movement","The Simon Commission agitation"],"a":0,"e":"The first phase of revolutionary activity emerged as a by-product of the growth of militant nationalism and the Swadeshi and Boycott Movement; the second phase later stemmed from the Non-Cooperation Movement."})

qs.append({"q":"The revolutionaries of this period, rather than attempting a violent mass revolution or subverting army loyalty, chose to follow the methods of:","o":["Russian nihilists and Irish nationalists","Chinese communists","Ottoman reformists","African National Congress activists"],"a":0,"e":"The revolutionaries modelled their methods — individual assassinations, dacoities for funds — on the tactics of Russian nihilists and Irish nationalists."})

qs.append({"q":"The Anushilan Samiti, one of the earliest revolutionary organisations in Bengal, was founded in Calcutta by:","o":["Promotha Mitter","Jnanendranath Basu","Barindra Kumar Ghosh","Bhupendranath Dutta"],"a":0,"e":"Promotha Mitter founded the Anushilan Samiti in Calcutta, which included figures like Jatindranath Banerjee and Barindra Kumar Ghosh."})

qs.append({"q":"The weekly newspaper Yugantar, associated with an inner circle of the Anushilan Samiti and advocating revolutionary violence, was started in April 1906 by:","o":["Barindra Kumar Ghosh and Bhupendranath Dutta","Promotha Mitter and Jnanendranath Basu","Rashbehari Bose and Sachin Sanyal","Jatindranath Mukherjee and Pulin Das"],"a":0,"e":"Barindra Kumar Ghosh and Bhupendranath Dutta started the Yugantar weekly in 1906, advocating revolutionary violence."})

qs.append({"q":"The 1908 Muzaffarpur bomb incident, in which two British women were accidentally killed, was carried out by which revolutionaries who intended to target the judge Kingsford?","o":["Prafulla Chaki and Khudiram Bose","Barindra Kumar Ghosh and Aurobindo Ghosh","Basant Kumar Biswas and Amir Chand","Rashbehari Bose and Sachin Sanyal"],"a":0,"e":"Prafulla Chaki and Khudiram Bose threw the bomb intended for Kingsford at Muzaffarpur; Chaki shot himself, while Khudiram Bose was tried and hanged."})

qs.append({"q":"The Alipore Conspiracy Case (also called the Manicktolla bomb conspiracy or Muraripukur conspiracy), which followed the Muzaffarpur incident, saw which nationalist leader acquitted after being defended by Chittaranjan Das?","o":["Aurobindo Ghosh","Barindra Kumar Ghosh","Ullaskar Dutt","Bhupendranath Dutta"],"a":0,"e":"Aurobindo Ghosh was acquitted in the Alipore Conspiracy Case after C.R. Das's defence exposed the flimsy evidence against him, while Barindra Ghosh and Ullaskar Dutt received death sentences later commuted to life imprisonment."})

qs.append({"q":"During the Alipore trial, the approver-turned-Crown-witness Narendra Gosain (Goswami) was shot dead in jail by:","o":["Satyendranath Bose and Kanailal Dutta","Prafulla Chaki and Khudiram Bose","Amir Chand and Avadh Behari","Basant Kumar Biswas and Rashbehari Bose"],"a":0,"e":"Satyendranath Bose and Kanailal Dutta, co-accused in the Alipore case, shot the approver Narendra Gosain dead within the jail."})

qs.append({"q":"The 1912 bomb attack on Viceroy Lord Hardinge during his ceremonial entry into the new capital of Delhi through Chandni Chowk was masterminded by:","o":["Rashbehari Bose and Sachin Sanyal","Aurobindo Ghosh and Barindra Ghosh","Madanlal Dhingra","Jatindranath Mukherjee"],"a":0,"e":"Rashbehari Bose and Sachin Sanyal organised the bomb attack on Viceroy Hardinge in December 1912; Hardinge was injured but survived."})

qs.append({"q":"The investigation into the 1912 Delhi bomb attack on Viceroy Hardinge led to which trial, in which Basant Kumar Biswas, Amir Chand and Avadh Behari were convicted and executed?","o":["The Delhi Conspiracy trial","The Alipore Conspiracy Case","The Nasik Conspiracy Case","The Lahore Conspiracy Case"],"a":0,"e":"The Delhi Conspiracy trial followed the 1912 bomb attack on Hardinge; Basant Kumar Biswas, Amir Chand and Avadh Behari were convicted and executed, while Rashbehari Bose evaded arrest."})

qs.append({"q":"Jatindranath Mukherjee, popularly known as Bagha Jatin, led which revolutionary group and organised the 'German Plot' (Zimmerman Plan) to import arms during World War I?","o":["The Jugantar (western Anushilan) group","The Ghadr Party","Abhinav Bharat","The Berlin Committee"],"a":0,"e":"Bagha Jatin led the western Anushilan/Jugantar group, coordinating the 'German Plot' to import German arms and organise an all-India insurrection during World War I."})

qs.append({"q":"Bagha Jatin's call \"We shall die to awaken the nation\" is associated with his final confrontation with police, which occurred at:","o":["Balasore, on the Orissa coast, in September 1915","Muzaffarpur, in 1908","Chandni Chowk, Delhi, in 1912","Nasik, in 1909"],"a":0,"e":"Bagha Jatin died in a gun-battle with police at Balasore on the Orissa coast in September 1915, after the German Plot to import arms was betrayed."})

qs.append({"q":"Which of the following describes a key limitation of Bengal's revolutionary movement, as noted in the chapter's evaluation?","o":["Overemphasis on Hindu religious symbolism kept Muslims aloof, and its narrow upper-caste social base excluded mass participation","It received full support from the Muslim League throughout","It successfully mobilised the peasantry across Bengal","It had no impact whatsoever on the educated youth"],"a":0,"e":"The Bengal revolutionary movement's Hindu religious overtones alienated Muslims, and its narrow, largely upper-caste base limited mass participation, ultimately failing against state repression."})

qs.append({"q":"The first revolutionary activity in Maharashtra, involving the organisation of the Ramosi Peasant Force to instigate an armed revolt by disrupting communication lines, was led in 1879 by:","o":["Vasudev Balwant Phadke","V.D. Savarkar","Chapekar brothers","Bal Gangadhar Tilak"],"a":0,"e":"Vasudev Balwant Phadke organised the Ramosi Peasant Force in 1879, aiming to expel the British through armed revolt and disruption of communications, though the effort was suppressed prematurely."})

qs.append({"q":"The Chapekar brothers, Damodar and Balkrishna, who were disciples of Tilak's militant nationalism, are notable for assassinating which official in 1897?","o":["Rand, the Plague Commissioner of Poona","Jackson, the Collector of Nasik","Kingsford, the judge at Muzaffarpur","Curzon-Wyllie, the India Office bureaucrat"],"a":0,"e":"The Chapekar brothers murdered Rand, the Plague Commissioner of Poona, along with Lieutenant Ayerst, in 1897."})

qs.append({"q":"The secret society Mitra Mela, organised by V.D. Savarkar and his brother in 1899, merged in 1904 with which organisation named after Mazzini's 'Young Italy'?","o":["Abhinav Bharat","Anushilan Samiti","Ghadr Party","Berlin Committee"],"a":0,"e":"Mitra Mela merged with Abhinav Bharat in 1904, an organisation inspired by Mazzini's 'Young Italy', with Nasik, Poona and Bombay becoming centres of bomb manufacture."})

qs.append({"q":"A.M.T. Jackson, the Collector of Nasik and a well-known Indologist, was assassinated in 1909 by which member of Abhinav Bharat?","o":["Anant Lakshman Kanhere","Madanlal Dhingra","Khudiram Bose","Basant Kumar Biswas"],"a":0,"e":"Anant Lakshman Kanhere, a member of Abhinav Bharat, assassinated A.M.T. Jackson, the Collector of Nasik, in 1909."})

qs.append({"q":"Following the Jackson assassination and the discovery of an armed revolution conspiracy, which leader was identified as the 'brain, leader and moving spirit' of Abhinav Bharat's conspiracy and sentenced to transportation for life?","o":["V.D. Savarkar","Anant Lakshman Kanhere","Lala Hardayal","Rashbehari Bose"],"a":0,"e":"V.D. Savarkar was identified as the mastermind of the conspiracy and sentenced to transportation for life with forfeiture of his property."})

qs.append({"q":"In Punjab, extremism was fuelled by frequent famines, rising land revenue and irrigation tax, and the zamindars' practice of:","o":["'Begar' (forced unpaid labour)","Sati","Purdah","Kulinism"],"a":0,"e":"The practice of 'begar' (forced labour imposed by zamindars), along with agrarian distress, fuelled extremism in Punjab."})

qs.append({"q":"Lala Lajpat Rai's newspaper in Punjab, which carried the motto of 'self-help at any cost', was called:","o":["Punjabee","Bharat Mata","Kesari","Yugantar"],"a":0,"e":"Lala Lajpat Rai's Punjabee carried the motto of self-help at any cost, reflecting Punjab's militant nationalist current."})

qs.append({"q":"Ajit Singh (Bhagat Singh's uncle) organised the extremist Anjuman-i-Mohisban-i-Watan in Lahore, bringing out which journal?","o":["Bharat Mata","Punjabee","Sandhya","Kal"],"a":0,"e":"Ajit Singh's organisation published the journal Bharat Mata; before turning fully extremist, his group had urged non-payment of revenue and water rates among Chenab colonists."})

qs.append({"q":"Shyamji Krishnavarma founded the Indian Home Rule Society ('India House') in London in 1905, along with which journal?","o":["The Indian Sociologist","Bande Mataram","The Ghadr","Free Hindustan"],"a":0,"e":"Shyamji Krishnavarma's India House in London published The Indian Sociologist and served as a hub for radical Indian students, including Savarkar and Hardayal."})

qs.append({"q":"Madanlal Dhingra, a member of the India House circle in London, is notable for assassinating which India Office official in 1909?","o":["Curzon-Wyllie","A.M.T. Jackson","Rand","Kingsford"],"a":0,"e":"Madanlal Dhingra assassinated Curzon-Wyllie, an India Office bureaucrat, in London in 1909, after which India House became too dangerous for revolutionaries."})

qs.append({"q":"Madame Bhikaji Cama, a Parsi revolutionary who operated from Paris and Geneva and developed contacts with French socialists, brought out which journal?","o":["Bande Mataram","The Indian Sociologist","Punjabee","Kesari"],"a":0,"e":"Madame Bhikaji Cama published the journal Bande Mataram from her base in Paris and Geneva as part of European revolutionary networks."})

qs.append({"q":"After 1909, Virendranath Chattopadhyaya chose which European city as his base for revolutionary activity, given deteriorating Anglo-German relations?","o":["Berlin","Paris","Geneva","London"],"a":0,"e":"Virendranath Chattopadhyaya based himself in Berlin after 1909, taking advantage of the worsening Anglo-German relationship, later helping found the Berlin Committee for Indian Independence."})

qs.append({"q":"The Ghadr Party, organised around a weekly newspaper by the same name, had its headquarters at:","o":["San Francisco","Vancouver","Berlin","London"],"a":0,"e":"The Ghadr Party was headquartered at San Francisco, with branches along the US and Canadian Pacific coast, drawing largely on Punjabi migrants."})

qs.append({"q":"Which of the following were the moving spirits behind the Ghadr Party?\n1. Lala Hardayal\n2. Kartar Singh Saraba\n3. Bhagwan Singh\n4. Rashbehari Bose\nHow many of the above are correctly identified as Ghadr Party leaders (as opposed to those who joined its activities in India during the war)?","o":["Only three","All four","Only two","Only one"],"a":0,"e":"Lala Hardayal, Kartar Singh Saraba and Bhagwan Singh were core Ghadr leaders in North America; Rashbehari Bose was contacted separately to lead operations in India during the failed 1915 uprising."})

qs.append({"q":"The Komagata Maru incident of 1914, which created an explosive situation in Punjab and encouraged the Ghadr Party, involved a ship carrying passengers from:","o":["Singapore to Vancouver, who were turned back by Canadian authorities","Bombay to London, denied entry by British authorities","Calcutta to San Francisco, denied entry by American authorities","Karachi to Aden, denied entry by colonial officials"],"a":0,"e":"The Komagata Maru carried about 370 Sikh and Punjabi Muslim would-be immigrants from Singapore to Vancouver; they were turned back after two months and later clashed with police at Budge Budge near Calcutta."})

qs.append({"q":"The clash between Komagata Maru passengers and police at Budge Budge near Calcutta in September 1914 resulted in:","o":["22 deaths","5 deaths","100 deaths","No casualties"],"a":0,"e":"The confrontation at Budge Budge resulted in 22 deaths when the ship's inmates refused to board the Punjab-bound train."})

qs.append({"q":"The Ghadr Party's planned armed revolt at the Ferozepur, Lahore and Rawalpindi garrisons was fixed for which date in 1915, though it was foiled by treachery?","o":["February 21, 1915","September 1915","March 1915","December 1912"],"a":0,"e":"The Ghadrites planned an armed revolt for February 21, 1915, but the plan was foiled at the last moment due to betrayal by an informer."})

qs.append({"q":"To suppress the Ghadr movement, the British government passed which key repressive legislation in March 1915?","o":["Defence of India Act","Rowlatt Act","Vernacular Press Act","Criminal Law Amendment Act"],"a":0,"e":"The Defence of India Act, passed in March 1915, was the primary legal instrument used to crush the Ghadr movement, enabling detentions without trial and special courts."})

qs.append({"q":"Which of the following best describes the Ghadr movement's ideological achievement, according to the chapter's evaluation, despite its political and military failure?","o":["It preached militant nationalism with a completely secular approach","It successfully united all Indian princely states against the British","It achieved complete independence for Punjab","It permanently ended communal tensions in India"],"a":0,"e":"The Ghadr movement's main achievement was ideological — promoting militant, secular nationalism — even though it failed militarily due to poor organisation and premature exposure of its plans."})

qs.append({"q":"The Berlin Committee for Indian Independence, established in 1915 with German foreign office support under the 'Zimmerman Plan', included which of the following founders?","o":["Virendranath Chattopadhyay, Bhupendranath Dutta and Lala Hardayal","Rashbehari Bose and Sachin Sanyal","Ajit Singh and Bhai Parmanand","Aurobindo Ghosh and Barindra Ghosh"],"a":0,"e":"Virendranath Chattopadhyay, Bhupendranath Dutta and Lala Hardayal, with German assistance, founded the Berlin Committee for Indian Independence in 1915."})

qs.append({"q":"The mission led by Raja Mahendra Pratap Singh, Barkatullah and Obaidullah Sindhi to Kabul during World War I aimed to:","o":["Organise a 'provisional Indian government' with the help of Crown Prince Amanullah","Negotiate a treaty between Afghanistan and British India","Establish a Ghadr Party branch in Afghanistan","Recruit Afghan soldiers for the British Indian Army"],"a":0,"e":"The Kabul mission sought to establish a provisional Indian government in exile with Afghan support, aided by Crown Prince Amanullah."})

qs.append({"q":"The mutiny at Singapore on February 15, 1915, involving the Punjabi Muslim 5th Light Infantry and the 36th Sikh battalion, was led by:","o":["Jamadar Chisti Khan, Jamadar Abdul Gani and Subedar Daud Khan","Rashbehari Bose and Sachin Sanyal","Kartar Singh Saraba and Bhagwan Singh","Lala Hardayal and Barkatullah"],"a":0,"e":"The Singapore Mutiny of February 1915 was led by Jamadar Chisti Khan, Jamadar Abdul Gani and Subedar Daud Khan before being crushed with severe reprisals."})

qs.append({"q":"Which of the following factors contributed to the temporary decline in revolutionary activity after the First World War?","o":["Release of prisoners under the Defence of India Rules, Montagu's August 1917 statement promising constitutional reforms, and the arrival of Gandhi with a non-violent programme","Complete elimination of all revolutionary leaders","Total absence of any nationalist sentiment after 1917","Permanent alliance between revolutionaries and the British government"],"a":0,"e":"A conciliatory atmosphere following Montagu's 1917 statement, the release of detained prisoners, and Gandhi's emergence with non-violent non-cooperation combined to reduce revolutionary activity temporarily after World War I."})

for q in qs:
    assert len(q["o"]) == 4, q["q"]
    assert 0 <= q["a"] <= 3
    assert len(set(q["o"])) == 4, q["q"]

print(f"Total questions: {len(qs)}")

out = {
    "id": "hist_upsc_revolutionary_activities_1",
    "title": "First Phase of Revolutionary Activities (1907-1917)",
    "desc": "Revolutionary activities in Bengal, Maharashtra, Punjab, and abroad (India House, Ghadr Party, Berlin Committee), the Komagata Maru incident, and their decline",
    "questions": qs
}

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/hist_upsc_ch13_revolutionary_activities_1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Saved.")

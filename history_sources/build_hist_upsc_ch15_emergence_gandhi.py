import json

qs = []

qs.append({"q":"The Bolshevik Revolution in Russia, which overthrew the Czarist regime and founded the Soviet Union, occurred on:","o":["November 7, 1917","August 20, 1917","March 1919","April 13, 1919"],"a":0,"e":"The October (Bolshevik) Revolution took place on November 7, 1917 (New Style calendar), under Lenin's leadership, and inspired anti-colonial movements worldwide, including India's."})

qs.append({"q":"Which of the following was an impact of the Russian Revolution on Indian nationalism, as noted in the chapter?","o":["It demonstrated that the masses, if organised and united, could challenge even the mightiest tyrants","It led to an immediate alliance between India and the Soviet Union","It caused the British to grant immediate self-government to India","It had no impact on Indian nationalist thinking"],"a":0,"e":"The Bolshevik Revolution showed that organised mass action could overthrow entrenched autocratic power, inspiring confidence among Indian nationalists in the potential of mass mobilisation."})

qs.append({"q":"Under the Montagu-Chelmsford Reforms (Government of India Act, 1919), 'dyarchy' — the rule of two — was introduced at which level of government?","o":["Provincial government","Central government only","Local government (municipalities) only","Princely states only"],"a":0,"e":"Dyarchy was introduced only at the provincial level, dividing subjects into 'reserved' (administered by the governor and executive councillors) and 'transferred' (administered by ministers responsible to the legislature)."})

qs.append({"q":"Under dyarchy in the provinces, which of the following subjects were classified as 'transferred' subjects, to be administered by ministers responsible to the legislature?","o":["Education, health, local government, agriculture and excise","Law and order, finance, land revenue and irrigation","Defence and foreign affairs","Currency and coinage"],"a":0,"e":"'Transferred' subjects like education, health, local government, agriculture and excise were administered by ministers accountable to the legislature, while 'reserved' subjects (law and order, finance, land revenue, irrigation) remained with the governor's executive council."})

qs.append({"q":"Under the Government of India Act, 1919, in case of failure of constitutional machinery in a province, the governor could:","o":["Take over the administration of transferred subjects as well","Only dissolve the provincial legislature","Refer the matter exclusively to the Secretary of State","Suspend dyarchy nationwide"],"a":0,"e":"The Act allowed the governor to take over administration of transferred subjects too, in case of a breakdown of constitutional machinery in the province — a significant limitation on ministerial responsibility."})

qs.append({"q":"Under the 1919 Act, what proportion of members of the provincial legislative councils were to be elected?","o":["70 per cent","50 per cent","100 per cent","25 per cent"],"a":0,"e":"Provincial legislative councils were expanded with 70 per cent of members to be elected, alongside the introduction of the right to vote for women for the first time."})

qs.append({"q":"At the central level under the Government of India Act, 1919, a bicameral legislature was introduced consisting of:","o":["The Central Legislative Assembly (lower house) and the Council of State (upper house)","The Lok Sabha and Rajya Sabha","The Imperial Council and the Provincial Council","The Legislative Assembly and the Senate"],"a":0,"e":"The 1919 Act introduced a bicameral central legislature — the Central Legislative Assembly as the lower house and the Council of State as the upper house."})

qs.append({"q":"Under the 1919 Act, how many Indians were included in the viceroy's executive council of eight members?","o":["Three","One","Five","None"],"a":0,"e":"Three of the eight members of the viceroy's executive council were to be Indians under the Montagu-Chelmsford reforms."})

qs.append({"q":"What proportion of the central budget remained non-votable by the legislature under the 1919 reforms?","o":["75 per cent","25 per cent","50 per cent","100 per cent"],"a":0,"e":"75 per cent of the central budget remained outside the legislature's voting power, severely limiting real financial control, though members could vote on the remaining portion and ask questions."})

qs.append({"q":"Which of the following is identified as a major drawback of the Montagu-Chelmsford Reforms?","o":["The franchise was extremely limited, covering only about one-and-a-half million people out of a population of roughly 260 million","The reforms granted full responsible government at the centre","Provincial ministers had complete control over finances","There was no division of subjects at all"],"a":0,"e":"The franchise remained extremely narrow — about 1.5 million voters out of India's roughly 260 million population — a key criticism of the reforms' limited democratic scope."})

qs.append({"q":"At the Bombay special session of Congress (August 1918, presided over by Hasan Imam), the Montford Reforms were declared to be:","o":["\"Disappointing\" and \"unsatisfactory\", with demands for effective self-government instead","Fully acceptable as a step towards self-government","A betrayal requiring immediate armed rebellion","Superior to the Morley-Minto Reforms in every respect"],"a":0,"e":"The Congress, at its August 1918 special session under Hasan Imam, rejected the Montford Reforms as disappointing and unsatisfactory, demanding real self-government instead."})

qs.append({"q":"Tilak famously described the Montford Reforms as:","o":["\"A sunless dawn\"","\"A ray of hope\"","\"A fair beginning\"","\"An adequate compromise\""],"a":0,"e":"Tilak dismissed the Montford Reforms as \"unworthy and disappointing—a sunless dawn\"."})

qs.append({"q":"Mohandas Karamchand Gandhi was born on October 2, 1869 in which princely state?","o":["Porbandar, in the princely state of Kathiawar, Gujarat","Rajkot, in Kathiawar","Baroda State","Bhavnagar State"],"a":0,"e":"Gandhi was born in Porbandar, in the princely state of Kathiawar in Gujarat, where his father served as diwan (minister)."})

qs.append({"q":"Gandhi went to South Africa in 1893 in connection with a legal case involving his client:","o":["Dada Abdullah","General Smuts","C.F. Andrews","Herman Kallenbach"],"a":0,"e":"Gandhi travelled to South Africa in connection with a case involving his client Dada Abdullah, initially intending only a brief stay before staying on to organise Indian workers."})

qs.append({"q":"During the moderate phase of his struggle in South Africa (1894-1906), Gandhi set up the Natal Indian Congress and started which newspaper?","o":["Indian Opinion","Young India","Harijan","New India"],"a":0,"e":"Gandhi founded the Natal Indian Congress and started the newspaper Indian Opinion during his moderate phase of activism in South Africa."})

qs.append({"q":"Gandhi's satyagraha technique in South Africa was first employed in 1906 to protest against:","o":["A law making it compulsory for Indians to carry registration certificates with fingerprints","A poll tax on ex-indentured Indians","A ban on Indian migration between provinces","A Supreme Court ruling invalidating non-Christian marriages"],"a":0,"e":"The 1906 satyagraha was launched against a new law requiring Indians to carry fingerprinted registration certificates at all times."})

qs.append({"q":"Which of the following campaigns did Gandhi lead during the passive resistance/satyagraha phase (1906-1914) in South Africa?\n1. Satyagraha against registration certificates.\n2. Campaign against restrictions on Indian migration.\n3. Campaign against poll tax and invalidation of Indian marriages.\n4. Protest against the Transvaal Immigration Act.\nHow many of the above are correctly listed?","o":["All four","Only three","Only two","Only one"],"a":0,"e":"All four campaigns were part of Gandhi's satyagraha phase in South Africa between 1906 and 1914."})

qs.append({"q":"The Supreme Court ruling in South Africa that invalidated all marriages not conducted according to Christian rites had the effect of:","o":["Declaring Hindu, Muslim and Parsi marriages illegal and their children illegitimate, drawing many women into the movement","Legalising all forms of interfaith marriage","Granting Indian women the right to vote","Abolishing the poll tax on Indians"],"a":0,"e":"This ruling delegitimised non-Christian marriages, provoking outrage and drawing many Indian women into the satyagraha movement to defend their honour."})

qs.append({"q":"The Tolstoy Farm, founded in 1910 by Gandhi's associate Herman Kallenbach and named after the Russian writer, served the purpose of:","o":["Housing the families of satyagrahis and providing vocational and manual training alongside education","Training Indian soldiers for the British Indian Army","Serving as a base for revolutionary bomb-making","Functioning purely as a religious ashram with no educational component"],"a":0,"e":"Tolstoy Farm housed satyagrahi families and combined manual labour with education, following Gandhi's philosophy inspired by Tolstoy and Ruskin's Unto This Last."})

qs.append({"q":"Gandhi's earlier settlement in Natal (1904), inspired by John Ruskin's Unto This Last and preceding the Tolstoy Farm, was called:","o":["Phoenix Farm","Sabarmati Ashram","Sevagram","Champaran Ashram"],"a":0,"e":"Phoenix Farm (1904) in Natal was Gandhi's first such settlement, inspired by Ruskin's critique of capitalism in Unto This Last."})

qs.append({"q":"The South African satyagraha campaigns were eventually resolved through negotiations involving Gandhi, Lord Hardinge, C.F. Andrews and:","o":["General Smuts","Winston Churchill","Lord Curzon","Edwin Montagu"],"a":0,"e":"General Smuts, representing the South African government, negotiated the compromise settlement addressing the poll tax, registration certificates, and marriage recognition issues."})

qs.append({"q":"Gandhi returned to India from South Africa in:","o":["January 1915","1919","1906","1898"],"a":0,"e":"Gandhi returned to India in January 1915, after which he toured the country for a year before taking any political position, per the advice of his mentor Gokhale."})

qs.append({"q":"The Champaran Satyagraha of 1917, often called Gandhi's 'first civil disobedience' in India, addressed the grievances of indigo cultivators forced under which system to grow indigo on a fixed portion of their land?","o":["Tinkathia system","Ryotwari system","Mahalwari system","Permanent Settlement"],"a":0,"e":"Under the 'tinkathia' system, European planters forced Champaran's peasants to grow indigo on 3/20th of their land, exploiting them further after synthetic dyes reduced indigo's profitability."})

qs.append({"q":"Gandhi was drawn to the Champaran issue by which local figure who requested he investigate the plight of indigo farmers?","o":["Rajkumar Shukla","Rajendra Prasad","Mazhar-ul-Haq","J.B. Kripalani"],"a":0,"e":"Rajkumar Shukla, a local Champaran farmer, persuaded Gandhi to investigate the indigo cultivators' grievances, leading to the historic Champaran Satyagraha."})

qs.append({"q":"Which of the following leaders joined Gandhi during the Champaran Satyagraha?\n1. Rajendra Prasad\n2. Mazhar-ul-Haq\n3. J.B. Kripalani\n4. Mahadeo Desai\nHow many of the above are correctly listed as associates in the Champaran campaign?","o":["All four","Only three","Only two","Only one"],"a":0,"e":"All four — Rajendra Prasad, Mazhar-ul-Haq, J.B. Kripalani and Mahadeo Desai — are named among those who joined Gandhi at Champaran."})

qs.append({"q":"The Ahmedabad Mill Strike of 1918, Gandhi's first hunger strike in India, arose from a dispute between mill owners and workers over:","o":["Discontinuation of the plague bonus amid wartime inflation","Reduction in working hours","Introduction of new machinery","Refusal to hire women workers"],"a":0,"e":"The dispute centred on mill owners wanting to discontinue the plague bonus while workers demanded higher wages to cope with wartime inflation, doubling the cost of essentials."})

qs.append({"q":"Anusuya Sarabhai, who helped organise the Ahmedabad mill workers and later founded the Ahmedabad Textile Labour Association (1920), was the sister of which mill owner?","o":["Ambalal Sarabhai","Ahmedabad Mill Owners Association's founder","Vallabhbhai Patel","Mahadeo Desai"],"a":0,"e":"Anusuya Sarabhai was the sister of Ambalal Sarabhai, a mill owner and president of the Ahmedabad Mill Owners Association, yet she sided with the workers against her own brother's interests."})

qs.append({"q":"In the Ahmedabad Mill Strike, Gandhi undertook his first fast unto death to:","o":["Strengthen the workers' resolve after negotiations stalled","Protest the Rowlatt Act","Demand the release of Annie Besant","Force the government to hold the Round Table Conference"],"a":0,"e":"Gandhi's first fast was undertaken to bolster the striking workers' morale when wage negotiations with mill owners reached an impasse; it ultimately led to arbitration and a 35 per cent wage hike."})

qs.append({"q":"The Kheda Satyagraha (1918), described as Gandhi's 'first non-cooperation' campaign in India, arose due to:","o":["Crop failure from drought, with peasants demanding revenue remission under the Revenue Code","A tax imposed on indigo cultivation","A wage dispute at textile mills","Restrictions on Indian migration"],"a":0,"e":"Kheda's peasants faced crop failure due to drought in 1918 and demanded revenue suspension as per the Revenue Code, which entitled remission when yields fell below one-fourth normal produce."})

qs.append({"q":"During the Kheda Satyagraha, while Gandhi served as the spiritual head, actual organisational leadership on the ground was provided by:","o":["Sardar Vallabhbhai Patel","Rajendra Prasad","Anusuya Sarabhai","Mazhar-ul-Haq"],"a":0,"e":"Sardar Vallabhbhai Patel, along with Narahari Parikh, Mohanlal Pandya and Ravi Shankar Vyas, provided ground-level leadership during the Kheda tax revolt."})

qs.append({"q":"The Rowlatt Act, passed in March 1919 and officially titled the Anarchical and Revolutionary Crimes Act, was based on recommendations of a committee headed by:","o":["Sir Sidney Rowlatt","Lord William Hunter","Sir Michael O'Dwyer","Lord Chelmsford"],"a":0,"e":"The Rowlatt Committee, headed by British judge Sir Sidney Rowlatt, recommended measures against 'seditious conspiracy' that formed the basis of the Rowlatt Act."})

qs.append({"q":"Which of the following powers did the Rowlatt Act grant to the government?","o":["Arrest without warrant on mere suspicion, trial without jury, and imprisonment without trial","Universal adult franchise for all Indians","Abolition of separate electorates","Full budgetary control for the central legislature"],"a":0,"e":"The Rowlatt Act allowed warrantless arrests on suspicion of 'treason', trials without juries or legal recourse, and effectively suspended habeas corpus protections."})

qs.append({"q":"Which elected Indian members of the Imperial Legislative Council resigned in protest against the passage of the Rowlatt Act?","o":["Mohammed Ali Jinnah, Madan Mohan Malaviya and Mazhar-ul-Haq","Gandhi, Tilak and Annie Besant","Motilal Nehru, C.R. Das and M.R. Jayakar","Surendranath Banerjea and Ananda Mohan Bose"],"a":0,"e":"Jinnah, Malaviya and Mazhar-ul-Haq were among the elected Indian members who resigned from the Imperial Legislative Council in protest against the Rowlatt Act."})

qs.append({"q":"Gandhi described the Rowlatt Act as the:","o":["\"Black Act\"","\"Sunless dawn\"","\"Satanic law\"","\"White-washing bill\""],"a":0,"e":"Gandhi termed the Rowlatt Act the \"Black Act\", organising a Satyagraha Sabha and calling for a nationwide hartal, fasting and civil disobedience in response."})

qs.append({"q":"The Jallianwala Bagh Massacre occurred in Amritsar on:","o":["April 13, 1919 (Baisakhi day)","April 6, 1919","March 1919","April 10, 1919"],"a":0,"e":"The massacre occurred on April 13, 1919, which was also the Baisakhi festival, when Brigadier-General Dyer's troops fired on an unarmed crowd."})

qs.append({"q":"The arrest of which two nationalist leaders in Amritsar on April 9, 1919 (without provocation beyond addressing protest meetings) triggered the unrest leading up to the Jallianwala Bagh massacre?","o":["Saifuddin Kitchlew and Dr Satyapal","Motilal Nehru and C.R. Das","Madan Mohan Malaviya and Mazhar-ul-Haq","Rajendra Prasad and Mazhar-ul-Haq"],"a":0,"e":"The arrest of Saifuddin Kitchlew and Dr Satyapal on April 9, 1919 sparked protests that culminated in the Jallianwala Bagh tragedy days later."})

qs.append({"q":"Brigadier-General Reginald Dyer, responsible for the Jallianwala Bagh firing, had earlier on April 13 issued a proclamation:","o":["Forbidding people from leaving the city without a pass or assembling in groups of more than three","Declaring a public holiday for Baisakhi","Ordering the release of all political prisoners","Announcing a curfew only after sunset"],"a":0,"e":"Dyer's April 13 proclamation banned unauthorised assembly and movement without a pass, though many at Jallianwala Bagh, especially villagers, were unaware of it."})

qs.append({"q":"According to official British Indian sources, how many people were identified as dead in the Jallianwala Bagh Massacre, while the Indian National Congress estimated a higher figure?","o":["379 officially identified dead; the Congress estimated approximately 1,000 killed","100 officially identified dead; Congress estimated 500 killed","1,650 officially identified dead, matching the number of bullets fired","No official figure was ever released"],"a":0,"e":"Official sources listed 379 dead and about 1,100 wounded, while the Congress estimated close to 1,000 killed and over 1,500 injured; notably, 1,650 bullets were fired into the unarmed crowd."})

qs.append({"q":"In protest against the Jallianwala Bagh Massacre, which two prominent Indians renounced honours bestowed on them by the British?","o":["Rabindranath Tagore (knighthood) and Gandhi (Kaiser-i-Hind title)","Motilal Nehru (title) and C.R. Das (title)","Jinnah (knighthood) and Malaviya (title)","Sir S. Subramaniya Aiyar (knighthood, in 1919) and Annie Besant (title)"],"a":0,"e":"Rabindranath Tagore renounced his knighthood, and Gandhi gave up his Kaiser-i-Hind title (awarded for his Boer War service), both in protest against the massacre."})

qs.append({"q":"Which historian is quoted in the chapter describing the Jallianwala Bagh Massacre as \"the decisive moment when Indians were alienated from British rule\"?","o":["A.J.P. Taylor","R.C. Majumdar","Bipan Chandra","Percival Spear"],"a":0,"e":"Historian A.J.P. Taylor described Jallianwala Bagh as the decisive turning point alienating Indians from British rule."})

qs.append({"q":"Udham Singh, who later assassinated Michael O'Dwyer (the Lieutenant-Governor responsible for the 1919 Punjab repression) in London, adopted which symbolic name reflecting Hindu-Muslim-Sikh unity?","o":["Ram Mohammad Singh Azad","Bhagat Singh Azad","Sardar Kartar Singh","Baba Gurdit Singh"],"a":0,"e":"Udham Singh took the name Ram Mohammad Singh Azad, symbolising unity across religious communities, before assassinating O'Dwyer in 1940 and being hanged the same year."})

qs.append({"q":"The Hunter Committee (Disorders Inquiry Committee), formed to investigate the Jallianwala Bagh Massacre and announced on October 14, 1919, was chaired by:","o":["Lord William Hunter","Sir Sidney Rowlatt","Sir Michael O'Dwyer","Edwin Montagu"],"a":0,"e":"Lord William Hunter, former Solicitor-General for Scotland, chaired the Disorders Inquiry Committee, widely known as the Hunter Committee."})

qs.append({"q":"Which of the following Indians served on the Hunter Committee?","o":["Sir Chimanlal Harilal Setalvad, Pandit Jagat Narayan and Sardar Sahibzada Sultan Ahmad Khan","Motilal Nehru, C.R. Das and M.R. Jayakar","Jinnah, Malaviya and Mazhar-ul-Haq","Rajendra Prasad, Mazhar-ul-Haq and J.B. Kripalani"],"a":0,"e":"Sir Chimanlal Harilal Setalvad, Pandit Jagat Narayan and Sardar Sahibzada Sultan Ahmad Khan were the three Indian members of the Hunter Committee."})

qs.append({"q":"When questioned by the Hunter Committee, Dyer justified his firing at Jallianwala Bagh by stating that his intention was to:","o":["Strike terror throughout the Punjab and produce a 'moral effect' to reduce the rebels' stature","Disperse the crowd with minimum casualties","Follow direct orders from the Viceroy","Protect European civilians under immediate physical threat"],"a":0,"e":"Dyer admitted before the committee that he intended to create a strong 'moral effect' and strike terror across Punjab, a justification the committee ultimately condemned."})

qs.append({"q":"Before the Hunter Committee began its proceedings, the government passed which legislation, criticised by Motilal Nehru as a 'white-washing bill', to protect its officers from prosecution?","o":["Indemnity Act","Rowlatt Act","Government of India Act, 1919","Defence of India Act, 1915"],"a":0,"e":"The Indemnity Act, passed before the Hunter Committee's proceedings, protected British officials from prosecution for actions during the 1919 disturbances, earning the label 'white-washing bill'."})

qs.append({"q":"In the British Parliament, which Secretary of State for War reviewed the Hunter Committee's report and condemned the Jallianwala Bagh Massacre as \"monstrous\"?","o":["Winston Churchill","Edwin Montagu","Lord Chelmsford","H.H. Asquith"],"a":0,"e":"Winston Churchill, then Secretary of State for War, condemned the massacre as \"monstrous\" in the House of Commons, despite his general reputation as no friend of Indian nationalism."})

qs.append({"q":"Following the Hunter Committee's findings, what disciplinary action was ultimately taken against General Dyer?","o":["He was relieved of his command and recalled to England, but faced no legal action and retained his pension","He was court-martialled and imprisoned","He was stripped of his pension and exiled","He was honoured with a promotion for maintaining order"],"a":0,"e":"Dyer was relieved of his command and recalled to England but faced no legal prosecution, retaining half pay and his army pension — a lenient outcome that outraged Indian opinion."})

qs.append({"q":"Despite official censure, Dyer received significant sympathy in Britain, including a fund of 26,000 pounds raised by which newspaper, to which Rudyard Kipling contributed?","o":["The Morning Post","The Times","The Manchester Guardian","The Daily Telegraph"],"a":0,"e":"The Morning Post raised a substantial fund for Dyer, with contributors including Rudyard Kipling, reflecting divided British opinion on the massacre."})

qs.append({"q":"The honouring of General Dyer as an honorary Sikh by the clergy of the Golden Temple (led by Arur Singh) contributed to the intensification of which subsequent movement?","o":["The Gurudwara Reform Movement (Akali Movement)","The Non-Cooperation Movement","The Khilafat Movement","The Home Rule Movement"],"a":0,"e":"The controversial honouring of Dyer by Golden Temple priests fuelled demands for reforming gurudwara management, contributing to the Gurudwara Reform (Akali) Movement."})

for q in qs:
    assert len(q["o"]) == 4, q["q"]
    assert 0 <= q["a"] <= 3
    assert len(set(q["o"])) == 4, q["q"]

print(f"Total questions: {len(qs)}")

out = {
    "id": "hist_upsc_emergence_gandhi",
    "title": "Emergence of Gandhi",
    "desc": "Post-WWI nationalist resurgence, the Montagu-Chelmsford Reforms and Government of India Act 1919, Gandhi's South African career and satyagraha technique, Champaran/Ahmedabad/Kheda, the Rowlatt Act, and the Jallianwala Bagh Massacre",
    "questions": qs
}

with open("/sessions/vigilant-wonderful-volta/mnt/outputs/hist_upsc_ch15_emergence_gandhi.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Saved.")

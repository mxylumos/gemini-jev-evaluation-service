# Jev Playground requests

This 26-case benchmark has 13 news-topic classifications and 13 passage-grounded BoolQ decisions. In Jev Playground's separate fields, paste each `State` object into **State** and the complete named map shown as `Question` into **Question**.

Expected answers are for checking after each run only; do not paste them into Jev.

## News topic classification (AG News)

### 1. `ag-news-train-29994`

Expected: `"world"`

State:

```json
{
  "text": "Afghan President Escapes Attack Afghanistan President Hamid Karzai was forced to cancel a trip to a provincial capital after a rocket hit near the landing site for his helicopter."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 2. `ag-news-train-29998`

Expected: `"world"`

State:

```json
{
  "text": "Bush, Kerry on Issue of National Security (AP) AP - Three times a week, The Associated Press picks an issue and asks Republican President Bush and Democratic presidential candidate John Kerry a question about it. Today's question and responses:"
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 3. `ag-news-train-29992`

Expected: `"sports"`

State:

```json
{
  "text": "Another day without practice for Phil BLOOMFIELD HILLS, Mich. -- Phil Mickelson skipped a practice for the second straight day on Thursday, 24 hours before the Ryder Cup gets under way at Oakland Hills."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 4. `ag-news-train-29993`

Expected: `"sports"`

State:

```json
{
  "text": "Hughes delighted with Blackburn Rovers Football Club The former Rovers striker has signed a two-year contract at Ewood Park, with the option to extend the deal by twelve months should both parties agree."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 5. `ag-news-train-29997`

Expected: `"business"`

State:

```json
{
  "text": "United Airlines CEO Sees Significant Job Losses BRUSSELS (Reuters) - The head of United Airlines parent UAL Corp. said on Thursday the airline's restructuring plan would lead to a significant number of job losses, but it was not yet clear how many."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 6. `ag-news-train-29990`

Expected: `"sci_tech"`

State:

```json
{
  "text": "Smithsonian To Add $60-Million Ocean Hall The Smithsonian's National Museum of Natural History announced plans to create a 28,000-square-foot Ocean Hall as part of a new Smithsonian Ocean Science Initiative."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 7. `ag-news-train-30003`

Expected: `"sci_tech"`

State:

```json
{
  "text": "Vodafone Peddles New BlackBerry Research In Motion's BlackBerry 7100v, which sports the company's latest keyboard technology, is being offered exclusively through Vodafone."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

## Passage-grounded yes/no (BoolQ)

### 8. `boolq-train-00000`

Expected: `true`

State:

```json
{
  "passage": "Persian (/ˈpɜːrʒən, -ʃən/), also known by its endonym Farsi (فارسی fārsi (fɒːɾˈsiː) ( listen)), is one of the Western Iranian languages within the Indo-Iranian branch of the Indo-European language family. It is primarily spoken in Iran, Afghanistan (officially known as Dari since 1958), and Tajikistan (officially known as Tajiki since the Soviet era), and some other regions which historically were Persianate societies and considered part of Greater Iran. It is written in the Persian alphabet, a modified variant of the Arabic script, which itself evolved from the Aramaic alphabet.",
  "question": "do iran and afghanistan speak the same language"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 9. `boolq-train-00004`

Expected: `false`

State:

```json
{
  "passage": "As with other games in The Elder Scrolls series, the game is set on the continent of Tamriel. The events of the game occur a millennium before those of The Elder Scrolls V: Skyrim and around 800 years before The Elder Scrolls III: Morrowind and The Elder Scrolls IV: Oblivion. It has a broadly similar structure to Skyrim, with two separate conflicts progressing at the same time, one with the fate of the world in the balance, and one where the prize is supreme power on Tamriel. In The Elder Scrolls Online, the first struggle is against the Daedric Prince Molag Bal, who is attempting to meld the plane of Mundus with his realm of Coldharbour, and the second is to capture the vacant imperial throne, contested by three alliances of the mortal races. The player character has been sacrificed to Molag Bal, and Molag Bal has stolen their soul, the recovery of which is the primary game objective.",
  "question": "is elder scrolls online the same as skyrim"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 10. `boolq-train-00009`

Expected: `true`

State:

```json
{
  "passage": "With the box office success of Batman Forever in June 1995, Warner Bros. immediately commissioned a sequel. They hired director Joel Schumacher and writer Akiva Goldsman to reprise their duties the following August, and decided it was best to fast track production for a June 1997 target release date, which is a break from the usual 3-year gap between films. Schumacher wanted to homage both the broad camp style of the 1960s television series and the work of Dick Sprang. The storyline of Batman & Robin was conceived by Schumacher and Goldsman during pre-production on A Time to Kill. Portions of Mr. Freeze's back-story were based on the Batman: The Animated Series episode ``Heart of Ice'', written by Paul Dini.",
  "question": "is batman and robin a sequel to batman forever"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 11. `boolq-train-00010`

Expected: `false`

State:

```json
{
  "passage": "Badgers are short-legged omnivores in the family Mustelidae, which also includes the otters, polecats, weasels, and wolverines. They belong to the caniform suborder of carnivoran mammals. The 11 species of badgers are grouped in three subfamilies: Melinae (Eurasian badgers), Mellivorinae (the honey badger or ratel), and Taxideinae (the American badger). The Asiatic stink badgers of the genus Mydaus were formerly included within Melinae (and thus Mustelidae), but recent genetic evidence indicates these are actually members of the skunk family, placing them in the taxonomic family Mephitidae.",
  "question": "is a wolverine the same as a badger"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 12. `boolq-train-00013`

Expected: `true`

State:

```json
{
  "passage": "Calcium carbide is a chemical compound with the chemical formula of CaC. Its main use industrially is in the production of acetylene and calcium cyanamide.",
  "question": "calcium carbide cac2 is the raw material for the production of acetylene"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 13. `boolq-train-00015`

Expected: `false`

State:

```json
{
  "passage": "A shoot-out is usually considered for statistical purposes to be separate from the match which preceded it. In the case of a two-legged fixture, the two matches are still considered either as two draws or as one win and one loss; in the case of a single match, it is still considered as a draw. This contrasts with a fixture won in extra time, where the score at the end of normal time is superseded. Converted shoot-out penalties are not considered as goals scored by a player for the purposes of their individual records, or for ``golden boot'' competitions.",
  "question": "does a penalty shoot out goal count towards the golden boot"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

## News topic classification (AG News)

### 14. `ag-news-train-00003`

Expected: `"business"`

State:

```json
{
  "text": "Iraq Halts Oil Exports from Main Southern Pipeline (Reuters) Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 15. `ag-news-train-00030`

Expected: `"business"`

State:

```json
{
  "text": "Japan nuclear firm shuts plants The company running the Japanese nuclear plant hit by a fatal accident is to close its reactors for safety checks."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 16. `ag-news-train-00038`

Expected: `"business"`

State:

```json
{
  "text": "Researchers seek to untangle the e-mail thread E-mail is a victim of its own success. That's the conclusion of IBM Corp. researchers in Cambridge, who have spent nearly a decade conducting field tests at IBM and other companies about how employees work and use electronic mail. It's clear to them that e-mail has become the Internet's killer application."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 17. `ag-news-train-00078`

Expected: `"sci_tech"`

State:

```json
{
  "text": "'Madden,' 'ESPN' Football Score in Different Ways (Reuters) Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because \"Madden NFL 2005\" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 18. `ag-news-train-00090`

Expected: `"sci_tech"`

State:

```json
{
  "text": "Science, Politics Collide in Election Year (AP) AP - With more than 4,000 scientists, including 48 Nobel Prize winners, having signed a statement opposing the Bush administration's use of scientific advice, this election year is seeing a new development in the uneasy relationship between science and politics."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

## Passage-grounded yes/no (BoolQ)

### 19. `boolq-train-00006`

Expected: `false`

State:

```json
{
  "passage": "The series premiered in the United States on Starz on 12 April 2013, and its second season premiered on 22 March 2014. The series was renewed for a third season, which premiered on 24 October 2015. On 23 July 2015, Starz announced that the third season would be the show's last. However Goyer has left it open for a miniseries return.",
  "question": "will there be a season 4 of da vinci's demons"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 20. `boolq-train-00012`

Expected: `false`

State:

```json
{
  "passage": "The United States should have the chance to observe and assess the functioning of the court, over time, before choosing to become subject to its jurisdiction. Given these concerns, I will not, and do not recommend that my successor, submit the treaty to the Senate for advice and consent until our fundamental concerns are satisfied.",
  "question": "does the icc has jurisdiction in the united states"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 21. `boolq-train-00023`

Expected: `false`

State:

```json
{
  "passage": "Both Jersey and Bank of England notes are legal tender in Jersey and circulate together, alongside the Guernsey pound and Scottish banknotes. The Jersey notes are not legal tender in the United Kingdom but are legal currency, so creditors and traders may accept them if they so choose.",
  "question": "is jersey currency legal tender in the uk"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 22. `boolq-train-00031`

Expected: `true`

State:

```json
{
  "passage": "The premise of the series is that Buffy is the latest Slayer, a young woman endowed by mystical forces with superhuman powers to fight and defeat vampires, demons, and other evil forces in the fictional town of Sunnydale. Like every Slayer before her, she was chosen and informed of her destiny when she was 15 years old. Her mother is unaware of her daughter's powers and responsibilities until Buffy is forced to tell her at the end of the second season of the television series. Although Joyce is shocked at this revelation, she recovers quickly and remains a source of stability for Buffy and Buffy's small circle of friends who assist her, dubbed the Scooby Gang. Eventually Joyce is able to take Buffy's dangerous demon-fighting in stride and even become proud and respectful of her daughter's abilities. Her natural death from an illness in the fifth season forces Buffy to face becoming an adult.",
  "question": "does buffy's mom know she's a slayer"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 23. `boolq-train-00036`

Expected: `true`

State:

```json
{
  "passage": "A bundle branch block can be diagnosed when the duration of the QRS complex on the ECG exceeds 120 ms. A right bundle branch block typically causes prolongation of the last part of the QRS complex, and may shift the heart's electrical axis slightly to the right. The ECG will show a terminal R wave in lead V1 and a slurred S wave in lead I. Left bundle branch block widens the entire QRS, and in most cases shifts the heart's electrical axis to the left. The ECG will show a QS or rS complex in lead V1 and a monophasic R wave in lead I. Another normal finding with bundle branch block is appropriate T wave discordance. In other words, the T wave will be deflected opposite the terminal deflection of the QRS complex. Bundle branch block, especially left bundle branch block, can lead to cardiac dyssynchrony. The simultaneous occurrence of left and right bundle branch block leads to total AV block.",
  "question": "can you have a right and left bundle branch block"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```

### 24. `boolq-train-00037`

Expected: `false`

State:

```json
{
  "passage": "In informal games, it is customary to announce ``check'' when making a move that puts the opponent's king in check. In formal competitions, however, check is rarely announced.",
  "question": "do you always have to say check in chess"
}
```

### 25. `ag-news-train-00073`

Expected: `"business"`

State:

```json
{
  "text": "Dutch Firm Beats Apple to Punch A music retailer from the Netherlands beats Apple by launching a download service in Europe's latest market battleground. Also: Movie industry wrests agreement from defunct company.... Microsoft challenges Photoshop   hellip;. and more."
}
```

Question:

```json
{
  "topic": {
    "type": "choice",
    "instructions": "Which news topic best classifies this article?",
    "criteria": {
      "world": "International affairs, politics, diplomacy, conflict, or major world events.",
      "sports": "Sports competitions, athletes, teams, or sporting organizations.",
      "business": "Companies, markets, finance, jobs, trade, or the economy.",
      "sci_tech": "Technology, science, software, devices, research, or space."
    }
  }
}
```

### 26. `boolq-train-00029`

Expected: `false`

State:

```json
{
  "passage": "Saline, also known as saline solution, is a mixture of sodium chloride in water and has a number of uses in medicine. Applied to the affected area it is used to clean wounds, help remove contact lenses, and help with dry eyes. By injection into a vein it is used to treat dehydration such as from gastroenteritis and diabetic ketoacidosis. It is also used to dilute other medications to be given by injection.",
  "question": "is saline and sodium chloride the same thing"
}
```

Question:

```json
{
  "answer": {
    "type": "noul",
    "instructions": "Using only the passage, is the answer to the question yes?",
    "criteria": {
      "true": "The answer to the supplied question is yes, based only on the supplied passage.",
      "false": "The answer is no, based only on the supplied passage."
    }
  }
}
```


from Rule import Rule


# Define the grammar as a list of Rule objects
grammar = [


    Rule('S', ['Adv', 'VP']),
    Rule('S', ['NP', 'VP']),
    Rule('S', ['Pron', 'VP']),
    Rule('S', ['Noun', 'VP']),
    Rule('S', ['X1', 'NP']),
    Rule('S', ['VP', 'Q1']),
    Rule('S', ['X2', 'Noun']),

    Rule('NP', ['Adj', 'Noun']),
    Rule('NP', ['Adj', 'NP']),
    Rule('NP', ['X3', 'Noun']),
    Rule('NP', ['Noun', 'Noun']),
    Rule('NP', ['NP', 'Particle']),
    Rule('NP', ['NP', 'Noun']),
    Rule('NP', ['AdjP', 'Noun']),

    Rule('VP', ['Noun', 'Verb']),
    Rule('VP', ['NP', 'Verb']),
    Rule('VP', ['Adv', 'VP']),
    Rule('VP', ['Adv', 'Verb']),
    Rule('VP', ['NP', 'VP']),
    Rule('VP', ['Q2', 'Verb']),
    Rule('VP', ['AdvP', 'VP']),

    Rule('AdjP', ['Adv', 'Adj']),

    Rule('AdvP', ['Adv', 'Adj']),
    Rule('AdvP', ['Adj', 'Noun']),

    Rule('Q1', ['mısınız']),
    Rule('Q2', ['ne zaman']),
    Rule('X1', ['NP', 'Adv']),
    Rule('X2', ['Noun', 'X1']),
    Rule('X3', ['Noun', 'Conj']),

    

    Rule('Noun', ['hediye', 'romanları', 'akşam', 'yemeği', 'destanlar', 'kültürümüzü', 'tarihimizi', 
                    'yaz', 'meyvelerinden', 'karpuz', 'meyvedir', 'akşamki', 'toplantıya', 'ağacın', 'altında',
                    'gece', 'mehtabı', 'okul', 'köye', 'uzaktaydı', 'sesle', 'müzik']),
    Rule('Adv', ['dün', 'arkadaşıma', 'keyifle', 'anneme', 'bence', 'en', 'buraya', 'epeyce']),
    Rule('Adj', ['bir', 'tarihi', 'milli', 'güzel', 'bu', 'her', 'son', 'bizim', 'yüksek']),
    Rule('Verb', ['aldım', 'okuyorum', 'yardım ettim', 'anlatır', 'katılacak', 'izlerdik', 'geldiniz', 'dinleme']),
    Rule('Pron', ['ben', 'siz']),
    Rule('Particle', ['için']), 
    Rule('Conj', ['ve'])


   
]
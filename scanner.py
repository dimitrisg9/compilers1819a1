"""
Ο στόχος της άσκησης είναι να κατασκευάσουμε σε απλή Python3 (χωρίς τη βοήθεια έτοιμων
βιβλιοθηκών/εργαλείων, δηλαδή, χωρίς τη χρήση κανονικών εκφράσεων!) λεκτικό αναλυτή, ο
οποίος θα αναγνωρίζει έγκυρες ενδείξεις ανέμου σύμφωνα με τα πρότυπα αναφορών
μετεωρολογικών παρατηρήσεων/προγνώσεων METAR/TAF
"""


def getchar(text, pos):
    """ returns char category at position `pos` of `text`,
    or None if out of bounds """

    if pos < 0 or pos >= len(text): return None

    c = text[pos]

    # **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις

    #if c >= '0' and c <= '9': return 'DIGIT'  # 0..9 grouped together

    #if c == '.': return 'DOT'  # dot as a category by itself

    return c  # anything else


def scan(text, transitions, accepts):
    """ scans `text` while transitions exist in
    'transitions'. After that, if in a state belonging to
    `accepts`, it returns the corresponding token, else ERROR_TOKEN.
    """

    # initial state
    pos = 0
    state = 's0'
    # memory for last seen accepting states
    last_token = None
    last_pos = None

    while True:

        c = getchar(text, pos)  # get next char (category)

        if state in transitions and c in transitions[state]:
            state = transitions[state][c]  # set new state
            pos += 1  # advance to next char

            # remember if current state is accepting
            if state in accepts:
                last_token = accepts[state]
                last_pos = pos

        else:  # no transition found

            if last_token is not None:  # if an accepting state already met
                return last_token, last_pos

            # else, no accepting state met yet
            return 'ERROR_TOKEN', pos


# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = {'s0': {'0': 's1', '1': 's1', '2': 's1', '3': 's3'},
               's1': {'0': 's2', '1': 's2', '2': 's2', '3': 's2', '4': 's2', '5': 's2', '6': 's2', '7': 's2', '8': 's2', '9': 's2'},
               's2': {'0': 's6', '1': 's6', '2': 's6', '3': 's6', '4': 's6', '5': 's6', '6': 's6', '7': 's6', '8': 's6', '9': 's6'},
               's3': {'5': 's4', '0': 's5', '1': 's5', '2': 's5', '3': 's5', '4': 's5'},
               's4': {'0': 's6'},
               's5': {'0': 's6', '1': 's6', '2': 's6', '3': 's6', '4': 's6', '5': 's6', '6': 's6', '7': 's6', '8': 's6', '9': 's6'},
               's6': {'0': 's7', '1': 's7', '2': 's7', '3': 's7', '4': 's7', '5': 's7', '6': 's7', '7': 's7', '8': 's7', '9': 's7'},
               's7': {'0': 's8', '1': 's8', '2': 's8', '3': 's8', '4': 's8', '5': 's8', '6': 's8', '7': 's8', '8': 's8', '9': 's8'},
               's8': {'K': 's9', 'M': 's10', 'G': 's11'},
               's9': {'T': 's15'},
               's10': {'P': 's12'},
               's11': {'0': 's13', '1': 's13', '2': 's13', '3': 's13', '4': 's13', '5': 's13', '6': 's13', '7': 's13', '8': 's13', '9': 's13'},
               's12': {'S': 's15'},
               's13': {'0': 's14', '1': 's14', '2': 's14', '3': 's14', '4': 's14', '5': 's14', '6': 's14', '7': 's14', '8': 's14', '9': 's14'},
               's14': {'K': 's16', 'M': 's17'},
               's16': {'T': 's19'},
               's17': {'P': 's18'},
               's18': {'S': 's19'}
               }

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = {'s19': 'WIND_TOKEN',
           's15': 'WIND_TOKEN'
           }

# get a string from input
text = input('give some input>')

# scan text until no more input
while text:  # i.e. len(text)>0
    # get next token and position after last char recognized
    token, pos = scan(text, transitions, accepts)
    if token == 'ERROR_TOKEN':
        print('ERROR_TOKEN','of', text)
        break
    print("token:", token, "text:", text[:pos])
    # new text for next scan
    text = text[pos:]

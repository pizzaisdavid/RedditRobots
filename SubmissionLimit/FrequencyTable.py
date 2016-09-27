
def buildUserSubmissionFrequencyTable(submissions):
    table = {}
    for s in submissions:
        username = s.author.name
        if username not in table:
            table[username] = []
        table[username].append(s)
    return table;
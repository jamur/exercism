OBJECTS = ['house that Jack built', 'malt', 'rat', 'cat', 'dog',
    'cow with the crumpled horn', 'maiden all forlorn', 'man all tattered and torn',
    'priest all shaven and shorn', 'rooster that crowed in the morn',
    'farmer sowing his corn', 'horse and the hound and the horn']

VERBS = ['lay in', 'ate', 'killed', 'worried', 'tossed', 'milked', 'kissed',
         'married', 'woke', 'kept', 'belonged to']

def recite(start_verse, end_verse):
    return [verse(number) for number in range(start_verse, end_verse + 1)]

def verse(number):
    return 'This is the ' + OBJECTS[number % 12 - 1] + verse_seq(number - 2) + '.'

def verse_seq(number):
    if number < 0:
        return ''
    seq = ' that ' + VERBS[number] + ' the ' + OBJECTS[number]
    return seq + verse_seq(number - 1)

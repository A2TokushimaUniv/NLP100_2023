import random
from logging import getLogger
logger = getLogger(__name__)
def test_Typoglycemia():
    text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    fragments = text.split(' ')

    new_fragments = []
    for fragment in fragments:
        if len(fragment) < 4:
            new_fragments.append(fragment)
            continue

        middle_text = list(fragment[1:-1])
        random.shuffle(middle_text)
        new_fragments.append(fragment[0]+''.join(middle_text)+fragment[-1])

    result = " ".join(new_fragments)
    logger.info(result)
    assert len(result) == len(text) and result != text

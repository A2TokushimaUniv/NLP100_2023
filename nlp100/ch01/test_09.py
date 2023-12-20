import random
import re
from logging import getLogger

logger = getLogger(__name__)


def test_Typoglycemia():
    text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    fragments = text.split(" ")

    new_fragments = []
    for fragment in fragments:
        if len(fragment) < 4:
            new_fragments.append(fragment)
            continue

        middle_text = list(fragment[1:-1])
        random.shuffle(middle_text)
        new_fragments.append(fragment[0] + "".join(middle_text) + fragment[-1])

    result = " ".join(new_fragments)
    logger.info(result)

    pattern = r"I c\S+t b\S+e t\S+t I c\S+d a\S+y u\S+d w\S+t I was r\S+g : the p\S+l p\S+r of the h\S+n m\S+d ."  # \Sは空白以外の文字 \S+で空白以外の文字の１回以上の繰り返し
    is_match = re.match(pattern, text) is not None  # 問題条件に沿って改変されているかをテストする
    is_diff = result != text
    same_length = len(result) == len(text)
    assert same_length and is_diff and is_match

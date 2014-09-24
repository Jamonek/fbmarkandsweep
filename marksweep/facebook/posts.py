"""
This module implements the post parsing behavoirs of Mark Sweep.

devel-notes :
    config and utils need to be implemented,
    config should have a __init__ that imports everything

Author: Jason Liu
"""
from config import (SPAM_THRESHOLD,
                    SPAM_RESPONSE,
                    MAYBE_SPAM_RESPONSE,
                    NOT_SPAM_RESPONSE,
                    OFFTOPIC_REPONSE,
                    ONTOPIC_REPONSE)

from utils import (get_classifier_by_gid,
                   new_post)


def parse(fb):
    """
    Consumes a facebook entity and return features used to make a action
    """
    clf = get_classifier_by_gid(fb.gid)

    if new_post(fb):
        spam, ontopic, short, hateful = clf.process(fb)
        return (spam, ontopic, short, hateful)


def act(fb, spam, ontopic, short, hateful):
    """
    Consumes a facebook entity and response features to determine best course
    of action
    """
    if spam > SPAM_THRESHOLD:
        fb.comment(SPAM_RESPONSE)
    else:
        if not ontopic:
            fb.comment(ONTOPIC_REPONSE)
        elif spam > 80:
            fb.comment(MAYBE_SPAM_RESPONSE)
        else:
            fb.comment(OFFTOPIC_REPONSE)
    pass

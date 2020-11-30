"""
Functions to clean up text data
"""
import re


def rep_linebrk(x):
    """
    Quick function to remove linebreak character.
    Args:
        x: row in the DataFrame to clean
    Returns:
        String with no linebreaks
    """
    try:
        new_str = re.sub("\\n", " ", x)
    except:
        new_str = x
    return new_str


def rep_tic(x):
    """
    Quick function to make ticks uniform.
    Args:
        x: row in the DataFrame to clean
    Returns:
        String with new ticks
    """
    try:
        new_str = re.sub("´", "'", x)
        new_str = re.sub("’", "'", x)
    except:
        new_str = x
    return new_str


def display_topics(model, feature_names, no_top_words, topic_names=None):
    """
    Helps display topics from a given NMF model

    Args:
        model: NMF model being discovered
        feature_names: Terms/tokens being used
            - can use _.get_feature_names() to help
        no_top_words: Number of topics being discovered
        topic_names: Optional to name each topic

    Returns:
        Prints the topics with the corresponding terms/tokens
    """
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '", topic_names[ix], "'")
        print(
            ", ".join(
                [
                    feature_names[i]
                    for i in topic.argsort()[: -no_top_words - 1 : -1]
                ]
            )
        )

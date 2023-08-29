from gensim.summarization import summarize

def get_summary(text):
    """
    Function to summarize a given text.

    :param text: Text to summarize.
    :return: Summarized text.
    """
    summary = summarize(text)
    return summary

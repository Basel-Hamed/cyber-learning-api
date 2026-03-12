def format_answer(text, mode):

    if mode == "short":

        return text[:400]

    elif mode == "full":

        return text

    else:

        return text

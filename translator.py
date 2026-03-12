from googletrans import Translator

translator = Translator()


def translate_bn(text, style):

    try:

        result = translator.translate(text, dest="bn").text

        if style == "sadhu":

            result = result.replace("করে", "করিয়া")
            result = result.replace("হয়", "হইয়াছে")

        return result

    except:

        return "বাংলা অনুবাদ করা যায়নি"

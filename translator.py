from deep_translator import GoogleTranslator

def translate_bn(text, style):
    """
    Translate text to Bangla using deep-translator.
    style: 'colloquial' or 'sadhu'
    """
    try:
        result = GoogleTranslator(source='auto', target='bn').translate(text)
        if style == "sadhu":
            # Optional minor modifications for sadhu style
            result = result.replace("করে", "করিয়া")
            result = result.replace("হয়", "হইয়াছে")
        return result
    except:
        return "বাংলা অনুবাদ করা যায়নি"

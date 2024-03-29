# Chomsky Hierarchy Type 1, natural language, context-sensitive.
# Neural networks are used for parsing.
from typing import List, Union

import spacy
import spacy.tokens.doc
import spacy.tokens.span

# For Language detection
import pycountry
from spacy.language import Language
from spacy_langdetect import LanguageDetector

# Easy to use API for getting things done, not meant for research
# The _sm datasets are meant for efficiency, there are others optimized
# for accuracy.
nlp = spacy.load("en_core_web_sm")
nlp("The quick brown fox jumps over the lazy dog")

nlp_es = spacy.load("es_core_news_sm")
nlp_es("Hasta mañana, Alberto")

# Add LanguageDetector and assign it a string name
@Language.factory("language_detector")
def create_language_detector(nlp, name):
    return LanguageDetector(language_detection_function=None)


# For recognizing sentence boundaries
nlp_multi = spacy.load("xx_sent_ud_sm")

# Should be the last pipeline
nlp_multi.add_pipe("language_detector")

samples = [
    "Hola, comó estas?",
    "The quick brown fox jumps over the lazy dog",
    "как ваши дела",
]

DEFAULT_WIDTH = 11


def format_strings(strings: List[str], width: int = DEFAULT_WIDTH) -> str:
    return " ".join(f"{str(column):<{width}}" for column in strings)


def print_langdetection(
    doc_or_span: Union[spacy.tokens.doc.Doc, spacy.tokens.span.Span]
) -> None:
    try:
        # Comes from the spacy-langdetect library
        language_info = doc_or_span._.language

        lang = language_info["language"]
        lang_info = pycountry.languages.get(alpha_2=lang)
        if lang_info is None:
            lang_name = "Unknown"
        else:
            lang_name = lang_info.name
        score = language_info["score"] * 100
        print(f"{lang_name} ({lang}) text. Certainty: {score:.3f}%")
    except AttributeError:
        # No language detection
        pass
    except KeyError:
        # Unknown dict keys
        pass


def print_info(
    doc_or_span: Union[spacy.tokens.doc.Doc, spacy.tokens.span.Span]
) -> None:
    print_langdetection(doc_or_span)
    print(
        format_strings(
            [
                "token",
                "position",
                "is title",
                "is start",
                "head",
                "morphology info",
            ]
        )
    )
    print(format_strings(["-" * (3 * DEFAULT_WIDTH // 4) for _ in range(6)]))
    for word in doc_or_span:
        print(
            format_strings(
                [
                    word.text,
                    word.pos_,
                    word.is_title,
                    word.is_sent_start,
                    word.head,
                    word.morph,
                ]
            )
        )


def print_doc_info(doc: spacy.tokens.doc.Doc, whole=False) -> None:
    if whole:
        print_info(doc)
        return
    for sent in doc.sents:
        print_info(sent)
        print()

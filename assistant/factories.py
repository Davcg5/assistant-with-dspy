from assistant.modules.assistant import Assistant
from assistant.modules.context_extractor import ContextExtractor
from assistant.modules.terms_finder import TermsFinder
from assistant.retrievers.chroma_db_retriever import ChromaDBRetriever
from assistant.retrievers.llama_index_retriever import LlamaIndexRetriever


def get_lli_assistant():
    context_extractor = ContextExtractor(retriever=LlamaIndexRetriever())
    context_extractor.retriever.populate('./documents')

    assistant = Assistant(
        terms_finder=TermsFinder,
        context_extractor=context_extractor,
    )
    return assistant


def get_chromadb_assistant():
    context_extractor = ContextExtractor(retriever=ChromaDBRetriever())

    context_extractor.retriever.populate('./documents/rules.txt')

    assistant = Assistant(
        terms_finder=TermsFinder,
        context_extractor=context_extractor,
    )
    return assistant

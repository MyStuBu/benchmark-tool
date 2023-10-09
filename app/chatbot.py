from app.components.embeddings.abstract.embeddings import Embeddings
from app.components.language_models.huggingface_hub_language_model_strategy import HuggingFaceHubLanguageModelStrategy
from app.components.language_models.openai_language_model_strategy import OpenAiLanguageModel
from app.components.vectorstores.faiss_from_text_strategy import VectorStore


class Chatbot:
    def __init__(self, language_model: OpenAiLanguageModel, embeddings: Embeddings,
                 vector_store: VectorStore):
        self.language_model = language_model
        self.embeddings = embeddings
        self.vector_store = vector_store

    def answer_question(self, question):
        # Logic to answer a question using the language model and vector store
        response = self.language_model.generate_response(question=question, vector_store=self.vector_store)

        # todo: find out if this is useful for persisting chat history during a chat session
        self.context = response['chat_history']
        # self.context['chat_history'].append(response['chat_history'])

        return response['answer']

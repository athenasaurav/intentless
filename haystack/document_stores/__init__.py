import os
import importlib
from haystack.utils.import_utils import safe_import
from haystack.document_stores.base import BaseDocumentStore, BaseKnowledgeGraph, KeywordDocumentStore

from haystack.document_stores.memory import InMemoryDocumentStore
from haystack.document_stores.deepsetcloud import DeepsetCloudDocumentStore
from haystack.document_stores.utils import eval_data_from_json, eval_data_from_jsonl, squad_json_to_jsonl

ElasticsearchDocumentStore = safe_import(
    "haystack.document_stores.elasticsearch", "ElasticsearchDocumentStore", "elasticsearch"
)
OpenDistroElasticsearchDocumentStore = safe_import(
    "haystack.document_stores.elasticsearch", "OpenDistroElasticsearchDocumentStore", "elasticsearch"
)
OpenSearchDocumentStore = safe_import(
    "haystack.document_stores.elasticsearch", "OpenSearchDocumentStore", "elasticsearch"
)
elasticsearch_index_to_document_store = safe_import(
    "haystack.document_stores.elasticsearch", "elasticsearch_index_to_document_store", "elasticsearch"
)
open_search_index_to_document_store = safe_import(
    "haystack.document_stores.elasticsearch", "open_search_index_to_document_store", "elasticsearch"
)

SQLDocumentStore = safe_import("haystack.document_stores.sql", "SQLDocumentStore", "sql")
FAISSDocumentStore = safe_import("haystack.document_stores.faiss", "FAISSDocumentStore", "faiss")
PineconeDocumentStore = safe_import("haystack.document_stores.pinecone", "PineconeDocumentStore", "pinecone")
if os.getenv("MILVUS1_ENABLED"):
    MilvusDocumentStore = safe_import("haystack.document_stores.milvus1", "Milvus1DocumentStore", "milvus1")
else:
    MilvusDocumentStore = safe_import("haystack.document_stores.milvus2", "Milvus2DocumentStore", "milvus")
WeaviateDocumentStore = safe_import("haystack.document_stores.weaviate", "WeaviateDocumentStore", "weaviate")
GraphDBKnowledgeGraph = safe_import("haystack.document_stores.graphdb", "GraphDBKnowledgeGraph", "graphdb")

from datetime import datetime, timezone

from opensearchpy import OpenSearch

from app.config import settings

client = OpenSearch(
    hosts=[{"host": settings.opensearch_host, "port": settings.opensearch_port}],
    use_ssl=False,
    verify_certs=False,
)


def index_name_for_today() -> str:
    date_str = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    return f"{settings.index_prefix}-{date_str}"


def index_log(doc: dict) -> None:
    client.index(index=index_name_for_today(), body=doc)
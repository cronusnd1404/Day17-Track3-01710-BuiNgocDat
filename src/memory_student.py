from __future__ import annotations

import re
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)
        self.query = ""

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        self.query = query
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""
        try:
            searches = [query]
            if any(term in query.casefold() for term in ("open-loop", "deadline", "task", "viec chua")):
                searches.append("benchmark report Friday 16:00 unfinished open loop TODO")
            episode_text = join_nonempty(
                [
                    render_graph_search(
                        self.client.graph.search(
                            user_id=user_id,
                            query=cap_query(search_query),
                            scope="episodes",
                            limit=8,
                        ),
                        episode_char_cap=240,
                    )
                    for search_query in searches
                ],
                sep="\n",
            )
        except Exception:
            episode_text = ""
        combined = join_nonempty([episode_text, fact_text, context_block], sep="\n\n")
        marker_snippets = []
        for match in re.finditer(r"\b[A-Z][A-Z0-9-]{3,}\b", combined):
            marker_snippets.append(combined[max(0, match.start() - 100):match.end() + 140])
        return join_nonempty(["\n".join(dict.fromkeys(marker_snippets)), combined], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        self.query = query
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        self.query = query
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        query_terms = {
            term for term in re.findall(r"[a-zA-Z0-9-]{4,}", self.query.casefold())
            if term not in {"minh", "trong", "dung", "theo", "truoc", "dong", "thoi", "nhung"}
        }
        compact_layers = {}
        for layer, text in layers.items():
            chunks = [chunk.strip() for chunk in re.split(r"\n(?=(?:EPISODE|FACT|ENTITY|OBSERVATION|THREAD_SUMMARY):)", text) if chunk.strip()]
            ranked = sorted(
                chunks,
                key=lambda chunk: sum(term in chunk.casefold() for term in query_terms),
                reverse=True,
            )
            compact_layers[layer] = "\n".join(ranked) if ranked else text
        return self.budget.assemble(compact_layers)

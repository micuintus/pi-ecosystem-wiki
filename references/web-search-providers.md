---
title: Web Search Providers Used by Major AI Products
type: reference
updated: 2026-05-08
sources: []
tags: [web-search, reference]
---

# Web Search Providers Used by Major AI Products

What search backend powers web search in the leading AI chat
interfaces. Useful context for Pi users evaluating
[web search extensions](../ecosystem/web-search-extensions.md).

## Overview

| Product | Backend | Notes |
|---|---|---|
| **Gemini** (gemini.google.com) | **Google Search** | Native "Grounding with Google Search" — same index as google.com |
| **Claude.ai** | **Brave Search** | Confirmed by TechCrunch (Mar 2025) and FedRAMP docs |
| **Claude Code** | **Brave Search** | Same `web_search` server tool on Anthropic infra as claude.ai |
| **ChatGPT** | **Bing** (primary) + **OpenAI OAI-Searchbot index** + undisclosed others | Mix; OpenAI building own index to reduce MS dependency |
| **Le Chat** (Mistral) | **Brave Search** | Reverse-engineered before launch; Mistral docs don't disclose |

## Key patterns

**Brave Search is becoming the de facto standard for AI chat search.** Why:

- Independent index (no Bing dependency since 2023)
- Clean API designed for LLM/RAG use (`llm-context` mode)
- Privacy-friendly positioning
- Bing Search APIs retiring 2025-08-11 — Brave is the leading replacement
- Powers Claude.ai, Le Chat, and most MCP web-search integrations

**Gemini** is the obvious outlier — they own Google Search.

**ChatGPT** is the other outlier — partnered with Bing (Microsoft is an
investor) but building their own `OAI-Searchbot` crawler/index to
reduce dependency.

## Provider comparison (for AI agent use)

| Provider | Search Model | Strength | Weakness | Cost |
|---|---|---|---|---|
| **Exa** | Neural / embeddings-based semantic search | Best for code/technical docs; powers most large coding-agent companies; dedicated `WebCode` evals | Does not maintain a traditional web index; weaker for news/current events | $0.005–0.01/query |
| **Brave Search API** | Traditional keyword + ranking index | Broad web coverage, news, current events; 40B+ pages; independent index | More generic; less optimized for deep technical retrieval | $0.005/query; free tier (2K/mo) |
| **Perplexity** | Synthesized answers with citations | Great for research/questions requiring synthesis | Returns summary, not raw results — changes the RAG contract | $5/1K queries |
| **Gemini Grounding** | Google Search index | Massive coverage; free with Gemini API key or browser cookies | Tied to Google ecosystem; less control over retrieval | Free with API/browser |

## What Google does NOT offer

Google does not provide a general-purpose web search API for AI agents.
This is a key reason Brave is becoming the de facto standard.

| Google Product | Status / Limitation |
|---|---|
| **Custom Search JSON API** | Closed to new customers. Existing users must transition by 2027-01-01. $5/1K queries; only metadata (title/snippet/URL); no content extraction |
| **Programmable Search Engine** | Site-restricted; whole-web mode does not match google.com quality |
| **Vertex AI Search / Agent Search** | Enterprise RAG for your own data, not general web search |
| **Gemini "Grounding with Google Search"** | Only works when calling Gemini models via Google's API — not a standalone search API |

With Bing Search APIs retiring 2025-08-11 and Google never offering a
real replacement, **Brave is the last independent Western web search
index with a developer API**.

## Relevance to Pi

Pi extensions like `pi-web-access` support Exa, Perplexity, and Gemini
with auto-selection. Adding Brave matches the provider choice of
Claude.ai and Le Chat, improves general web/news coverage, and adds a
free-tier option. The multi-provider pattern is standard — no major AI
product relies on a single search backend.

For the Pi-side design rule on how to *expose* multiple backends to
the model (one tool with internal routing, not several visible tools),
see [Web Search Extensions — routing guidance](../ecosystem/web-search-extensions.md#routing-guidance-one-tool-internal-selection).

## See also

- [Web Search Extensions](../ecosystem/web-search-extensions.md) — Pi extensions that use these providers
- [Pi Ecosystem Catalogs](catalogs.md) — where to find more extensions


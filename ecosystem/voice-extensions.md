---
title: Pi Voice and Speech Extensions
type: ecosystem
updated: 2026-10-15
sources:
  - pi-voice
  - pi-voice-npm
  - pi-voice-catalog
  - pi-voice-recommendations
  - open-asr-leaderboard
  - s1m0n38-pi-voice
  - privateer-speak
  - pi-voicekit
  - picrophone
  - pi-voice-stt
tags: [extension, voice, stt, tts, dictation, transcription]
entries:
  - id: pi-voice
    name: "@earendil-works/pi-voice"
    repo: earendil-works/pi-voice
    npm: "@earendil-works/pi-voice"
    role: local-dictation
    notes: "First-party local speech-to-text: shortcut dictation into the prompt plus a `transcribe_file` agent tool, all on-device through downloaded models. No TTS. Successor to `pi-transcribe`."
  - id: privateer-speak
    name: privateer-speak
    repo: privateer-agent/privateer-speak
    npm: privateer-speak
    role: voice-out
    notes: "Catalog-level, not code-read. Replies read aloud as written plus recorded voice input, through pluggable providers."
  - id: pi-voice-stt
    name: pi-voice-stt
    repo: cgarrot/pi-voice-stt
    npm: pi-voice-stt
    role: dictation-key
    notes: "Catalog-level, not code-read. Ctrl+R dictation plus audio file transcription, provider-agnostic."
  - id: pi-voicekit
    name: pi-voicekit
    repo: CyFeng16/pi-voicekit
    npm: pi-voicekit
    role: both-directions
    notes: "Catalog-level, not code-read. Hold-to-talk STT plus TTS, Chinese and English, offline models or cloud."
  - id: picrophone
    name: picrophone
    npm: picrophone
    role: on-device-both
    notes: "Catalog-level, not code-read. On-device dictation and read-aloud bridge, macOS first."
  - id: s1m0n38-pi-voice
    name: S1M0N38/pi-voice
    repo: S1M0N38/pi-voice
    role: simplified-tts
    notes: "Catalog-level, not code-read. Simplified take on agent voice output, inspired by `pi-transcribe`."
---

# Pi Voice and Speech Extensions

For dictation and file transcription, first-party `pi-voice` is the
pick: local models, no cloud, no key. It does not speak back. For
replies read aloud, pair it with a voice-out extension.

## How `pi-voice` works

Mic audio is captured, cut into PCM chunks, filtered by a bundled
Silero VAD 6.2 model, and transcribed on-device by `transcribe-cpp`
(a Whisper-style local runner). Nothing leaves the machine. Audio and
video files go through the same pipeline after `ffmpeg` decodes them
(up to 512 MiB, about 2.3 hours). Setup is one `/voice-settings` run
to pick a model, which downloads from HuggingFace
([pi-voice-catalog]).

Two builds share the Pi-voice name and are easy to confuse. The
Parakeet `unified-en` build lists exactly one language (English); the
Parakeet TDT v3 build covers 25, German included. "Parakeet for
German" means the TDT build.

## Which model

Per-language error from the extension's own benchmark file, lower is
better ([pi-voice-recommendations]):

| Model | Size | English | German | Note |
|---|---|---|---|---|
| Parakeet unified-en 0.6B | 731 MB | 3.99% | no data (English only) | Best English dictation |
| Parakeet TDT v3 0.6B | 740 MB | 4.83% | 5.24% (25 languages) | The bilingual Parakeet; the v2 build is English-only |
| Cohere Transcribe 03-2026 | 2.4 GB | 5.08% | 5.06% | Balanced bilingual, Apache-2.0 |
| Canary 180m Flash | 218 MB | 5.98% | 7.33% | Tiny and fast, both languages |
| Whisper Medium | 830 MB | 4.64% | 6.23% (99 languages) | The fallback default |
| Voxtral Mini 4B realtime | 4.7 GB | 6.27% | 4.24% | Best bilingual accuracy, slower than realtime |

The independent HF Open ASR board (63 models, 7 datasets) agrees on
the ordering where they overlap: Cohere 6.26 and Parakeet TDT 6.43
average WER sit together, both clearly ahead of Whisper Large 7.84
and Canary 1B 7.91, with Parakeet far faster. Voxtral's weak board
average hides its German strength, and the board has no German split,
so the catalog's per-language figures decide that question
([open-asr-leaderboard]).

Licenses are mixed but all local: Whisper and Cohere Apache-2.0,
Silero VAD MIT, Parakeet and Canary CC-BY-4.0 (free weights with
attribution, not OSI FOSS).

## Voice out

`pi-voice` never speaks. The voice-out side:

- `privateer-speak`: `/speak` reads answers aloud as written,
  `/talk` records voice input, pluggable providers.
- `pi-voice-stt`: Ctrl+R dictation plus file transcription.
- `pi-voicekit`: hold-to-talk plus TTS, Chinese and English.
- `picrophone`: on-device both directions, macOS first.
- `S1M0N38/pi-voice`: simplified voice output.

## Picking a voice setup

| If you want | Use | Why |
|---|---|---|
| Dictate English prompts, transcribe files, nothing leaves the machine | `pi-voice` with Parakeet unified-en | Best English numbers, first-party maintenance |
| German in the mix | `pi-voice` with Parakeet TDT v3 or Cohere | TDT keeps the Parakeet family at full speed; Cohere matches it within 0.2 points in both languages |
| Replies read aloud | add `privateer-speak` | Most recently updated voice-out option verified (October 2026) |
| Smallest download that covers both languages | Canary 180m Flash | 218 MB, both languages, fastest |

## See also

- [Model Routing Extensions](model-routing-extensions.md): nothing
  voice-specific; routers treat transcription like any tool call
- [How to Evaluate a Pi Extension](../references/evaluation.md)

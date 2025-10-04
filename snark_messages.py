"""Gloriously excessive snark message generator and accessories."""

from __future__ import annotations

import itertools
import random
from typing import List


_ADJECTIVES = [
    "Velvet-clad",
    "Radioactive",
    "Hyper-sugared",
    "Intergalactic",
    "Dungeon-chic",
    "Laser-tongued",
    "Carnival-grade",
    "Mythically-sassy",
    "Aphrodisiac",
    "Void-kissed",
    "Galaxy-dripping",
    "Caffeine-lubed",
    "Tarantella-spun",
    "Whip-smart",
    "Corset-bound",
    "Aether-soaked",
    "Cathedral-neon",
    "Holographic",
    "Confetti-splattered",
    "Avalanche-polished",
    "Sugar-combusted",
    "Opera-drunk",
    "Ritual-inked",
    "Taffeta-armored",
    "Incense-stained",
    "Lava-gowned",
    "Stiletto-sharp",
    "Thunder-veiled",
    "Champagne-slick",
    "Voodoo-gilded",
    "Neon-strapped",
    "Saffron-smeared",
    "Quantum-laced",
    "Cloak-and-sparkle",
    "Molten-meringue",
    "Velour-armored",
    "Tinsel-fanged",
    "Champagne-foamed",
    "Siren-song",
    "Thunder-charged",
    "Jellyfish-lit",
    "Obsidian-glossed",
    "Bourbon-lacquered",
    "Euphoria-tuned",
    "Candle-wicked",
    "Cyborg-scented",
    "Honey-dipped",
    "Zephyr-stitched",
]

_ACTIONS = [
    "brig-hacked the backlog",
    "lassoed the feature flag",
    "snuggled the CI gremlin",
    "spanked the flaky test suite",
    "bedazzled the deploy cannon",
    "seduced the linter into silence",
    "pirouetted through merge conflict magma",
    "put glitter handcuffs on tech debt",
    "blessed the build pipeline with moonlight",
    "crowned the hotpath with velvet chains",
    "poured syrup over the cron daemon",
    "hosted a séance with failing lambdas",
    "arm-wrestled the OAuth hydra",
    "whispered dirtiest secrets to kubectl",
    "dipped the sprint board in liquid chrome",
    "necklaced the backlog with pearls of debt",
    "made scrum stand-ups vogue in heels",
    "drafted architecture on perfumed parchment",
    "lassoed runaway threads with glitter rope",
    "massaged observability dashboards with oil",
    "baptized the message queue in glitter",
    "tattooed the API gateway with lipstick",
    "saber-rattled the release train",
    "brewed espresso in the error budget",
    "loop-de-looped through canary cages",
    "auctioned deprecated endpoints for kisses",
    "dropped slow queries in a velvet oubliette",
    "shimmed the load balancer with rhinestones",
    "DJed the sprint review on neon turntables",
    "broke prod on purpose to make it stronger",
    "drove the monolith through a glitter carwash",
    "tucked microservices into satin coffins",
    "auctioned uptime to the highest flirt",
    "spritzed container logs with pheromones",
    "staged a drag revue inside kubernetes",
    "fed cron jobs champagne-drenched cherries",
    "phased the incident bridge into a rave",
    "tattooed compliance docs with gold leaf",
    "piped trace data into a lava lamp",
    "stargazed with load tests on velvet blankets",
    "wireframed the backlog using edible glitter",
    "whipped the API gateway into couture",
    "moisturized the message bus with cosmic aloe",
    "danced a tango with the release checklist",
    "perfumed the deployment with rosewater logs",
    "gift-wrapped feature flags in silk",
    "choreographed migrations to bass drops",
]

_TWISTS = [
    "now the servers purr consentingly",
    "leaving QA blushing in binary",
    "while stakeholders chant the safe word",
    "causing scrum masters to melt like wax",
    "summoning ghostly parrots from staging",
    "igniting KPI fireworks over the abyss",
    "as product managers sway in rope harnesses",
    "with compliance sipping cocktails on deck",
    "sending retro notes dripping in glitter",
    "so on-call rotations feel like spa days",
    "ensuring risk registers smell like roses",
    "convincing CTOs to exhale champagne",
    "making the incident timeline read like fanfic",
    "showering the SOC floor in holographic tinsel",
    "while documentation moans in markdown bliss",
    "painting SLO charts with ultraviolet mascara",
    "herding microservices into tantric alignment",
    "tickling SLAs until they sign prenups",
    "turning status pages into erotic tarot",
    "blessing pager rotations with silk blindfolds",
    "hushing burnout by fanning with peacock feathers",
    "wrapping OKRs in latex and lilacs",
    "teaching dashboards to purr lullabies",
    "making audit logs taste like champagne",
    "rendering OKRs in holographic hieroglyphs",
    "gifting the roadmap a diamond choke-chain",
    "tuning backlog whispers into club remixes",
    "turning uptime graphs into fireworks",
    "massaging retros until they confess secrets",
    "enchanting design docs to whisper sweet nothings",
    "sending SOC 2 reports to a candlelit spa",
    "teaching code reviews burlesque etiquette",
    "making load balancers hum lullabies",
    "transforming backlog grooming into cabaret",
    "brew-stretching SLIs on velvet racks",
    "turning threat models into oracle readings",
    "wrapping deploy windows with fox-fur stoles",
    "balancing error budgets on crystal goblets",
    "tickling SLIs until they leak secrets",
    "granting runbooks their own fan club",
    "ushering feature toggles into champagne baths",
    "bathing observability in ultraviolet glitter",
    "sending CAP dashboards on yacht vacations",
    "crowning sprint reviews with rhinestone tiaras",
    "teaching retrospectives tantric breathing",
    "coaxing blockers to confess over martinis",
    "turning pager duty into a moonlit picnic",
]

_EMOJI_SWIRL = [
    "🏴‍☠️🪩",
    "🧵🔥",
    "🪢💋",
    "🫧🚀",
    "🥵🌈",
    "🪬💣",
    "💿🍑",
    "🕯️🛸",
    "🧪🎠",
    "🦄🗡️",
    "🩸🎀",
    "🛁🪐",
    "🫦⚡",
    "🎩🧨",
    "🧿🪭",
    "🧊🫧",
    "🛼💎",
    "🧚‍♀️🗺️",
    "🎠🪄",
    "🪙🪞",
    "🧬🧿",
    "🩰🗡",
    "🪧💥",
    "🎢🧪",
    "🧜‍♀️✨",
    "🧲🌪",
    "🧘‍♂️🪻",
    "💋🌀",
    "🦕🥂",
    "🧨🪬",
    "🌋💄",
    "🧵🌀",
    "🛳️🕺",
    "🧲🖤",
    "🫀🧯",
    "🌪️🦋",
    "🥂🎧",
    "🧿🪽",
]


def _build_messages() -> List[str]:
    combos: List[str] = []
    for index, (adj, action, twist) in enumerate(
        itertools.product(_ADJECTIVES, _ACTIONS, _TWISTS)
    ):
        if index >= 1000:
            break
        emoji = _EMOJI_SWIRL[index % len(_EMOJI_SWIRL)]
        combos.append(f"{adj} {action}; {twist}. {emoji}")
    return combos


SNARKY_MESSAGES = _build_messages()
SNARKY_EXTRA_EMOJI = list(dict.fromkeys(_EMOJI_SWIRL))
SNARKY_BLAME_TAGS = [
    "@legacy",
    "@backend",
    "@frontend",
    "@ops",
    "@infra",
    "@ghost",
    "@intern",
    "@QA",
    "@deploy",
    "@unknown",
    "@gremlin",
    "@capn",
]


def pick_snarky_message(rng: random.Random | None = None) -> str:
    """Return a random snark message, optionally using the provided RNG."""

    chooser = rng or random
    return chooser.choice(SNARKY_MESSAGES)


def pick_snarky_extra_emoji(rng: random.Random | None = None) -> str:
    chooser = rng or random
    return chooser.choice(SNARKY_EXTRA_EMOJI)


def pick_snarky_blame_tag(rng: random.Random | None = None) -> str:
    chooser = rng or random
    return chooser.choice(SNARKY_BLAME_TAGS)


__all__ = [
    "SNARKY_MESSAGES",
    "SNARKY_EXTRA_EMOJI",
    "SNARKY_BLAME_TAGS",
    "pick_snarky_message",
    "pick_snarky_extra_emoji",
    "pick_snarky_blame_tag",
]

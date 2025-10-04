"""Gloriously excessive snark message generator and accessories."""

from __future__ import annotations

import random
from typing import List

# Structured components for grammatically consistent NSFW space-pirate snark.
_SUBJECTS = [
    "Captain Velvet, corseted corsair",
    "Mistress Nebula, whip-smart navigator",
    "Quartermaster Siren, honey-dipped enforcer",
    "Commodore Eclipse, velvet-clad raider",
    "Bosun Stardust, tether-toting rogue",
    "Madam Plasma, pleasure-charged pilot",
    "Lord Void, shibari-loving gunner",
    "Saint Kraken, incense-stained captain",
    "Oracle Mirage, corset-bound tactician",
    "Duchess Fathom, cat-o'-nine whisperer",
    "Baroness Flux, diamond-lashed hacker",
    "Admiral Oblivion, silk-haloed tyrant",
    "Sable Viper, collar-clinked saboteur",
    "Warden Hyperia, lash-happy helmswoman",
    "High Priestess Rum, dungeon-perfumed oracle",
    "Sir Zephyr, garter-wired privateer",
    "Countess Rift, latex-latticed code witch",
    "Matron Nebulon, chains-and-roses quartermaster",
    "Corsair Lumen, pleasure-shocked surgeon",
    "Marshal Abyss, tinsel-fanged executioner",
    "Countess Chainstorm, flogger-forged navigator",
    "High Inquisitor Tether, ball-gagged buccaneer",
    "Mistress Nebulace, latex-veiled raider",
    "Admiral Sirenlash, corset-strapped tactician",
    "Captain Gossamer, shackle-kissed provocateur",
    "Overseer Lashfire, rope-burnished ravager",
    "Dominator Starbane, dungeon-scented corsair",
    "Oracle Ironveil, safe-word sorceress",
    "Bosun Emberbite, whip-stitched taskmaster",
    "Seeress Darkwake, velvet-veiled oracle",
    "Matriarch Voidbloom, stiletto-bruised quartermaster",
]

_OPENERS = [
    "caught me against the trembling bulkhead",
    "sealed me to the figurehead with starlit chains",
    "swept me into the chart room's velvet shadow",
    "pressed me over the humming warp drive",
    "pinned me across the brig's obedient rail",
    "tethered me to the captain's oathstone",
    "dragged me below deck where planets spin",
    "kissed a rope-brand along my throat",
    "buckled me into the cryo-cradle of sinners",
    "hoisted me above the deck in shimmering rigging",
    "clasped cold cuffs around my fevered wrists",
    "cinched my waist with comet-lit corsetry",
    "slid a hook beneath my spine and laughed",
    "locked my ankles to the mast with nebulae",
    "braced me on the hull as meteors whispered",
]

_TIDES = [
    "while their voice dripped obsidian promises",
    "as silk lashes mapped constellations on my skin",
    "with a cat-o'-nine tail singing in slow, wicked arcs",
    "while irons steamed the scent of rum and salt",
    "as their gloved fingers traced consent sigils",
    "while hot candlewax spelled out forbidden tides",
    "with breathless murmurs of mutiny and surrender",
    "as pearls of sweat jeweled the leather straps",
    "while the ship AI begged to record every moan",
    "as the crew knelt, reciting the safe word in chorus",
]

_PLEDGES = [
    "I offered the map to my tidal heartbeat",
    "my pulse thrummed like rigging in a storm",
    "our hips marked time with the cannons' thunder",
    "I tasted plasma and paradise on their tongue",
    "we bartered oxygen for wicked devotion",
    "I promised them the treasure locked under my ribs",
    "the keel groaned in rhythm with our hunger",
    "their teeth signed the captain's log on my shoulder",
    "we rewrote the Articles of Plunder in sweat",
    "desire bloomed like a red sun over the horizon",
]

_FINALES = [
    "until the void itself shuddered and sighed",
    "while the figurehead wept jewels into the sea",
    "as star-whales crooned lullabies of aftercare",
    "until the brig applauded with rattling chains",
    "while the moon carved our names in phosphor",
    "as the crew toasted our ruin with black rum",
    "until the nebula outside painted us in auroras",
    "while cursed admirals begged for a turn",
    "until the mast surrendered its final knot",
    "as the Jolly Roger fluttered like a lover's gasp",
]

_EMOJI_SWIRL = [
    "🏴‍☠️🪢",
    "🛸🍑",
    "🪩🗡️",
    "🪝💋",
    "🪬🥵",
    "🧼🩸",
    "🧨🖤",
    "🫀🪠",
    "🪽🛸",
    "🧲🌪",
    "🧿🪽",
    "🪢🔥",
    "🩸🫦",
    "🧊🪢",
    "💍🪤",
    "🧴🦂",
]


def _build_messages() -> List[str]:
    combos: List[str] = []
    for idx in range(1000):
        subject = _SUBJECTS[(idx * 5) % len(_SUBJECTS)]
        opener = _OPENERS[(idx * 7) % len(_OPENERS)]
        tide = _TIDES[(idx * 11) % len(_TIDES)]
        pledge = _PLEDGES[(idx * 13) % len(_PLEDGES)]
        finale = _FINALES[(idx * 17) % len(_FINALES)]
        emoji = _EMOJI_SWIRL[idx % len(_EMOJI_SWIRL)]
        combos.append(
            f"{subject} {opener}, {tide}; {pledge}, {finale}. {emoji}"
        )
    return combos


SNARKY_MESSAGES = _build_messages()
SNARKY_EXTRA_EMOJI = list(dict.fromkeys(_EMOJI_SWIRL))
SNARKY_BLAME_TAGS = [
    "@bosun",
    "@captain",
    "@quartermaster",
    "@sirens",
    "@brig",
    "@galley",
    "@mutineer",
    "@corsair",
    "@helmsman",
    "@rigging",
    "@raiding-party",
    "@nebula",
]


def pick_snarky_message(rng: random.Random | None = None) -> str:
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

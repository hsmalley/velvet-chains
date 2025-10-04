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
    "caught me against the trembling bulkhead, breath hot with rum-drenched sin",
    "sealed me to the figurehead with starlit chains and a smile sharper than a cutlass",
    "pinned me to the brig's rail while nebulae swirled like voyeur ghosts",
    "pressed me over the humming warp drive, tasting my gasp like contraband",
    "dragged me to the oathstone and traced consent in phosphor kisses",
    "buckled me into the cryo cradle, promising thaw only for obedience",
    "hooked my spine into the rigging, humming shanties of soft surrender",
    "cinched comet-lit corsetry around my waist until gravity whimpered",
    "brushed brimstone lips along my throat and whispered mutiny",
    "tethered my wrists with silken moorings as planets spun jealous circles",
    "pressed the chill of a cutlass flat to my ribs, inviting me to beg",
    "swept me into the chart room where maps melted under our heat",
]

_TIDES = [
    "Each lash of the cat-o'-nine painted constellations down my spine",
    "Silk ropes braided the safe word around my pulse",
    "Leather gloves traced promises of pillage over every scar",
    "Chains sang hymns of desire against the bulkhead",
    "Hot candlewax spelled out forbidden ports upon my skin",
    "Breath heavy with bloodwine fogged my collarbones",
    "Suspension hooks rocked me like a storm-tossed mast",
    "Gilded manacles clicked like a maestro conducting sighs",
    "Razor-edged kisses tasted of gunpowder and surrender",
    "Velvet gags caught every plea and polished it into melody",
]

_PLEDGES = [
    "I traded the treasure map inked beneath my ribs for another strike",
    "We rewrote the Articles of Plunder line by sweating line",
    "My heartbeat hammered SOS against the hull until they answered",
    "We bartered oxygen for decadent devotion in the dark",
    "I swore fealty to their lash in the language of sighs",
    "The keel groaned harmony with our wicked duet",
    "They carved their rank into my shoulder with jeweled teeth",
    "We signed a treaty of lust with pearls and bruises",
    "Desire bloomed like a red dwarf beneath our skin",
    "I offered my pulse as collateral for another plunge",
]

_FINALES = [
    "Until the void shuddered and moaned like a satiated kraken",
    "While the Jolly Roger fluttered like a lover's gasp",
    "As star-whales crooned aftercare in distant harmonics",
    "Until the mast surrendered and the crew cheered for encore",
    "While cursed admirals begged to taste our ruin",
    "As the moon carved our names into phosphorescent foam",
    "Until the figurehead wept jewels into the hungry sea",
    "While the AI archived our every gasp for legend",
    "As the tide bowed and the stars promised silence",
    "Until dawn blushed scarlet across the scandalous deck",
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
    for idx in range(3000):
        subject = _SUBJECTS[(idx * 5) % len(_SUBJECTS)]
        opener = _OPENERS[(idx * 7) % len(_OPENERS)]
        tide = _TIDES[(idx * 11) % len(_TIDES)]
        pledge = _PLEDGES[(idx * 13) % len(_PLEDGES)]
        finale = _FINALES[(idx * 17) % len(_FINALES)]
        emoji = _EMOJI_SWIRL[idx % len(_EMOJI_SWIRL)]
        story = (
            f"{subject} {opener}. {tide}. {pledge}. {finale}. {emoji}"
        )
        combos.append(story)
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

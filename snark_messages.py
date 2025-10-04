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
    "Captain Ballast, rope-burnished rigger",
    "Harbormistress Thorn, strobe-lit strategist",
    "Enchantress Maelstrom, safe-word oracle",
    "Barbarossa Bliss, chandelier-spiked marauder",
    "Countess Chainstorm, flogger-forged navigator",
    "High Inquisitor Tether, ball-gagged buccaneer",
    "Mistress Nebulace, latex-veiled raider",
    "Admiral Sirenlash, corset-strapped tactician",
    "Captain Gossamer, shackle-kissed provocateur",
    "Overseer Lashfire, rope-burnished ravager",
    "Dominator Starbane, dungeon-scented corsair",
    "Oracle Ironveil, safe-word sorceress",
    "Bosun Emberbite, whip-stitched taskmaster",
]

_VERBS = [
    "chain-kissed",
    "tar-and-silk lashed",
    "electro-flogged",
    "velvet-gag sealed",
    "firmly corseted",
    "neon-brined",
    "astral-handcuffed",
    "bloodwine-baptised",
    "paddle-charmed",
    "tether-twirled",
    "lace-lassoed",
    "spice-dripped",
    "starlight-branded",
    "rum-splashed",
    "comet-bound",
    "satin-strapped",
    "meteor-whipped",
    "moonbeam-shackled",
    "void-collared",
    "galaxy-hogtied",
    "nebula-branded",
    "satellite-seared",
    "starline-choked",
    "thruster-nuzzled",
    "mutiny-muzzled",
    "corsair-caressed",
    "kraken-nipped",
    "pegleg-pinched",
    "plasma-bound",
]

_TARGETS = [
    "the warp drive's aching core",
    "the reactor bay's trembling idol",
    "the brig's obedient mutineers",
    "the captain's log of taboo secrets",
    "the chart room's throbbing holo-reef",
    "the galley stove purring for punishment",
    "the AI's blushing command nexus",
    "the cryo-pod of recalcitrant admirals",
    "the cloaking veil's fevered glyphs",
    "the cannon deck's quivering rails",
    "the navigation rune, eager for orders",
    "the plasma rig's submissive throttles",
    "the data shrine of contraband fantasies",
    "the lash locker of legendary safe words",
    "the cargo net of restrained starmaps",
    "the quantum sail's needy folds",
    "the brigantine's scandalous figurehead",
    "the forecastle's cowering deckhands",
    "the helm's sapphire manacles",
    "the rumor mill of kink-soaked admirals",
    "the brig's velvet-cloaked confessional",
    "the powder room's trembling cannonballs",
    "the captain's chair begging for ballast",
    "the plank slick with brine and honey",
    "the crow's nest of breathless lookouts",
    "the bowline of feverish star-whales",
    "the quarterdeck's chained figurehead",
    "the treasure hold's purring chest",
    "the aft thrusters aching for discipline",
]

_TAILS = [
    "while the crew chanted the safe word in pirate cant",
    "as the moonlit riggings hummed consent in octaves",
    "right before the bosun poured stardust over bruised hull plating",
    "with compliance officers fanning themselves on velvet loungers",
    "until the mutiny tribunal begged for another lash",
    "while parrots in latex hoods kept lookout",
    "as the flag of surrender fluttered like a corset ribbon",
    "while the engine room signed marriage contracts in bloodwine",
    "with the lookout tracing consent sigils across the mast",
    "while the galley served rum-glazed restraint bars",
    "as the nebula seduced the hull with ultraviolet moans",
    "while cannon smoke spelled out the safe word 'plunder'",
    "as the tide charts confessed their dirtiest currents",
    "with the helmsman kneeling on a throne of coiled chains",
    "while the ship's AI begged for another firmware flogging",
    "as the brig's restraints squealed in blissful harmony",
    "while the riggers braided silk tethers into the Jolly Roger",
    "as treasure maps inked themselves in suggestive constellations",
    "while ghostly admirals applauded from padded cells",
    "as the void outside purred like a satiated kraken",
    "while the mast ropes squealed for tighter knots",
    "as the powder monkeys begged for aftercare",
    "while the grog fountains overflowed with desire",
    "as constellations spelled out 'consent' in Morse",
    "while the bosun flogged the stars for rhythm",
    "as the cabin boy tuned sea-shanty safewords",
    "while the moon chained the tides to our keel",
    "as the galley simmered aphrodisiac stew",
    "while captured admirals inked apologies in glitter",
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
        verb = _VERBS[(idx * 7) % len(_VERBS)]
        target = _TARGETS[(idx * 11) % len(_TARGETS)]
        tail = _TAILS[(idx * 13) % len(_TAILS)]
        emoji = _EMOJI_SWIRL[idx % len(_EMOJI_SWIRL)]
        combos.append(f"{subject} {verb} {target}, {tail}. {emoji}")
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

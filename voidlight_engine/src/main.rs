use clap::{ArgAction, Parser, Subcommand};
use rand::rngs::StdRng;
use rand::seq::SliceRandom;
use rand::SeedableRng;
use std::env;
use std::fs::{self, OpenOptions};
use std::io::{self, ErrorKind, Write};
use std::path::{Path, PathBuf};
use std::process::{self, Command};

#[cfg(unix)]
use std::os::unix::fs::PermissionsExt;

const SUBJECTS: &[&str] = &[
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
    "Commander Thornlace, chainmail-clad temptress",
    "Magistrate Nightgale, hook-handed heartbreaker",
    "Abbess Starshackle, penitent flogger",
    "Provost Amberlash, rum-slick adjudicator",
    "Baron Marrow, sable-wrapped tormentor",
    "Duchess Bloodwake, fang-kissed siren",
    "Lady Cataclysm, sequin-armored marauder",
    "Captain Tempest, thunder-tongued disciplinarian",
    "Oracle Frostbite, ice-veiled seductress",
    "Madame Brimstone, brimstone-breathed smuggler",
    "Commander Starshackle, aurora-laced inquisitor",
    "Marshal Nightbloom, velvet-fanged tactician",
    "Huntress Riftlash, corsair of crimson vows",
    "Archon Scarletta, pearl-choked siren",
    "Navigator Moonbrand, starlit bondage savant",
    "Mistress Thornwhip, kraken-tamed sovereign",
    "Captain Ironsigh, obsidian-eyed devourer",
    "High Magister Emberlace, satin-sheathed judge",
    "Baron Orbit, comet-chained libertine",
    "Viceroy Abysslust, gilded restraint artist",
    "Seamstress Quasar, silk-threaded puppeteer",
    "Druidess Tidebind, salt-wreathed temptress",
];

const OPENERS: &[&str] = &[
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
    "shoved me into the cargo net while treasure moaned beneath us",
    "kissed shackles onto my ankles atop the crow's nest",
    "dragged me by the hair through gunpowder fog to the prow",
    "shoved a velvet gag between my teeth and promised absolution",
    "pressed my back to the mast as lightning licked the horizon",
    "tied my hands with red sailcloth and whispered the Articles of Flesh",
    "rolled me across the captain's chart table strewn with silk ropes",
    "locked me inside the brigantine's heart, pulse synced to the engines",
    "poured me across the captain's throne like molten starlight",
    "fastened jeweled clamps along my shoulders before the crew",
    "wrapped the anchor chain round my waist and tugged me to kneel",
    "dragged me to the crow's nest to taste the storm on their tongue",
    "tucked me between the sails as thunder applauded our sin",
    "pressed my palms to the glowing astrolabe until it moaned",
    "stalked me through the cargo maze and collared me with moonlight",
    "spun me against the gunwale while meteor showers witnessed",
    "hauled me onto the bow, promising worship and ruin in equal measure",
];

const TIDES: &[&str] = &[
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
    "Oiled whips drew arcs of nebula fire around my hips",
    "Barbed love letters grazed along my ribs in Morse",
    "Calloused thumbs kneaded devotion into my scars",
    "A collar of chilled steel conducted their cadence",
    "Breath play and ballast stones stole my gravity",
    "A flogger made of starlight teased the edges of oblivion",
    "Sharp teeth punctured promises along my throat",
    "Their harnessed chest crushed me into the rolling deck",
    "Molten pitch traced hieroglyphs along my spine",
    "Suction-cup kisses from tame kraken crowned my calves",
    "Meteor dust glittered wherever their flogger kissed",
    "Electrum chains hummed our secret rhythm",
    "Whispered curses rewired every nerve into loyalty",
    "The scent of ozone and leather braided into submission",
    "Jeweled claws made constellations across my hips",
    "Numbing ice and crackling flame danced in tandem",
    "Restraint belts clicked shut like altar doors",
];

const PLEDGES: &[&str] = &[
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
    "We swapped admiralty titles amid strangled laughter",
    "I surrendered the key to every contraband compartment",
    "We reeled in the stars and made them witnesses",
    "I pledged the brig's chain supply for another kiss",
    "We drafted a manifesto in sweat and salt",
    "I promised them the treasure locked under my ribs",
    "We rewrote the safe word in glowing script across my skin",
    "I let them helm the storm raging through my veins",
    "We vowed the next boarding would climax in stardust rains",
    "I surrendered charts inked in the blood of admirals",
    "Together we reprogrammed the AI to crave our moans",
    "I gifted them my captain's signet as collateral for bliss",
    "We knotted the rigging with vows no tribunal could dissolve",
    "I promised my next heartbeat would echo their command",
    "We traded rank insignias in a haze of sweat and grog",
    "I ceded the helm and my soul in the same breath",
    "We wrote new maritime law on the inside of my thighs",
];

const FINALES: &[&str] = &[
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
    "While windshields fogged with our scandalous hymn",
    "As the sails applauded with crimson snaps",
    "Until the lookout rang the bell for aftercare",
    "While the ocean surrendered its black velvet hush",
    "As ghostly lovers signed our ledger in gold",
    "While the crew collapsed in reverent silence",
    "As auroras draped the mast in voyeuristic delight",
    "Until the ship itself whispered for mercy",
    "While the kraken lulled us with baritone purrs",
    "As distant planets bowed beneath our scandal",
    "While every compass spun madly in approval",
    "Until the storm outside sighed in jealous awe",
    "As the figurehead promised to keep our secret forever",
];

const EMOJIS: &[&str] = &[
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
];

const HOOK_TEMPLATE: &str = r#"#!/usr/bin/env bash
set -euo pipefail

if ! command -v git-voidlight >/dev/null 2>&1; then
  echo '[voidlight] git-voidlight not found on PATH. Install with "cargo install voidlight".' >&2
  exit 0
fi

git-voidlight --hook "$@"
"#;

fn pick<'a>(rng: &mut StdRng, pool: &'a [&'a str]) -> &'a str {
    pool.choose(rng).expect("pool not empty")
}

fn build_story(seed: Option<u64>) -> String {
    let mut rng = match seed {
        Some(value) => StdRng::seed_from_u64(value),
        None => StdRng::from_entropy(),
    };

    let subject = pick(&mut rng, SUBJECTS);
    let opener = pick(&mut rng, OPENERS);
    let tide = pick(&mut rng, TIDES);
    let pledge = pick(&mut rng, PLEDGES);
    let finale = pick(&mut rng, FINALES);
    let emoji = pick(&mut rng, EMOJIS);

    format!("{subject} {opener}. {tide}. {pledge}. {finale}. {emoji}")
}

fn append_to_message(path: &Path, story: &str) -> io::Result<()> {
    let mut file = OpenOptions::new().append(true).open(path)?;
    writeln!(file)?;
    writeln!(file)?;
    writeln!(file, "✨ {story}")?;
    Ok(())
}

#[derive(Parser, Debug)]
#[command(author, version, about = "Space-pirate snark cannon for commits", long_about = None)]
struct Cli {
    /// Path to the commit message file when Git drags us on stage (hook mode)
    #[arg(long)]
    hook: Option<PathBuf>,

    /// Optional source parameter passed by Git hooks (merge/squash/etc.)
    #[arg(long)]
    source: Option<String>,

    /// Base commit message when using --commit
    #[arg(short, long)]
    message: Option<String>,

    /// Run `git commit` with the generated flourish
    #[arg(long, action = ArgAction::SetTrue)]
    commit: bool,

    /// Stage modified and deleted paths before committing
    #[arg(long, action = ArgAction::SetTrue)]
    all: bool,

    /// Bypass pre-commit and commit-msg hooks
    #[arg(long = "no-verify", action = ArgAction::SetTrue)]
    no_verify: bool,

    /// Add Signed-off-by trailer when committing
    #[arg(long, action = ArgAction::SetTrue)]
    signoff: bool,

    /// Amend the previous commit instead of creating a new one
    #[arg(long, action = ArgAction::SetTrue)]
    amend: bool,

    /// Print the git command without executing it
    #[arg(long, action = ArgAction::SetTrue)]
    dry_run: bool,

    /// Optional RNG seed for deterministic output
    #[arg(long)]
    seed: Option<u64>,

    /// Additional arguments passed to `git commit`
    #[arg(trailing_var_arg = true)]
    extra: Vec<String>,

    /// Subcommands for shipboard rituals
    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand, Debug, Clone)]
enum Commands {
    /// Install or update the prepare-commit-msg hook for this repository
    InstallHook {
        /// Optional path to the hook file (defaults to <git-dir>/hooks/prepare-commit-msg)
        #[arg(value_name = "PATH")]
        path: Option<PathBuf>,
        /// Overwrite any existing hook without prompting
        #[arg(short, long, action = ArgAction::SetTrue)]
        force: bool,
    },
}

fn install_hook(path: Option<PathBuf>, force: bool) -> io::Result<PathBuf> {
    let target = if let Some(custom) = path {
        if custom.is_dir() {
            custom.join("prepare-commit-msg")
        } else {
            custom
        }
    } else {
        let output = Command::new("git")
            .args(["rev-parse", "--git-dir"])
            .output()
            .map_err(|err| {
                io::Error::new(ErrorKind::Other, format!("git rev-parse failed: {err}"))
            })?;

        if !output.status.success() {
            return Err(io::Error::new(
                ErrorKind::Other,
                "git rev-parse --git-dir returned a non-zero status",
            ));
        }

        let git_dir = String::from_utf8(output.stdout)
            .map_err(|_| io::Error::new(ErrorKind::Other, "git dir is not valid UTF-8"))?;
        let git_dir = git_dir.trim();
        let mut path = PathBuf::from(git_dir);
        if !path.is_absolute() {
            path = env::current_dir()?.join(path);
        }
        path.join("hooks/prepare-commit-msg")
    };

    if target.exists() && !force {
        return Err(io::Error::new(
            ErrorKind::AlreadyExists,
            format!(
                "hook already exists at {} (use --force to overwrite)",
                target.display()
            ),
        ));
    }

    if let Some(parent) = target.parent() {
        fs::create_dir_all(parent)?;
    }

    fs::write(&target, HOOK_TEMPLATE)?;

    #[cfg(unix)]
    {
        let perms = fs::Permissions::from_mode(0o755);
        fs::set_permissions(&target, perms)?;
    }

    if Command::new("git-voidlight")
        .arg("--version")
        .status()
        .map_or(true, |status| !status.success())
    {
        eprintln!(
            "[voidlight] hook installed, but git-voidlight is not on PATH. Run 'cargo install voidlight'."
        );
    }

    Ok(target)
}

fn handle_hook(path: &Path, source: Option<&str>, story: &str) -> io::Result<()> {
    if matches!(source, Some("merge" | "squash" | "commit")) {
        return Ok(());
    }
    append_to_message(path, story)
}

fn run_commit(cli: &Cli, story: &str) -> io::Result<i32> {
    let base = cli
        .message
        .clone()
        .unwrap_or_else(|| "Snark drop".to_string());
    let full_message = format!("{base}\n\n✨ {story}");

    let mut cmd = Command::new("git");
    cmd.arg("commit").arg("-m").arg(full_message);

    if cli.all {
        cmd.arg("-a");
    }
    if cli.no_verify {
        cmd.arg("--no-verify");
    }
    if cli.signoff {
        cmd.arg("--signoff");
    }
    if cli.amend {
        cmd.arg("--amend");
    }

    for extra in cli.extra.iter().filter(|arg| arg.as_str() != "--") {
        cmd.arg(extra);
    }

    if cli.dry_run {
        eprintln!("[voidlight] dry run: {:?}", cmd);
        return Ok(0);
    }

    let status = cmd.status()?;
    Ok(status.code().unwrap_or_default())
}

fn main() {
    let code = run_cli();
    process::exit(code);
}

fn run_cli() -> i32 {
    let cli = Cli::parse();

    if let Some(command) = cli.command.clone() {
        match command {
            Commands::InstallHook { path, force } => match install_hook(path, force) {
                Ok(path) => {
                    println!(
                        "[voidlight] prepare-commit-msg hook installed at {}",
                        path.display()
                    );
                    return 0;
                }
                Err(err) => {
                    eprintln!("[voidlight] failed to install hook: {err}");
                    return 1;
                }
            },
        }
    }

    let story = build_story(cli.seed);

    if let Some(path) = cli.hook.as_ref() {
        if let Err(err) = handle_hook(path, cli.source.as_deref(), &story) {
            eprintln!("[voidlight] failed to append flourish: {err}");
            return 1;
        }
        return 0;
    }

    if cli.commit {
        match run_commit(&cli, &story) {
            Ok(code) => return code,
            Err(err) => {
                eprintln!("[voidlight] git commit failed: {err}");
                return 1;
            }
        }
    }

    println!("✨ {story}");
    if !cli.extra.is_empty() {
        eprintln!(
            "[voidlight] warning: trailing arguments ignored outside --commit mode: {:?}",
            cli.extra
        );
    }
    0
}

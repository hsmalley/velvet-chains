import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <meta
          name="description"
          content="A dark romance theatrical git toolchain for the discerning corsair developer, featuring spectacular choreographed commits and void-light whispers from beyond the stars."
        />
        <link rel="icon" href="favicon.svg" type="image/svg+xml" />
        {/* Google Fonts for dark romance typography */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
        <link
          href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Fira+Code:wght@300;400;500&display=swap"
          rel="stylesheet"
        />
        {/* Open Graph meta tags for social sharing spectacle */}
        <meta
          property="og:title"
          content="⚓ Velvet Chains - Dark Romance BDSM Space-Pirate Git Toolchain ⚓"
        />
        <meta
          property="og:description"
          content="Dark romance choreographed commits meet corsair aesthetics in this over-the-top git workflow system."
        />
        <meta property="og:type" content="website" />{' '}
        {/* Global styles moved to styles/globals.css */}
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}

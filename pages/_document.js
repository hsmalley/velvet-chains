import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head>
      <meta name="description" content="A dark romance theatrical git toolchain for the discerning corsair developer, featuring spectacular choreographed commits and void-light whispers from beyond the stars." />
      <link rel="icon" href="/favicon.ico" />

      {/* Google Fonts for dark romance typography */}
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
      <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Fira+Code:wght@300;400;500&display=swap" rel="stylesheet" />

      {/* Open Graph meta tags for social sharing spectacle */}
      <meta property="og:title" content="⚓ Velvet Chains - Dark Romance BDSM Space-Pirate Git Toolchain ⚓" />
      <meta property="og:description" content="Dark romance choreographed commits meet corsair aesthetics in this over-the-top git workflow system." />
      <meta property="og:type" content="website" />      {/* Additional styling for dark romance theatrical impact */}
      <style jsx global>{`
        * {
          box-sizing: border-box;
        }

        html {
          scroll-behavior: smooth;
        }

        ::selection {
          background: rgba(217, 70, 239, 0.4);
          color: #f3e8ff;
        }

        ::-webkit-scrollbar {
          width: 14px;
        }

        ::-webkit-scrollbar-track {
          background: linear-gradient(180deg, #1a0e1a, #2d1b3d);
        }

        ::-webkit-scrollbar-thumb {
          background: linear-gradient(180deg, #d946ef, #be123c);
          border-radius: 10px;
          border: 2px solid #1a0e1a;
        }

        ::-webkit-scrollbar-thumb:hover {
          background: linear-gradient(180deg, #be123c, #d946ef);
        }

        body::before {
          content: '';
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-image:
            radial-gradient(circle at 20% 80%, rgba(217, 70, 239, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(190, 18, 60, 0.1) 0%, transparent 50%);
          pointer-events: none;
          z-index: -1;
        }
      `}</style>
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}

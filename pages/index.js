// Next.js index page - displays the spectacular BRIG_BRIEFING content
import { useState, useEffect } from 'react'
import dynamic from 'next/dynamic'
import { MDXProvider } from '@mdx-js/react'
import Head from 'next/head'

// Dynamically import the BRIG_BRIEFING.mdx file
const BrigBriefing = dynamic(() => import('../BRIG_BRIEFING.mdx'), {
  loading: () => (
    <div style={{ color: '#e8d5e8', textAlign: 'center', padding: '2rem' }}>
      Loading the cosmic spectacle...
    </div>
  ),
})

const Callout = ({ type, emoji, children }) => (
  <div
    style={{
      padding: '2rem',
      borderRadius: '15px',
      border: '2px solid',
      borderColor: type === 'warning' ? '#d946ef' : type === 'info' ? '#9333ea' : '#be123c',
      background:
        type === 'warning'
          ? 'linear-gradient(135deg, rgba(0, 0, 0, 0.98), rgba(1, 0, 0, 0.99))'
          : type === 'info'
            ? 'linear-gradient(135deg, rgba(0, 0, 0, 0.98), rgba(1, 0, 1, 0.99))'
            : 'linear-gradient(135deg, rgba(0, 0, 0, 0.98), rgba(1, 0, 0, 0.99))',
      marginBottom: '2rem',
      color: '#e8d5e8',
      boxShadow:
        type === 'warning'
          ? '0 6px 20px rgba(217, 70, 239, 0.3)'
          : type === 'info'
            ? '0 6px 20px rgba(147, 51, 234, 0.3)'
            : '0 6px 20px rgba(190, 18, 60, 0.3)',
      backdropFilter: 'blur(10px)',
    }}
  >
    <div
      style={{
        fontWeight: 'bold',
        marginBottom: '0.5rem',
        fontSize: '1.1rem',
      }}
    >
      {emoji} {children}
    </div>
  </div>
)

const Card = ({ icon, title, children }) => (
  <div
    style={{
      border: '2px solid rgba(217, 70, 239, 0.4)',
      borderRadius: '18px',
      padding: '2rem',
      background: 'linear-gradient(145deg, rgba(0, 0, 0, 0.98), rgba(1, 0, 0, 0.99))',
      boxShadow: '0 15px 40px rgba(217, 70, 239, 0.3)',
      backdropFilter: 'blur(15px)',
      transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
      position: 'relative',
      overflow: 'hidden',
    }}
  >
    <h3
      style={{
        margin: '0 0 1.5rem 0',
        display: 'flex',
        alignItems: 'center',
        gap: '0.75rem',
        background: 'linear-gradient(45deg, #d946ef, #be123c)',
        WebkitBackgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
        backgroundClip: 'text',
        fontSize: '1.3rem',
        fontWeight: 'bold',
        textShadow: '0 0 15px rgba(217, 70, 239, 0.4)',
      }}
    >
      <span style={{ fontSize: '1.5rem' }}>{icon}</span> {title}
    </h3>
    <div style={{ color: '#e8d5e8', lineHeight: '1.6' }}>{children}</div>
  </div>
)

const Cards = ({ children }) => (
  <div
    style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
      gap: '2rem',
      marginBottom: '3rem',
    }}
  >
    {children}
  </div>
)

// Create the components object for MDX
const components = {
  Callout,
  Card,
  Cards,
}

export default function Home() {
  return (
    <>
      <Head>
        <title>⚓ Velvet Chains - The Ultimate BDSM Space-Pirate Romance Git Toolchain ⚓</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <div
        style={{
          maxWidth: '1200px',
          margin: '0 auto',
          padding: '2rem',
        }}
      >
        {/* Provide styled components to MDX content */}
        <MDXProvider components={components}>
          <BrigBriefing />
        </MDXProvider>
      </div>
    </>
  )
}

/*const withMDX = require('@next/mdx')({
  extension: /\.mdx?$/,
  options: {
    // Remove plugins for now to debug the issue
  },
})import('next').NextConfig} */

const withMDX = require('@next/mdx')({
  extension: /\.mdx?$/,
  options: {
    // Simplified configuration to avoid plugin issues
    providerImportSource: "@mdx-js/react",
  },
})

const nextConfig = {
  // Configure for GitHub Pages - only in production
  basePath: process.env.NODE_ENV === 'production' ? '/velvet-chains' : '',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/velvet-chains/' : '',

  // Enable static exports
  output: 'export',
  trailingSlash: true,

  // Disable server-side image optimization for static export
  images: {
    unoptimized: true
  },

  // Configure MDX
  pageExtensions: ['ts', 'tsx', 'js', 'jsx', 'md', 'mdx'],

  // Experimental features for better MDX support
  experimental: {
    mdxRs: false,
  },

  // Custom webpack config for better MDX handling
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.resolve.fallback = {
        ...config.resolve.fallback,
        fs: false,
      }
    }
    return config
  },

  // Environment variables for build info
  env: {
    NEXT_PUBLIC_BUILD_TIME: new Date().toISOString(),
    NEXT_PUBLIC_REPO_NAME: 'velvet-chains',
    NEXT_PUBLIC_REPO_OWNER: 'hsmalley',
  },
}

module.exports = withMDX(nextConfig)

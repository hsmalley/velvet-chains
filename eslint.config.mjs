import nextCoreWebVitals from 'eslint-config-next/core-web-vitals'
import prettier from 'eslint-config-prettier'

const corsairLintConfig = [
  ...nextCoreWebVitals,
  {
    ignores: ['build/**', 'coverage/**', 'dist/**', 'public/**'],
  },
  prettier,
]

export default corsairLintConfig

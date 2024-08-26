/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'media',
  content: [],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    function ({ addUtilities }) {
      addUtilities({
        '.no-scrollbar': {
          '-ms-overflow-style': 'none', /* Internet Explorer 10+ */
          'scrollbar-width': 'none', /* Firefox */
        },
        '.no-scrollbar::-webkit-scrollbar': {
          'display': 'none', /* Safari and Chrome */
        },
      })
    }
  ],
}


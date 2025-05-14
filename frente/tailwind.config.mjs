/** @type {import('tailwindcss').Config} */



export default {
  content: [
    './src/**/*.{astro,html,js,svelte,ts,md,mdx,css}', 
    './node_modules/flowbite-svelte/**/*.{astro,html,js,svelte,ts,md,mdx,css}',
    './node_modules/flowbite/**/*.{astro,html,js,svelte,ts,md,mdx,css}'
  ],
  darkMode: 'selector',
  theme: {
    extend: {
      colors: {
        // flowbite-svelte
          // violet
          primary: {"50":"#f5f3ff","100":"#ede9fe","200":"#ddd6fe","300":"#c4b5fd","400":"#a78bfa","500":"#8b5cf6","600":"#7c3aed","700":"#6d28d9","800":"#5b21b6","900":"#4c1d95"}
      }
    }
  },
  plugins: [
    require('@tailwindcss/typography'), 
    require('flowbite/plugin')
  ]
};


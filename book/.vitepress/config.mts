import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "The Simplest Bitcoin Book Ever Written",
  description: "to orange-pill (verb): the act of explaining bitcoin in such a way that a pre-coiner gets it, and becomes a bitcoiner!",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'The Book', link: '/chapters/01-why-we-need/' }
    ],

    sidebar: [
      {
        text: 'Chapters',
          items: [
              {text: '01 - Why We Need Bitcoin', link: '/chapters/01-why-we-need/'},
              {text: '02 - Bitcoin Fixes This', link: '/chapters/02-bitcoin-fixes-this/'},
              {text: '03 - What Is Bitcoin', link: '/chapters/03-what-is-bitcoin/'},
              {text: '04 - How Does Bitcoin Work', link: '/chapters/04-how-does-bitcoin-work/'},
              {text: '05 - A Word On The Lightning Network', link: '/chapters/05-word-on-lightning-network/'},
              {text: '06 - How To Bitcoin', link: '/chapters/06-how-to-bitcoin/'},
              {text: '07 - On Privacy', link: '/chapters/07-on-privacy/'},
              {text: '08 - Dispelling Bitcoin Fud', link: '/chapters/08-dispelling-bitcoin-fud/'},
              {text: '09 - Why Bitcoin Only?', link: '/chapters/09-why-bitcoin-only/'},
              {text: '010 - Satoshi’s Numbers 369 Clock', link: '/chapters/010-satoshis-numbers/'},
              {
                  text: '011 - Resources For The  Bitcoin Rabbit Hole',
                  link: '/chapters/011-resources-for-the-bitcoin-rabbit-hole/'
              },
              {text: '012 - Bitcoin Community Projects', link: '/chapters/012-bitcoin-community-projects/'},
              {text: '013 - Bitcoin Induced Ponderings', link: '/chapters/013-bitcoin-induced-ponderings/'},
              {text: '014 - A Cypherpunk’s Manifesto', link: '/chapters/014-a-cypherpunk-manifesto/'},
              {text: '015 - The Bitcoin White Paper', link: '/chapters/015-the-bitcoin-white-paper/'},
              {text: '016 - Nostr', link: '/chapters/016-nostr/'},
          ]
      },
      {
        text: 'Resources',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/b-n-space' },
      { icon: 'twitter', link: 'https://twitter.com/SimplestBTCBook' }
    ]
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en'
    },
    ar: {
      label: 'عربي',
      lang: 'ar', // optional, will be added  as `lang` attribute on `html` tag
      dir: 'rtl'
    }
  }
})

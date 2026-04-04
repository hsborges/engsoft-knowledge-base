// @ts-check

const config = {
  title: "Engsoft Knowledge Base",
  tagline: "Documentacao institucional organizada",

  url: "https://hsborges.github.io",
  baseUrl: "/engsoft-knowledge-base/",

  onBrokenLinks: "warn",
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: "warn"
    }
  },

  i18n: {
    defaultLocale: "pt-BR",
    locales: ["pt-BR"]
  },

  presets: [
    [
      "classic",
      {
        docs: {
          path: "docs",
          routeBasePath: "/",
          sidebarPath: require.resolve("./sidebars.js")
        },
        blog: false,
        pages: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css")
        }
      }
    ]
  ],

  plugins: [
    [
      require.resolve("docusaurus-lunr-search"),
      {
        languages: ["pt"]
      }
    ]
  ],

  themeConfig: {
    navbar: {
      title: "ES/FACOM/UFMS Docs",
      items: [
        {
          type: "docSidebar",
          sidebarId: "mainSidebar",
          position: "left",
          label: "Documentacao"
        }
      ]
    }
  }
};

module.exports = config;

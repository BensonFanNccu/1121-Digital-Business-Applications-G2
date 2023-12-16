/** @type { import('@storybook/vue-webpack5').StorybookConfig } */

const config = {
  stories: ["../src/**/*.mdx", "../src/stories/**/*.stories.@(js|jsx)"],
  addons: [
    "@storybook/addon-links",
    "@storybook/addon-essentials",
    "@storybook/addon-interactions",
  ],
  framework: {
    name: "@storybook/vue-webpack5",
    options: {
    },
  },
  docs: {
    autodocs: "tag",
    options: {
      configureJSX: true,
      sourceLoaderOptions: {
        injectStoryParameters: true,
      },
      // Set the default mode to "auto"
      source: {
        type: 'auto',
      },
    },
  },
};
export default config;

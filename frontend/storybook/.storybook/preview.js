/** @type { import('@storybook/vue').Preview } */
const preview = {
  parameters: {
    actions: { argTypesRegex: "^on[A-Z].*" },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
    storySort: {
      method: 'alphabetical',
      order: ['Overview 總覽', 'General 一般', 'Layout 佈局', 'Navigation 導航', 'Data Entry 數據錄入', 'Data Display 數據呈現', 'Feedback 反饋', 'Other 其他'],
    }
  },
};

export default preview;

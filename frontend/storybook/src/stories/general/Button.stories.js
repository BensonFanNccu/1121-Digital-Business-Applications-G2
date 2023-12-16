// src/stories/general/Button.stories.js

import MyButton from '../../components/Button.vue';
import { IconNames } from '../../components/IconNames.js';

// More on how to set up stories at: https://storybook.js.org/docs/vue/writing-stories/introduction
export default {
  title: 'General 通用/Button 按鈕',
  component: MyButton,
  tags: ['autodocs'],

  render: (args, { argTypes }) => ({
    props: Object.keys(argTypes),
    components: { MyButton },
    template: `<my-button @onClick="onClick" v-bind="$props"/>`,
  }),

  argTypes: {
    size: {
      control: { type: 'radio' },
    },
    theme: {
      control: { type: 'radio'},
    },
    icon: {
      control: { type: 'select' },
      options: IconNames,
    },
    disabled: {
      control: { type: 'boolean' },
    },
  },
};

// More on writing stories with args: https://storybook.js.org/docs/vue/writing-stories/args
export const Filled = {
  args: {
    label: 'Button',
    theme: 'filled'
  },
};

export const Outline = {
  args: {
    label: 'Button',
    theme: 'outline'
  },
};

export const Flat = {
  args: {
    label: 'Button',
    theme: 'flat'
  },
};

export const Floating = {
  args: {
    label: 'Button',
    theme: 'floating'
  },
};

export const Large = {
  args: {
    size: 'large',
    label: 'Button',
  },
};

export const Medium = {
  args: {
    size: 'medium',
    label: 'Button',
  },
};

export const Small = {
  args: {
    size: 'small',
    label: 'Button',
  },
};

export const Icon_Label = {
  args:{
    icon: 'plus',
    label: 'Button'
  }
}

export const Icon_Only = {
  args:{
    icon: 'plus',
  }
}

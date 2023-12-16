import MyIcon from '../../components/Icons.vue';
import { IconNames } from '../../components/IconNames.js';


// More on how to set up stories at: https://storybook.js.org/docs/vue/writing-stories/introduction
export default {
  title: 'General 通用/Icons 圖標',
  component: MyIcon,
  tags: ['autodocs'],
  
  render: (args, { argTypes }) => ({
    props: Object.keys(argTypes),
    components: { MyIcon },
    template: `<my-icon v-bind="$props"/>`,
  }),

  argTypes: {
    name: {
      control: { type: 'select' },
      options: IconNames,
    },
    size: {
      control: { type: 'inline-radio' },
    },
    color: {
      control: { type: 'select' },
    },
  },
};

export const example = {
  args: {
    name: 'activity',
    size: 16
  },
};
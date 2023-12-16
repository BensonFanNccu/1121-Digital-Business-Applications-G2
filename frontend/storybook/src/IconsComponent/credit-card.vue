<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="width" :height="height" :viewBox=viewBox :fill="fill" :stroke="stroke"
    :stroke-width="stroke-width" stroke-linecap="round" stroke-linejoin="round" class="feather feather-credit-card"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line>
  </svg>
</template>

<script>
export default {
  name: 'icon-credit-card',
  props: {
    width: {
      type: String,
      default: '16',
    },
    height: {
      type: String,
      default: '16',
    },
    viewBox: {
      type: String,
      default: '0 0 24 24',
    },
    stroke: {
      type: String,
      default: '#000000',
    },
    fill: {
      type: String,
      default: 'none',
    },
    'stroke-width': {
      type: String,
      default: '1',
    },
  },
};
</script>
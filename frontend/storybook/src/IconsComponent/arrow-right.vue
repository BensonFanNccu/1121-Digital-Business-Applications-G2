<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="width" :height="height" :viewBox=viewBox :fill="fill" :stroke="stroke"
    :stroke-width="stroke-width" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline>
  </svg>
</template>

<script>
export default {
  name: 'icon-arrow-right',
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
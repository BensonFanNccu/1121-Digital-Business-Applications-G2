<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="width" :height="height" :viewBox=viewBox :fill="fill" :stroke="stroke"
    :stroke-width="stroke-width" stroke-linecap="round" stroke-linejoin="round" class="feather feather-wind"><path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"></path>
  </svg>
</template>

<script>
export default {
  name: 'icon-wind',
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
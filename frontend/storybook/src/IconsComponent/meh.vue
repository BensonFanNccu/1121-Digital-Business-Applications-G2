<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="width" :height="height" :viewBox=viewBox :fill="fill" :stroke="stroke"
    :stroke-width="stroke-width" stroke-linecap="round" stroke-linejoin="round" class="feather feather-meh"><circle cx="12" cy="12" r="10"></circle><line x1="8" y1="15" x2="16" y2="15"></line><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line>
  </svg>
</template>

<script>
export default {
  name: 'icon-meh',
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
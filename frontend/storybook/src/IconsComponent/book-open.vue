<template>
  <svg xmlns="http://www.w3.org/2000/svg" :width="width" :height="height" :viewBox=viewBox :fill="fill" :stroke="stroke"
    :stroke-width="stroke-width" stroke-linecap="round" stroke-linejoin="round" class="feather feather-book-open"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
  </svg>
</template>

<script>
export default {
  name: 'icon-book-open',
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
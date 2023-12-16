<template>
  <div>
    <div v-show="isVisible" ref="myDiv">
      这是一个可见的 元素
    </div>
    <button @click="toggleVisibility">切换可见性</button>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      isVisible: true,
    };
  },
  mounted() {
    document.addEventListener('click', this.checkOutsideClick);
  },
  beforeUnmount() {
    document.removeEventListener('click', this.checkOutsideClick);
  },
  methods: {
    checkOutsideClick(event) {
      if (!this.$refs.myDiv || !this.$refs.myDiv.contains(event.target)) {
        this.isVisible = true;
      }
    },
    toggleVisibility() {
      this.isVisible = !this.isVisible;
    }
  }
};
</script>
  
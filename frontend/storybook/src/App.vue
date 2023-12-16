<template lang="pug">
#app 
  my-switch(v-model="switchValue")
</template>

<script>

import MySwitch from './components/Switch.vue'

export default {
  name: 'App',
  components: {
    MySwitch
  }
}
</script>

<style lang="sass">
#app
  font-family: Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #2c3e50
  margin-top: 60px
</style>

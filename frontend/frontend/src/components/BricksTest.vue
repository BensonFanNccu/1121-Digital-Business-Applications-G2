<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "BricksTest", //should be multi-word
  data() {
    return {
      msg: "Not Found",
    };
  },
  methods: {
    getResponse() {
      const path = "http://127.0.0.1:5000/bricks";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
